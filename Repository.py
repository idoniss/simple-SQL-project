import sqlite3
import atexit
from Dao import _Students
from Dao import _Courses
from Dao import _Classrooms
import os.path


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('schedule.db')
        self.courses = _Courses(self._conn)
        self.students = _Students(self._conn)
        self.classrooms = _Classrooms(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
          CREATE TABLE courses (
            id  INTEGER PRIMARY KEY,
            course_name TEXT    NOT NULL,
            student TEXT    NOT NULL,
            number_of_students   INTEGER NOT NULL,
            class_id    INTEGER REFERENCES classrooms(id),
            course_length   INTEGER NOT NULL
        );

        CREATE TABLE students (
            grade   TEXT PRIMARY KEY,
            count   INTEGER NOT NULL
        );

        CREATE TABLE classrooms (
            id  INTEGER PRIMARY KEY,
            location    TEXT    NOT NULL,
            current_course_id   INTEGER NOT NULL,
            current_course_time_left    INTEGER NOT NULL
        );
    """)


# the repository singleton
repo = _Repository()
atexit.register(repo._close)