from DB_1prog import *

def processing():
    db= DBhelper()
    while True:
        print("PRESS 1 to display all details.")
        print("PRESS 2 to insert details.")
        print("PRESS 3 to update any details.")
        print("PRESS 4 to delete the details.")
        print("PRESS 5 to exit program.")
        print()
        try:
            choice=int(input("Entert the number: "))
            if choice==1:
                #display
                db.fetch_all()
            elif choice==2:
                #insert
                id = int(input("Enter id: "))
                name = input("Enter the name: ")
                phone = input("Enter the phone no: ")
                db.insert_user(id, name, phone)
            elif choice==3:
                #update
                id = int(input("Enter id .up: "))
                name = input("Enter the name .up: ")
                phone = input("Enter the phone no .up: ")
                db.update(id, name, phone)
            elif choice==4:
                #delete
                userid=int(input("Enter user id: "))
                db.delete(userid)
            elif choice==5:
                break
            else:
                print("Invaild input, try again!")
        except Exception as e:
            print(e)
            print("Invaild details, try again!")

if __name__ == "__main__":
    processing()

