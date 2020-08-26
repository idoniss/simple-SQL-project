import sqlite3
import os
from Repository import repo
from Dao import _Courses

dbcon = sqlite3.connect('schedule.db')
cursor = dbcon.cursor()
databaseexist = os.path.isfile("schedule.db")
num_of_courses = repo.courses.num_of_courses()
counter = 0
if num_of_courses > 0 :
    while databaseexist and num_of_courses > 0 :
        classrooms = repo.classrooms.find_all()
        # courses = repo.courses.find_all()
        for classroom in classrooms:
            if counter == 0 and classroom.current_course_time_left == 0:
                current_course = repo.courses.find_by_class_id(classroom.id)

                if current_course is not None :
                    repo.classrooms.update_course(classroom.id, current_course.id, current_course.course_length)
                    student = repo.students.find(current_course.student)
                    repo.students.deduct_amount_by_type(student, current_course.number_of_students)
                    print("(" + str(counter) + ") " + classroom.location + ": " + current_course.course_name + " is schedule to start")

            elif classroom.current_course_time_left > 1 :
                curr_course = repo.courses.find(classroom.current_course_id)
                print("(" + str(counter) + ") " + classroom.location + ": occupied by " + curr_course.course_name)
                repo.classrooms.decrease_time(classroom)

            elif classroom.current_course_time_left == 1 and counter != 0 :
                if(classroom.current_course_time_left != 0):
                    curr_course = repo.courses.find(classroom.current_course_id)
                    print("(" + str(counter) + ") " + classroom.location + ": " + curr_course.course_name + " is done")
                    repo.classrooms.decrease_time(classroom)
                    repo.classrooms.reset_classroom(classroom)
                    repo.courses.delete_course(curr_course.id)
                    num_of_courses = num_of_courses - 1
                    next_course = repo.courses.find_by_class_id(classroom.id)
                    if next_course is not None :
                        print("(" + str(counter) + ") " + classroom.location + ": " + next_course.course_name + " is schedule to start")
                        repo.classrooms.update_course(classroom.id, next_course.id, next_course.course_length)
                        student = repo.students.find(next_course.student)
                        repo.students.deduct_amount_by_type(student, next_course.number_of_students)
            dbcon.commit()
        counter = counter + 1

        print("courses")
        courses_list = repo.courses.find_all_by_tuple()
        for course in courses_list:
            print(course)
        print("classrooms")
        classrooms_list = repo.classrooms.find_all_by_tuple()
        for classroom in classrooms_list:
            print(classroom)
        print("students")
        students_list = repo.students.find_all_by_tuple()
        for student in students_list:
            print(student)

        dbcon.commit()

else :
    print("courses")
    courses_list = repo.courses.find_all_by_tuple()
    for course in courses_list:
        print(course)
    print("classrooms")
    classrooms_list = repo.classrooms.find_all_by_tuple()
    for classroom in classrooms_list:
        print(classroom)
    print("students")
    students_list = repo.students.find_all_by_tuple()
    for student in students_list:
        print(student)

dbcon.close()