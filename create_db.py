import sqlite3
import os.path
from Repository import repo
from Dao import _Courses
from Dto import Course
from Dao import _Students
from Dto import Student
from Dao import _Classrooms
from Dto import Classroom
import sys


if os.path.isfile("schedule.db") :
    dbcon = sqlite3.connect('schedule.db')
    with dbcon:
        cursor = dbcon.cursor()
        repo.create_tables()
        config = sys.argv[1]
        file = open(config, 'r')
        for line in file :
            if not line == "" :
                letter = line[0]
                if letter == 'C' :
                    args = line.split(', ', 7)
                    cursor.execute("INSERT INTO courses VALUES (?,?, ?, ?, ?, ?)", (args[1], args[2], args[3], args[4], args[5], args[6]))

                elif letter == 'S' :
                    args = line.split(', ', 3)
                    cursor.execute("INSERT INTO students VALUES (?,?)", (args[1], args[2]))

                elif letter == 'R' :
                    args = line.split(', ', 3)
                    cursor.execute("INSERT INTO classrooms VALUES (?,?, ?, ?)", (args[1], args[2][:len(args[2])-1], 0, 0))

        print("courses")
        cursor.execute("SELECT * FROM Courses")
        courses = cursor.fetchall()
        for course in courses :
            print(course)

        print("classrooms")
        cursor.execute("SELECT * FROM Classrooms")
        classrooms = cursor.fetchall()
        for classroom in classrooms:
            print(classroom)

        print("students")
        cursor.execute("SELECT * FROM Students")
        students = cursor.fetchall()
        for student in students:
            print(student)

        dbcon.commit()
dbcon.close()
