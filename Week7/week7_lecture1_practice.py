def practice_1_beginner():
    """
    Beginner: Understanding why we need files
    """
    print("\n" + "="*50)
    print("EXERCISE 1.1: Save Your Name")
    print("="*50)

    # TODO 1: Get user's name
    name = input("Enter your name: ")

    # TODO 2: Open a file called "myname.txt" for writing
    # TODO 3: Write the name to the file
    with open("myname.txt", "w") as file:
        file.write(name)

    print(f"Name '{name}' saved to myname.txt!")

    # TODO 5: Read it back
    with open("myname.txt", "r") as file:
        saved_name = file.read()

    print(f"Read back: '{saved_name}'")


# Run the exercise
practice_1_beginner()
def practice_2_beginner():
    """
    Beginner: Work with file objects
    """
    print("\n" + "="*50)
    print("EXERCISE 2.1: File Object Basics")
    print("="*50)

    # TODO 1: Create a text file with 3 lines
    number_text = open("numbers.txt", "w")
    # Write three numbers, each on a new line
    number_text.write("10\n")
    # TODO: Write 20 and 30
    number_text.write("20\n")
    number_text.write("30\n")
    number_text.close()

    # TODO 2: Open the file and check its properties
    number_text = open("numbers.txt", "r")

    # Print file name
    print(f"File name: {number_text.name}")
    # TODO: Print file mode
    # Hint: Use file.mode
    print(f"File mode: {number_text.mode}")
    # TODO: Check if file is closed
    # Hint: Use file.closed
    print(f"File closed: {number_text.closed}")
    # TODO 3: Read one line at a time until EOF
    while True:
        line = number_text.readline()
        if line == "":  # Check for EOF
            print("Reached end!")
            break
        print(f"Read: {line.strip()}")

    number_text.close()


# Run the exercise
practice_2_beginner()
def practice_2_intermediate():
    """
    Intermediate: Track file position
    """
    print("\n" + "="*50)
    print("EXERCISE 2.2: File Position Tracking")
    print("="*50)

    # Create a file with alphabet
    alphabet_file = open("alphabet.txt", "w")
    alphabet_file.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphabet_file.close()

    # TODO 1: Open and read specific positions
    alphabet_file = open("alphabet.txt", "r")

    # Read first 5 characters
    chunk1 = alphabet_file.read(5)
    print(f"First 5: {chunk1}")

    # TODO 2: Check current position
    position = alphabet_file.tell()
    print(f"Current position: {position}")

    # TODO 3: Read next 5 characters
    chunk2 = alphabet_file.read(5)
    print(f"Next 5: {chunk2}")

    # TODO 4: Check position again
    # Your code here
    print(f"Checking posistion: {position}")

    # TODO 5: Read until EOF
    remaining = alphabet_file.read()
    print(f"Remaining: {remaining}")

    alphabet_file.close()


# Run the exercise
practice_2_intermediate()
