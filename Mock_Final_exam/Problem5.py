#Use map, filter, and lambda functions to process student grades.
def process_grades(students):
    # Step 1: Calculate average for each student using map
    students_with_avg = list(map(lambda student: {**student, 'average': sum(student['grades']) / len(student['grades'])}, students))
    
    # Step 2: Filter out students with average < 60
    filtered_students = list(filter(lambda student: student['average'] >= 60, students_with_avg))
    
    # Step 3: Add letter grades using map
    def add_letter_grade(student):
        avg = student['average']
        if avg >= 90:
            student['letter'] = 'A'
        elif avg >= 80:
            student['letter'] = 'B'
        elif avg >= 70:
            student['letter'] = 'C'
        else:
            student['letter'] = 'D'
        return student
    
    students_with_grades = list(map(add_letter_grade, filtered_students))
    
    # Step 4: Sort by average (highest first)
    result = sorted(students_with_grades, key=lambda student: student['average'], reverse=True)
    return result


# Example data to test the function
if __name__ == "__main__":
    students = [
        {'name': 'Alice', 'grades': [90, 85, 95]},
        {'name': 'Bob', 'grades': [50, 45, 55]},
        {'name': 'Charlie', 'grades': [70, 75, 72]},
        {'name': 'Diana', 'grades': [88, 92, 85]},
    ]
    
    result = process_grades(students)
    
    print("Processed Student Grades:")
    print("-" * 60)
    for student in result:
        print(f"{student['name']} Average: {student['average']}  Grade: {student['letter']}")
    print("-" * 60)