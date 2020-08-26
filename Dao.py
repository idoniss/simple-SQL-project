import inspect
from Dto import Student
from Dto import Classroom
from Dto import Course


class _Courses:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, course):
        self._conn.execute("""
                INSERT INTO courses (id, course_name, student, number_of_students, class_id, course_length) VALUES (?, ?, ?, ?, ?, ?)
        """, [course.id, course.course_name, course.student, course.number_of_student, course.class_id, course.course_length])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT * FROM courses WHERE id=(?)
            """, [id])

        return Course(*c.fetchone())

    def num_of_courses(self):
        c = self._conn.cursor()
        c.execute("""
                SELECT COUNT(id) FROM Courses
            """)
        return c.fetchone()[0]

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
             SELECT * FROM Courses
         """).fetchall()

        return [Course(*row) for row in all]

    def delete_course(self, id):
        c = self._conn.cursor()
        c.execute("""
                DELETE FROM courses WHERE id=(?)""", [id])

    def find_by_class_id(self, classroom_id):
        c = self._conn.cursor()
        c.execute("""
                SELECT * FROM courses WHERE class_id = (?)""", [classroom_id])
        cursor_fetch = c.fetchone()
        if cursor_fetch is not None:
            return Course(*cursor_fetch)
        else:
            return None

    def find_all_by_tuple(self):
        c = self._conn.cursor()
        all_tuples = c.execute("""
                      SELECT id, course_name, student, number_of_students, class_id, course_length FROM courses
                """).fetchall()
        return all_tuples

class _Students:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, grade, count):
        self._conn.execute("""
               INSERT INTO students VALUES (?, ?)
           """, [grade, count])

    def find(self, grade):
        c = self._conn.cursor()
        c.execute("""
            SELECT grade, count FROM students WHERE grade = ?
        """, [grade])

        return Student(*c.fetchone())

    def deduct_amount_by_type(self, student, num_to_deduct):
        self._conn.execute("""
                UPDATE students SET count = (?) WHERE grade = (?) """, [student.count-num_to_deduct, student.grade])

    def find_all_by_tuple(self):
        c = self._conn.cursor()
        all_tuples = c.execute("""
            SELECT grade, count FROM students""").fetchall()
        return all_tuples


class _Classrooms:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, classroom):
        self._conn.execute("""
            INSERT INTO classrooms (id, location, current_course_id, current_course_time_left) VALUES (?, ?, ?, ?)
        """, [classroom.id, classroom.location, classroom.current_course_id, classroom.current_course_time_left])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, location, current_course_id, current_course_time_left FROM classrooms WHERE id=(?)
        """, [id])

        return Classroom(*c.fetchone())

    def update_course(self, id, course_id, course_length):
        self._conn.execute("""
               UPDATE classrooms SET current_course_id = (?), current_course_time_left = (?) WHERE id = (?)
               """, [course_id, course_length, id])

    def decrease_time(self, classroom):
        self._conn.execute("""
                UPDATE classrooms SET current_course_time_left=(?) WHERE id=(?)""", [classroom.current_course_time_left-1, classroom.id])

    def reset_classroom(self, classroom):
        self._conn.execute("""
                UPDATE classrooms SET current_course_id = 0 WHERE id = (?)""", [classroom.id])

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, location, current_course_id, current_course_time_left FROM classrooms
        """).fetchall()

        return [Classroom(*row) for row in all]

    def find_all_by_tuple(self):
        c = self._conn.cursor()
        all_tuples = c.execute("""
                   SELECT id, location, current_course_id, current_course_time_left FROM classrooms
               """).fetchall()
        return all_tuples