def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(len(lines))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1
count_lines("non_existent_file.txt")
count_lines("C:\\Users\\jayde\\CS2\\Python-learning\\Mock_Final_exam\\test.txt")