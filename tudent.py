bimport sqlite3
# import pandas as pd
from studentdetails import Student
connection = sqlite3.connect("students.db")
studentdetails = connection.cursor()

# studentdetails.execute('''CREATE TABLE details(
#         first_name text,
#         last_name text,
#         id integer,
#         nationality text,
#         age integer
        
# )''')

choice=input("Type in keyword 'view' or 'other' to interact with database: ")
if choice=='view':
    choice2=input("Enter 'name' to only view name or 'details' to only view details: ")
    if choice2=="name":
        name=input("Enter first name to check whether student exists in Database: ")
        def get_details(name):
            studentdetails.execute("SELECT * FROM details WHERE first_name=:first_name",{'first_name':name})
            print(studentdetails.fetchall())
        get_details(name=name)

    elif choice2=="details":
        def get_all():
            studentdetails.execute("SELECT * FROM details ")
            print( studentdetails.fetchall())
        get_all()
        
    
elif choice=='other':
    option=input("Type in 'add' to add entry, 'update' to update/change entry and 'del' to delete entry: ")
    if option=="add":
        fname=input("First Name: ")
        lname=input("Last Name: ")
        id=int(input("ID: "))
        nationality=input("Nationality: ")
        age=int(input("age: "))
        def insert_details():
            with connection:
                studentdetails.execute("INSERT INTO details VALUES (?,?,?,?,?)",(fname,lname,id,nationality,age))
                print("Database Has been successfully updated")
        insert_details()
       

    elif option=="update":
        name=input("Enter name:")
        age=input("New age: ")
        def update_detail(name,upddetail):
            with connection:
                studentdetails.execute("UPDATE details SET age=:age WHERE first_name=:first_name",{'first_name':name,'age':upddetail})
                print("Database updated")
        update_detail(name=name,upddetail=age)

    elif option=="del":
        name=input("Enter name:")
        def delete(name):
            with connection:
                studentdetails.execute("DELETE from details WHERE first_name=:first_name ", {'first_name':name})
                print("Database updated")
        delete(name=name)
        
    
    else:
        print("Enter Valid input")



student1=Student("Shadya","Obuya",37098890,"Kenyan",22)
student2=Student("Mercy","Ssozi",5679877,"Ugandan",21)
student3=Student("Marie","Chantal",789765,"Rwandan",20)



connection.close()