# A university needs to track student course enrollments. Each student can enroll in multiple courses, and each course can have multiple students enrolled. Implement a system that allows adding students to courses, removing students from courses, and retrieving a list of students enrolled in a specific course. Use sets to manage the enrollments efficiently.

def find_common_students(course1_students, course2_students):
    return course1_students.intersection(course2_students)

def find_all_students(course1_students, course2_students):
    return course1_students.union(course2_students)
def find_unique_to_course1(course1_students, course2_students):
    return course1_students.difference(course2_students)
def check_enrollment(student_name, *course_lists):
    return any(student_name in course for course in course_lists)
if __name__ == "__main__":
    cs_students = {"Alice", "Bob", "Charlie", "David"}
    math_students = {"Bob", "Charlie", "Eve", "Frank"}
    physics_students = {"George", "Hannah", "Alice"}
    print("Common Students:", find_common_students(cs_students, math_students, physics_students))
    print("All Students:", find_all_students(cs_students, math_students, physics_students))
    print("CS only:", find_unique_to_course1(cs_students, math_students))
    print("Is Alice enrolled?", check_enrollment("Alice", cs_students, math_students, physics_students))
    print("Is Henry enrolled?", check_enrollment("Henry", cs_students, math_students, physics_students))