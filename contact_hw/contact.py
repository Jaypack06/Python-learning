from datetime import datetime as time
from collections import Counter
contactdatabase = {
}
flag = True
counter = 1


def menu():
    while flag:
        print("1: Create contact \n 2: Show Contacts \n 3: Search for Contact \n 4: Update contacts \n 5: delete contact \n 6: Generate statistics \n 7: merge contacts \n 8: find duplicate contacts \n 9: exit.")
        num = input('--> ')
        
        if not num.isdigit() :
            print("enter a number")
            continue
        if num =='':
            print("enter a number")
        
        choice= int(num)
        if choice == 1:
            return("1")
        elif choice == 2:
            return('2')
        elif choice == 3:
            return('3')
        elif choice == 4:
            return('4')
        elif choice == 5:
            return('5')
        elif choice == 6:
            return('6')
        elif choice == 7:
            return('7')
        elif choice == 8:
            return('8')
        elif choice == 9:
            return('9')

def updatecontact(dic):
    showcontact(contactdatabase)
    
    while True:
        updatenum = input("what ID number do you want to update?")
        if not updatenum.isdigit():
            print('Enter the ID number please.')
            continue
        if updatenum == '':
            print('Enter the ID number please.')
            continue
        else:
            num=int(updatenum)
            break
    while True:
        infoupdate = input('What would you like to update? \n 1. First name \n 2. Last name \n 3.Phone number \n 4. Email  \n 5. Address \n 6. Category \n 7. Notes \n 8. Done \n --> ')
        if not infoupdate.isdigit():
            print('Enter one of the numbers please.')
        if infoupdate == '':
            print('Enter one of the numbers please.')
        else:
            update = int(infoupdate)
            
        if update == 1:
            key = 'First name'
            dic[num][key] = input(f'Enter new {key}: ')
        elif update == 2:
            key = 'Last name'
            dic[num][key] = input(f'Enter new {key}: ')
        elif update == 3:
            key = 'phone number'
            dic[num][key] = input(f'Enter new {key}: ')
        elif update == 4:
            key = 'email'
            dic[num][key] = input(f'Enter new {key}: ')
        elif update == 6:
            key = 'category'
            dic[num][key] = input(f'Enter new {key}: ')
        elif update == 7:
            key = 'notes'
            dic[num][key] = input(f'Enter new {key}: ')
        elif update == 5:
            key = 'address'
            dic[num][key]['street']=(input("New street: "))
            dic[num][key]['city']=(input("New city: "))
            dic[num][key]['state']=(input("New state: "))
            dic[num][key]['zip code']=(input("New zip code: "))
        elif update == 8:
            break
    
    showcontact(dic)
    
    
def showcontact(dic):
    if not dic:
        print("No contacts yet.\n")
        return
    else:
        for cid, info in dic.items():
            print(f"ID: {cid}")
            for key, value in info.items():
                print(f"  {key.capitalize()}: {value}")
        
def delcontact(dic):
    showcontact(contactdatabase)
    
    while True:
        updatenum = input("what ID number do you want to delete?")
        if not updatenum.isdigit():
            print('Enter the ID number please.')
            continue
        if updatenum == '':
            print('Enter the ID number please.')
            continue
        else:
            num=int(updatenum)
            break
    dic[num].clear()
            


def searchContact(dic):
    while True:
        searchkey = input("What do you want to search by? \n 1.First Name, 2.Last Name 3.Category, or 4.Phone Number \n Type number here: ")
        if not searchkey.isdigit():
            print('Enter 1, 2, 3, or 4.')
            continue
        if searchkey =='':
            print('Enter 1, 2, 3, or 4.')
        search = int(searchkey)
        if search in [1,2,3,4]:
            if search == 1:
                check = input('Enter first name: ')
                key = 'First name'
                break
            elif search ==2:
                check = input('Enter last name: ')
                key = 'Last name'
                break
            elif search == 3:
                check = input('Enter category: ')
                key = 'category'
                break
            elif search == 4:
                check = input('Enter phone number: ')
                key = 'phone number'
                break
        else:
            print('Enter 1, 2, 3, or 4.')
    for i in range(1,counter):
        if check in dic[i][key]:
            print(dic[i])



def deep_merge_with_prompt(d1, d2):
    result = d1.copy()
    for key, val in d2.items():
        if key in result and isinstance(result[key], dict) and isinstance(val, dict):
            result[key] = deep_merge_with_prompt(result[key], val)
        else:
            if key in result and result[key] and val and result[key] != val:
                print(f"Conflict in '{key}':")
                print(f"  [1] {result[key]} (from first contact)")
                print(f"  [2] {val} (from second contact)")
                choice = input("Choose 1 or 2: ")
                result[key] = result[key] if choice == "1" else val
            else:
                result[key] = val if val else result.get(key, "")
    return result

