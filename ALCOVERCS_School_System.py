from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        print(f"Age: {self.__age}")

    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self):
        print(f"{self.name} is studying.")

    def role(self):
        print(f"{self.name} is a student.")

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def teach(self):
        print(f"{self.name} is teaching.")

    def role(self):
        print(f"{self.name} is a teacher.")

class Principal(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def manage_school(self):
        print(f"{self.name} is managing the school.")

    def role(self):
        print(f"{self.name} is the principal.")

class GuidanceCounselor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def assist_students(self):
        print(f"{self.name} is assisting the students.")

    def role(self):
        print(f"{self.name} is a guidance counselor.")


teacher1 = Teacher("Givenchy", 89)
student1 = Student("Carra", 23)
principal1 = Principal("Mr. Dubois", 87)
guidCouns1 = GuidanceCounselor("Mr. Chantellerie", 55)

print(f"Name: {teacher1.name}")
teacher1.get_age()
teacher1.teach()
teacher1.role()

print()

print(f"Name: {student1.name}")
student1.get_age()
student1.study()
student1.role()

print()

print(f"Name: {principal1.name}")
principal1.get_age()
principal1.manage_school()
principal1.role()

print()

print(f"Name: {guidCouns1.name}")
guidCouns1.get_age()
guidCouns1.assist_students()
guidCouns1.role()

print()

people = [teacher1, student1, principal1]

for x in people:
    x.role()

#Exercise 2:
#Why is it better to access __age through get_age()?
# It is better to access the private age value through get_age() as it ensures that the age is not accidentally changed, as well as being simple to use to access the age.

#Reflection Questions:
#How does encapsulation protect information in the Person class?
#Encapsulation protects information in the Person class as it makes them inaccessible unless accessed through specific getter and setter methods, making accidental changes hard and protecting the info in the class.
#How does Student inherit features from Person?
#Student inherits features from Person as it has the attributes name and age as well as the methods get_age and the abstract method role.
#Why can role() produce different results for different objects?
#Role() can produce different results for different objects as those objects are in different classes which have the role method but has a different output to each other.
#Why is Person made an abstract class?
#Person is made an abstract class in order to force the child classes to have the methods that the Person class has, which makes it easy to spot errors as to what is missing within the child classes.
#How do the four pillars work together in this program?
#Encapsulation works in the program by protecting the information that the parent class holds.
#Inheritance works in the program as child classes inherit attributes and methods from the parent class.
#Abstraction works in the program as the the parent class is abstracted, which forces child classes to have the methods of the parent class.
#Polymorphism works in the program as the same method could have different outputs in different classes such as the role() method.
