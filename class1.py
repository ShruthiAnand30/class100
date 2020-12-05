class Student(object):
    def __init__(self,firstName,lastName,level,email,grades):
        self.firstName = firstName
        self.lastName = lastName
        self.level = level
        self.email = email
        self.grades = grades
    
    def getName(self):
        print(self.firstName+ ' '+ self.lastName)
    
stu1 = Student("abc","xyz",8,"abc.xyz@school.com","A")

stu1.getName()
