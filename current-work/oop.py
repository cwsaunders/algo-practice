class Students:
    def __init__(self,fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email


stu1 = Students('Christian','Saunders','christiansemail@email.com') # object of Students class
stu2 = Students('Chris','Saun','chrisemail@email.com') # object of Students class
print(stu1.lname,stu1.email,stu1.fname) # Print lname, email, fname stu1
print(stu2.fname) # print fname stu2
