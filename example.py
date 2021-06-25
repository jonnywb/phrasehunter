class Student():
    def __init__(self, name):
        self.name = name
    
    def change_name(self, new_name):
        self.name = new_name


class Course():
    def __init__(self, name):
        self.name = name
    
    def change_name(self, new_name):
        self.name = new_name


student = Student("Shavez")
course = Course("Python")

# change_name("JavaScript")  causes an error

course.change_name("JavaScript")  # No error and changes the course's name

print(course.name)
#output JavaScript