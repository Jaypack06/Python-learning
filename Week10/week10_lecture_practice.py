def practice_1_beginner():
	"""
	Beginner: Convert text to CSV
	"""
	print("\n" + "="*50)
	print("EXERCISE 1.1: Text to CSV Converter")
	print("="*50)
	# Create a text file with data
	with open("employees.txt", "w") as employees:
		employees.write("John Smith 35 Engineer\n")
		employees.write("Jane Doe 28 Designer\n")
		employees.write("Bob Johnson 42 Manager\n")
	# TODO 1: Read text file and convert to CSV
	with open("employees.txt", "r") as employees:
		with open("employees.csv", "w") as employees_csv:
			# Write CSV header
			employees_csv.write("First,Last,Age,Job\n")
			# TODO: Read each line and convert
			for line in employees:
				parts = line.strip().split()
				# parts[0] = first name, parts[1] = last name, etc.
				# TODO: Write as CSV line
				# Format: John,Smith,35,Engineer
				csv_line = f"{parts[0]},{parts[1]},{parts[2]},{parts[3]}"
				employees_csv.write(csv_line + "\n")
	# TODO 2: Read and verify CSV
	print("\nCSV Contents:")
	with open("employees.csv", "r") as employees_csv:
		# TODO: Read and display
		for line in employees_csv:
			print(line.strip())
# Run the exercise
#practice_1_beginner()

def practice_1_intermediate():

    #Intermediate: Process CSV data

    print("\n" + "="*50)
    print("EXERCISE 1.2: Grade Calculator")
    print("="*50)
    # Create grades CSV
    with open("grades.csv", "w") as grades:
        grades.write("Student,Math,Science,English\n")
        grades.write("Alice,95,87,92\n")
        grades.write("Bob,78,85,88\n")
        grades.write("Charlie,92,94,85\n")
        grades.write("Diana,88,91,95\n")
    # TODO 1: Read CSV and calculate averages
    with open("grades.csv", "r") as grades:
        header = grades.readline().strip().split(",")
        print(f"Subjects: {header[1:]}")
        student_averages = []
        for line in grades:
            parts = line.strip().split(",")
            name = parts[0]
            # TODO: Convert grades to numbers
            grades = [int(grade) for grade in parts[1:]]
            # TODO: Calculate average
            average = sum(grades) / len(grades) if grades else 0
            student_averages.append((name, average))
            print(f"{name}: {average:.1f}")
    # TODO 2: Save results to new CSV
    with open("averages.csv", "w") as averages:
        averages.write("Student,Average\n")
        # TODO: Write each student's average
        for name, avg in student_averages:
            averages.write(f"{name},{avg:.1f}\n")
    # Run the exercise
#practice_1_intermediate()


def practice_2_beginner():
    print("\n" + "="*50)
    print("EXERCISE 2.1: JSON Contact Card")
    print("="*50)
    import json
    # TODO 1: Create a contact dictionary
    contact = {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "555-1234",
    "age": 25
    }
    # TODO 2: Convert to JSON string
    json_str = json.dumps(contact) # Replace with json.dumps(contact)
    print(f"JSON String: {json_str}")
    # TODO 3: Save to file
    with open("contact.json", "w") as f:
        # TODO: Use json.dump to save contact
        json.dump(contact, f)
    print("Contact saved to file")
    # TODO 4: Load from file
    with open("contact.json", "r") as f:
        loaded_contact = json.load(f) # Replace with json.load(f)
    # TODO 5: Access data
    print(f"\nLoaded contact:")
    print(f"Name: {loaded_contact['name']}")
    print(f"Email: {loaded_contact['email']}")
# Run the exercise
practice_2_beginner()