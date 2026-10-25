#UML Relationships in Python Code


#Inheritance
class Room:
    def __init__(self, length = float, width = float, height = float):
        self.length = length
        self.width = width
        self.height = height

class Bedroom(Room):
    def area(self):
        area = (self.length * self.width)
        print(f"The area of the room is {area}m^2.")

my_bedroom = Bedroom(10, 10, 10)

my_bedroom.area()


#Composition
class Engine:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = Engine("V-200")

    def engine_type(self):
        engine_type = self.engine.name
        print(f"Engine type: {engine_type}")

my_car = Car("Suzuki", "Multi-cab")

my_car.engine_type()


#Aggregation
class Student:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self, name, students: list[Student] = None):
        self.name = name
        self.students = students if students else []
    
stud1 = Student("Mary")
stud2 = Student("Joy")

my_school = School("Werner High", [stud1, stud2])
print(f"Students in school: {[a.name for a in my_school.students]}")


#Association
class Lesson:
  def __init__(self, title):
    self.title = title
    
  def __repr__(self):
        return f"'{self.title}'"
  
class Scholar:
  def __init__(self, name):
    self.name = name
    self.lessons = []  

  def enroll(self, lesson: Lesson):
    self.lessons.append(lesson)

my_scholar = Scholar("Geerda")

lesson1 = Lesson("Math 10101")
lesson2 = Lesson("English 9901029301")

my_scholar.enroll(lesson1)
my_scholar.enroll(lesson2)

print(f"Student {my_scholar.name} has the lessons: {my_scholar.lessons}")


#Dependency
class Blackboard:
   def __init__(self, size):
      self.size = size

class Teacher:
  def __init__(self, name):
    self.name = name

  def teach(self, blackboard: Blackboard):
    print(f"Teacher {self.name} is teaching.")
    blackboard.present()


#Realization/Implementation
from abc import ABC, abstractmethod

class Presentable(ABC):
  @abstractmethod
  def present(self):
    pass

class Whiteboard(Presentable):  # Realizes/implements Presentable
  def __init__(self, color="White"):
    self.color = color

  def present(self):
    print(f"Displaying notes on the {self.color} whiteboard.")




