class Person():
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def getName(self):
    return f"{self.firstname} {self.lastname}"

class Student(Person):
  def __init__(self, firstname, lastname, subject):
    super().__init__(firstname, lastname)
    self.subject = subject

  def printNameSubject(self):
    return print(f"{self.getName()}, {self.subject}")
  
class Teacher(Person):
  def __init__(self, firstname, lastname, subject):
    super().__init__(firstname, lastname)
    self.subject = subject

  def printNameSubject(self):
    return print(f"{self.getName()}, {self.subject}") 
