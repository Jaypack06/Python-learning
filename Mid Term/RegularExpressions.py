#use regular expressions to extract information from text
import re
def find_all_phones(text):
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(pattern, text)

def find_all_prices(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)
    
def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)
def validate_student(student_id):
    pattern = r'^[A-Za-z]{2}\d{4}$'
    return re.match(pattern, student_id) is not None

if __name__ == "__main__":
    test_text = """
    For info, call 555-123-4567 or (555) 987-6543.
Email us at info@school.edu or admin@college.com
Course fees: $50.00 for materials, $150.50 for tuition
"""
    print("Phones: ", find_all_phones(test_text))
    print("Prices: ", find_all_prices(test_text))
    print("Emails: ", extract_emails(test_text))
    print("Valid Student ID (CS1234): ", validate_student("CS1234"))
    print("Valid Student ID (12ABCD): ", validate_student("12ABCD"))
    print("Valid Student ID (AB12345): ", validate_student("AB12345"))