class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass  #Use the pass keyword when you do not want to add any other properties or methods to the class.

x = Person("Osman", "Koçak")
x.printname()

x = Student("Sarp Aka", "Koçak")
x.printname()
