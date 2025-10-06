#Numpy practice
'''
import numpy as np
arr = np.array([2,4,6])
print(arr / 2)

arr2 = np.zeros((2, 3))
print(arr2)

arr3 = np.array([[10,20],
                 [30,40]])
print(arr.shape)
print(arr[1, 1])
'''
#string
'''
text = "Hello"
print(text[1:3])
print(text * 2)

msg = "     Python Programming      "
clean = msg.strip()
print(len(clean))
words = clean.split()
print(words[0])
print("-".join(words))
'''
#dictionary coding practice
'''
order = {}
counter = 1
def add_to_order(order, item_name, quantity, price_per_item):
    global counter
    order[f"item{counter}"] = {
        "name": item_name,
        "quantity": quantity,
        "price": price_per_item
    }
    counter += 1

def remove_from_order(order, item_name):
    for key in list(order.keys()):
        if order[key]["name"] == item_name:
            del order[key]
            break
def calculate_total(order, tax_rate):
    total = 0
    for item in order.values():
        total += item["quantity"] * item["price"]
    total += total * tax_rate
    return total

if __name__ == "__main__":
    add_to_order(order, "Apple", 2, 3.0)
    add_to_order(order, "Banana", 5, 1.0)
    print(order)
    remove_from_order(order, "Apple")
    print(order)
    total = calculate_total(order, 0.07)
    print(f"Total with tax: {total}")
'''

#regex practice
#processing email
import re
email = "jaydenPacker.267@gmail.com"
def extract_username(email):
    pattern = r'([^@]+)@[^@]+\.[^@]+'
    match = re.match(pattern, email)
    if match:
        return match.group(1)
    return None

def extract_domain(email):
    pattern = r'[^@]+@([^@]+\.[^@]+)'
    match = re.match(pattern, email)
    if match:
        return match.group(1)
    return None
def standardize_email(email, extract_username):
    #get rid of leading/trailing spaces and convert to lowercase
    email = email.strip().lower()
    #search for '.' and replace with '' in the username part
    username = extract_username(email)
    if username:
        email = email.replace(username, username.replace('.', ''))
    return email
def validate_email_list(email_string):
    #input: comma-separated email addresses
    emails = [email.strip() for email in email_string.split(',')]
    #validate each email has '@' and '.'
    valid_emails = []
    none_valid_emails = []
    pattern = r'^[^@]+@[^@]+\.[^@]+$'
    for email in emails:
        if re.match(pattern, email):
            valid_emails.append(email)
        else:
            none_valid_emails.append(email)
    return valid_emails, none_valid_emails
if __name__ == "__main__":
    username = extract_username(email)
    domain = extract_domain(email)
    standardized_email = standardize_email(email, extract_username)
    email_string = "   jaydenPacker.267@gmail.com, invalid-email, another.valid@email.com   "
    valid_emails, none_valid_emails = validate_email_list(email_string)
    print("Username:", username)
    print("Domain:", domain)
    print("Standardized email:", standardized_email)
    print("Valid emails:", valid_emails)
    print("Invalid emails:", none_valid_emails)
