class Student():
    number_of_Students=0
    def __init__(self,fname,lname,id,nationality,age):
        self.fname=fname
        self.lname=lname
        self.id=id
        self.nationality=nationality
        self.age=age
        Student.number_of_Students+=1
