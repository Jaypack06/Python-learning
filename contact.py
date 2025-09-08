from datetime import datetime as time

contactdatabase = {
}
flag = True
counter = 1


def menu():
    while flag:
        print("1: Create contact \n 2: Show Contacts \n 3: Search for Contact \n 4: Update contacts \n 5: delete contact \n 6: Generate statistics \n 7: search for duplactated contact \n 8: exit.")
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

def mergeContact(dic):
    showcontact(contactdatabase)
    while True:
        mergenum1 = input("First ID numbers do you want to Merge? \n -->")
        if not mergenum1.isdigit():
            print('Enter the ID number please.')
            continue
        if mergenum1 == '':
            print('Enter the ID number please.')
            continue
        if not mergenum2.isdigit():
            print('Enter the ID number please.')
            continue
        if mergenum2 == '':
            print('Enter the ID number please.')
            continue
        mergenum2 = input("what's the second ID number you want to merge? \n -->")
    
def genstat(dic):
    print(f'there are {len(dic)} contacts') 
    print("contacts that are in catagories are")

    for i in range(len(dic)):
        num = i +1
    if  dic[num]['category']:     
        print(q)
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

def dupcontact(dic):
    print("couldn't make it happen")
    
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
        dupcontact(contactdatabase)
    elif action == '8':
        exit()
   
    if action == '1':
        counter += 1
    
