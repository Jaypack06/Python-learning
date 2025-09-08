'''from datetime import datetime as time
contactdatabase = {
}
counter = 1

while True:
    contactdatabase.update({counter:{}}) 
    def contactmaker(dic):
        dic['First name'] = input("First name: ")
        dic['Last name'] = input("Last name: ")
        dic['phone number'] = input("Phone number: ")
        dic['email'] = input("Email: ")
        dic.update({'address':{}})
        dic['address']['street']=(input("street: "))
        dic['address']['city']=(input("city: "))
        dic['address']['state']=(input("state: "))
        dic['address']['zip code']=(input("zip code: "))
        dic['category'] = input("Category: ")
        dic['notes'] = input("Notes: ")
        dic['created date'] = time.now()
        dic['last updated'] = time.now()
    contactmaker(contactdatabase[counter])
    print(contactdatabase)
    '''
    
