#clean and validate user input from a registration form

def clean_name(name):
    return name.strip().title()
def validate_email(email):
    if email.count("@") != 1:
        return False
    if email.split("@")[1].count(".") == 0:
        return False
    return True
def format_phone(phone):
    digits = ''.join(filter(str.isdigit, phone))
    if len(digits) != 10:
        return "Invalid"
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
def process_registration(data_string):
    parts = data_string.split(",")
    if len(parts) != 3:
        return None #invalid format
    name = clean_name(parts[0])
    email = parts[1].strip()
    phone = parts[2].strip()
    if not validate_email(email):
        return None
    formatted_phone = format_phone(phone)
    if formatted_phone == "Invalid":
        return None
    return {
        "name": name,
        "email": email,
        "phone": formatted_phone
    }
    
if __name__ == "__main__":
    print(clean_name("  john DOE  "))
    print(validate_email("john.doe@example.com"))
    print(validate_email("john.doeexample.com"))
    print(format_phone("123-456-7890"))
    print(format_phone("1234567"))
    
    test_data = "  jane smith  , jane@example.com,9871234567"
    print(process_registration(test_data))