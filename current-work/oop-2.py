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
    pass