def choose_contacts_to_merge(dic):
    if not dic:
        print("No contacts available.")
        return

    print("\nContacts available:")
    for cid, contact in dic.items():
        print(f"[{cid}] {contact.get('First name', '')} {contact.get('Last name', '')}")

    try:
        id1 = int(input("\nEnter the ID of the first contact to merge: "))
        id2 = int(input("Enter the ID of the second contact to merge: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    if id1 not in dic or id2 not in dic:
        print("One or both IDs do not exist.")
        return

    
    try:
        new_id = int(input("Enter the new ID for the merged contact: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    merged = deep_merge_with_prompt(dic[id1], dic[id2])
    
    dic[new_id] = merged

    print(f"\n Contacts {id1} and {id2} merged into new ID {new_id}\n")


    
def genstat(dic):
    total_contacts = len(dic)
    contacts_by_category = {}
    contacts_by_state = {}
    area_codes = []
    contacts_without_email = 0

    
    for contact in dic.values():
        
        category = contact.get('category', 'Uncategorized')
        contacts_by_category[category] = contacts_by_category.get(category, 0) + 1
        
        
        state = contact.get('address', {}).get('state', 'Unknown')
        contacts_by_state[state] = contacts_by_state.get(state, 0) + 1
        
        
        phone_number = contact.get('phone number', '')
        if phone_number:
            area_code = phone_number[:3] 
            area_codes.append(area_code)
        
        
        email = contact.get('email', None)
        if not email:
            contacts_without_email += 1
    
    
    total_categories = len(contacts_by_category)
    average_contacts_per_category = total_contacts / total_categories if total_categories else 0
    
    
    area_code_counts = Counter(area_codes)
    most_common_area_code = area_code_counts.most_common(1)[0][0] if area_codes else None
    
    
    stats = {
        'total_contacts': total_contacts,
        'contacts_by_category': contacts_by_category,
        'contacts_by_state': contacts_by_state,
        'average_contacts_per_category': average_contacts_per_category,
        'most_common_area_code': most_common_area_code,
        'contacts_without_email': contacts_without_email
    }

    print(stats) 
    
def contactmaker(dic):
    dic.update({counter:{}})
    dic[counter]['First name'] = input("First name: ")
    dic[counter]['Last name'] = input("Last name: ")
    dic[counter]['phone number'] = input("Phone number: ")
    dic[counter]['email'] = input("Email: ")
    dic[counter].update({'address':{}})
    dic[counter]['address']['street']=(input("street: "))
    dic[counter]['address']['city']=(input("city: "))
    dic[counter]['address']['state']=(input("state: "))
    dic[counter]['address']['zip code']=(input("zip code: "))
    dic[counter]['category'] = input("Category: ")
    dic[counter]['notes'] = input("Notes: ")
    dic[counter]['created date'] = time.now()
    dic[counter]['last updated'] = time.now()

def find_duplicates(dic):
    duplicates = []

    checked = set()
    keys = list(dic.keys())

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            id1, id2 = keys[i], keys[j]

            # Avoid re-checking pairs
            if (id1, id2) in checked or (id2, id1) in checked:
                continue

            c1, c2 = dic[id1], dic[id2]

            # Define duplicate rules
            same_name = (c1.get("First name", "").lower() == c2.get("First name", "").lower() and
                         c1.get("Last name", "").lower() == c2.get("Last name", "").lower())

            same_phone = (c1.get("phone number") and c1.get("phone number") == c2.get("phone number"))
            same_email = (c1.get("email") and c1.get("email") == c2.get("email"))

            if same_name or same_phone or same_email:
                duplicates.append((id1, id2))

            checked.add((id1, id2))

    print(duplicates)

    
while flag == True:
    
    action=menu()
    if action == '1':
        contactmaker(contactdatabase)
    elif action == '2':
        showcontact(contactdatabase)
    elif action == '3':
        searchContact(contactdatabase)
    elif action == '4':
        updatecontact(contactdatabase)
    elif action == '5':
        delcontact(contactdatabase)
    elif action == '6':
        genstat(contactdatabase)
    elif action == '7':
        choose_contacts_to_merge(contactdatabase)
    elif action == '8':
        find_duplicates(contactdatabase)
    elif action == '9':
        exit()
   
    if action == '1':
        counter += 1
        