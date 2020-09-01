class Students:

    num_of_students = 0

    def __init__(self,fname,lname,email):
        self.fname = fname # firstname
        self.lname = lname # lastname
        self.email = email # email

        Students.num_of_students += 1 # Increment # of students by 1 every initialization
    def print_fullname(self):
        print(self.fname + ' ' + self.lname)
    
class Teachers(Students):
    pass

stu1 = Students('Christian','Saunders','christiansemail@email.com') # object of Students class
stu2 = Students('Chris','Saun','chrisemail@email.com') # object of Students class
# print(stu1.lname,stu1.email,stu1.fname) # Print lname, email, fname stu1
# print(stu2.fname) # print fname stu2

stu1.print_fullname() # print fullname of stu1
stu2.print_fullname() # print fullname of stu2
Students.print_fullname(stu1) # Print fullname of stu1

print(Students.num_of_students) # Print # of Student objects

# Access Students class via Teachers class
stu3 = Teachers('teach', 'lname', 'teach1@email.net') # teacher 1
Teachers.print_fullname(stu3) # print stu3 (aka teacher 1)
math = Teachers('Emma','Johnson','email@email.email') # teacher 2
print(math.fname) # fullname