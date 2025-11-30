contacts={}
#adding contacts in dictionary
def add_contacts():
    name=input("enter name:")
    phone=input("enter phone number:")
    contacts[name]=phone
    print("added contacts succesfully.")
def view_contacts():
    if not contacts:
        print("no contacts available")
    else:
        print("\n=== contacts===")
        for name , phone in contacts.items():


            print(f"{name} : {phone}")
def search_contacts():
    name=input("enter name:")
    if name in contacts:
        print(f"fund -> {name}:{contacts[name]}")
    else:
         print("contact not found.")
def delete_contacts():
    name=input("enter name to delete.")
    if name in contacts:
        del contacts[name]
        print("contact deleted")
    else:
        print("contact not found!")
while True:
    print("\n=== PHONE CONTACT MANAGEMENT ===")
    print("1.add Contacts.")
    print("2.view contacts.")
    print("3.search contacts.")
    print("4.delete Contacts.")
    print("5.exit.")

    choice=input("enter your choice:")

    if choice=='1':
        add_contacts()
    elif choice=='2':
        view_contacts()
    elif choice=='3':
        search_contacts()
    elif choice=='4':
        delete_contacts()
    elif choice=='5':
        print("thsnk you existing contacts.goodbye!")
        break
    else:
        print("invalid input.please try again!")
    
        


