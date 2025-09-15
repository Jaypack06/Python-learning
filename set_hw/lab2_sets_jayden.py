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

def find_common_student(course1, course2, enrollments):
    names1 = []
    if course1 in enrollments:
        for i in enrollments[course1]:
            names1.append(i)
    names2 = []
    if course2 in enrollments:
        for i in enrollments[course2]:
            names2.append(i)
    matchingname = []
    for names in names1:
        if names in names2:
            matchingname.append(names)
    print(matchingname)

def find_popular_combinations(student_schedules):
    pair_counter = Counter()
    for courses in student_schedules.values():
        # Convert to list to access by index
        course_list = list(courses)
        
        # Generate all pairs manually (since we can't use itertools.combinations)
        for i in range(len(course_list)):
            for j in range(i + 1, len(course_list)):
                # Create pair and sort to ensure consistent ordering
                pair = tuple(sorted([course_list[i], course_list[j]]))
                pair_counter[pair] += 1
    
    # Return pairs sorted by count (most common first)
    return pair_counter.most_common()

#find_common_student('CS1350', 'MATH2010', course_enrollments)


result = find_popular_combinations(student_schedules)
if result:
    most_popualr = result[0]
    print(f"Most popular combination: {most_popualr[0]} taken by {most_popualr[1]} students")