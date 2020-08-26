class Course:
    def __init__(self, id, course_name, student, number_of_students, class_id, course_length):
        self.id = id
        self.course_name = course_name
        self.student = student
        self.number_of_students = number_of_students
        self.class_id = class_id
        self.course_length = course_length

class Student:
    def __init__(self, grade, count):
        self.grade = grade
        self.count = count

class Classroom:
    def __init__(self, id, location, current_course_id, current_course_time_left):
        self.id = id
        self.location = location
        self.current_course_id = current_course_id
        self.current_course_time_left = current_course_time_left