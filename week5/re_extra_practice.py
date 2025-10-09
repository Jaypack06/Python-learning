import re
'''
email = input()

pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
if(re.search(pattern, email)):
    print("valid email")
else:
    print("invalid email")
'''

pattern = r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
newpat = r"\1\2\3"
user_input = input("type: ")
new_user_input = re.sub(pattern, newpat, user_input)
print(new_user_input)