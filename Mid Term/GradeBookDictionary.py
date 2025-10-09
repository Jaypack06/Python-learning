#Grade Book dictionary

def add_grade(grade_book, name, grade):
    if not (0 <= grade <= 100):
        return False
    if name in grade_book:
        grade_book[name].append(grade)
    else:
        grade_book[name] = [grade]
    return True
def get_class_average(grade_book):
    total = 0
    count = 0
    for grades in grade_book.values():
        total += sum(grades)
        count += len(grades)
    return total / count if count > 0 else 0

def get_passing_students(grade_book, passing_grade=60):
    passing_students = []
    for name, grades in grade_book.items():
        if any(grade >= passing_grade for grade in grades):
            passing_students.append(name)
    return passing_students

if __name__ == "__main__":
    grade_book = {}
    print(add_grade(grade_book, "Alice", 85))
    print(add_grade(grade_book, "Bob", 150))
    print(add_grade(grade_book, "Charlie", 45))
    print(grade_book)
    print("Class Average:", get_class_average(grade_book))
    print("Passing Students:", get_passing_students(grade_book))