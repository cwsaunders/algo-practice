class Students:

    def __init__(self,fname,lname,email):
        self.fname = fname # firstname
        self.lname = lname # lastname
        self.email = email # email

    def print_fullname(self):
        print(self.fname + ' ' + self.lname)




class Teachers:

    def __init__(self,fname,lname,email):
        self.fname = fname # firstname
        self.lname = lname # lastname
        self.email = email # email

    def print_fullname(self):
        print(self.fname + ' ' + self.lname)



stu1 = Students('Christian','Saunders','christiansemail@email.com') # object of Students class
stu2 = Students('Chris','Saun','chrisemail@email.com') # object of Students class

math = Teachers('Emma','Johnson','email@email.email') # teacher



    