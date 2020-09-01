# Inheritence file

class UniversityPeople:
    def __init__(self,fname,lname,email):
        self.fname = fname # firstname
        self.lname = lname # lastname
        self.email = email # email

    def print_fullname(self):
        print(self.fname + ' ' + self.lname)


class Students(UniversityPeople):
    pass

class Teachers(UniversityPeople):
    def __init__(self,fname,lname,email,salary):
        super().__init__(fname,lname,email) # Inheritence __init__ of UniversityPeople
        self.salary = salary

stu1 = Students('Christian','Saunders','christiansemail@email.com') # object of Students class
stu2 = Students('Chris','Saun','chrisemail@email.com') # object of Students class

math = Teachers('Emma','Johnson','email@email.email', 90000) # teacher


print(stu1.fname) # firstname
print(stu2.fname) # firstname
print(math.fname) # firstname
print(math.salary) # salary

print(isinstance(stu1,Students)) # is stu1 an instance of the class Students
print(isinstance(stu1, Teachers)) # is stu1 an instance of the class Students
print(isinstance(stu1,UniversityPeople)) # is stu1 an instance of the class UniversityPeople (it is a subclass)