user_name = "Amani alhsasna" 
pass_word = "9112004" 
Num_data = [] 
 
def Admin_Dashboard(): 
    name = input("Enter the username: ") 
    password = input("Enter the password: ") 
    while name != user_name or password != pass_word: 
        print("Error!! Try again") 
        name = input("Enter the username: ") 
        password = input("Enter the password:") 
    print("You are successfully logged") 
    
    choice = " " 
    while choice != "6": 
        print("--- Admin Dashboard ---") 
        print("1. Add phone number") 
        print("2. Show all phone numbers") 
        print("3. Search for phone number") 
        print("4. Update phone number data") 
        print("5. Delete phone number") 
        print("6. Exit") 
        
        choice = input("Enter your choice: ") 
        
        if choice == "1": 
            add_phone() 
        elif choice == "2": 
            show_all() 
        elif choice == "3": 
            search_number() 
        elif choice == "4": 
            update_phone() 
        elif choice == "5": 
            delete_phone() 
        elif choice == "6": 
            print("Exiting Admin Dashboard...") 
        else: 
            print("Invalid choice, try again") 
 
def add_phone(): 
    phoneNum = input("Enter the phone number: ") 
    while len(phoneNum) != 10 or phoneNum[0:3] != "059": 
        print("The phone number must be 10 digits and start with 059") 
        phoneNum = input("Enter the phone number again: ") 
    
    name = input("Enter the name: ") 
    ID = input("Enter the ID: ") 
    while len(ID) != 9: 
        print("The ID must be exactly 9 digits") 
        ID = input("Enter the ID again: ") 
 
    age = input("Enter the age: ") 
    Address = input("Enter the address: ") 
    
    data = { 
        "number": phoneNum, 
        "name": name, 
        "ID": ID, 
        "age": age, 
        "Address": Address 
    } 
    
    result = False 
    for num in Num_data: 
        if num["number"] == phoneNum: 
            result = True 
            print("The number exists.") 
            break 
    
    if not result: 
        Num_data.append(data) 
        print("Number added successfully") 

def show_all(): 
    if len(Num_data) == 0: 
        print("There is no data") 
    else: 
        for item in Num_data: 
            print("Number:", item["number"]) 
            print("Name:", item["name"]) 
            print("ID:", item["ID"]) 
            print("Age:", item["age"]) 
            print("Address:", item["Address"]) 
            print("-----------------------") 

def search_number(): 
    Number = input("Enter your phone number: ") 
    found = False 
    for item in Num_data: 
        if Number == item["number"]: 
            print("Number:", item["number"]) 
            print("Name:", item["name"]) 
            print("ID:", item["ID"]) 
            print("Age:", item["age"]) 
            print("Address:", item["Address"]) 
            found = True 
            break 
    if not found: 
        print("The number does not exist") 

def update_phone(): 
    number = input("Enter your phone number: ") 
    found = False 
    for item in Num_data: 
        if number == item["number"]: 
            new_name = input("Enter the name: ") 
            new_ID = input("Enter the ID: ") 
            while len(new_ID) != 9: 
                print("The ID must be exactly 9 digits") 
                new_ID = input("Enter the ID again: ") 
 
            new_age = input("Enter the age: ") 
            new_Address = input("Enter the address: ") 
            item["name"] = new_name 
            item["ID"] = new_ID 
            item["age"] = new_age 
            item["Address"] = new_Address 
            print("The data has been successfully updated") 
            found = True 
            break 
    if not found: 
        print("The number does not exist") 

def delete_phone(): 
    number = input("Enter your phone number: ") 
    found = False 
    for item in Num_data: 
        if number == item["number"]: 
            Num_data.remove(item) 
            print("The data was successfully deleted") 
            found = True 
            break 
    if not found: 
        print("The number does not exist") 

print("***********************************") 
print("*") 
print("Welcome, the system is ready now") 
print("*") 
print("***********************************") 

while True: 
    print("1. Admin Dashboard") 
    print("2. Searching for details about phone number") 
    print("3. Exit") 
    choice1 = input("Enter your choice: ") 
    
    if choice1 == "1": 
        Admin_Dashboard() 
    elif choice1 == "2": 
        search_number() 
    elif choice1 == "3": 
        print("Exiting....") 
        break 
    else: 
        print("Invalid number, try again")
