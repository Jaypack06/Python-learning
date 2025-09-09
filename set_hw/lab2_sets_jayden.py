import time
import random
import string
from collections import Counter

def create_enrollment_data():

    # Course enrollments - each key is a course, value is set of students
    enrollments = {
        'CS1350': {'Alice', 'Bob', 'Carol', 'David', 'Eve'},
        'MATH2010': {'Alice', 'Carol', 'Frank', 'Grace'},
        'PHYS1410': {'Bob', 'David', 'Frank', 'Henry'},
        'ENGL1010': {'Eve', 'Grace', 'Henry', 'Ivy'},
        'CHEM1010': {'Alice', 'Bob', 'Ivy', 'Jack'},
        'CS2040': {'Carol', 'David', 'Eve', 'Jack'}
    }
    # Student schedules - each key is a student, value is set of courses
    student_courses = {
    'Alice': {'CS1350', 'MATH2010', 'CHEM1010'},
    'Bob': {'CS1350', 'PHYS1410', 'CHEM1010'},
    'Carol': {'CS1350', 'MATH2010', 'CS2040'},
    'David': {'CS1350', 'PHYS1410', 'CS2040'},
    'Eve': {'CS1350', 'ENGL1010', 'CS2040'},
    'Frank': {'MATH2010', 'PHYS1410'},
    'Grace': {'MATH2010', 'ENGL1010'},
    'Henry': {'PHYS1410', 'ENGL1010'},
    'Ivy': {'ENGL1010', 'CHEM1010'},
    'Jack': {'CHEM1010', 'CS2040'}
    }
    return enrollments, student_courses
    # Load the data
course_enrollments, student_schedules = create_enrollment_data()

