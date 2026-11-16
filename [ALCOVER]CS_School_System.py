from abc import ABC, abstractmethod

@abstractmethod
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        print(f"Age: {self.__age}")

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self):
        print(f"{self.name} is studying.")

    @abstractmethod
    def role(self):
        print(f"{self.name} is a student.")

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def teach(self):
        print(f"{self.name} is teaching.")

    @abstractmethod
    def role(self):
        print(f"{self.name} is a teacher.")

teacher1 = Teacher("Givenchy", 89)
student1 = Student("Carra", 23)

print(f"Name: {teacher1.name}")
teacher1.get_age()
teacher1.teach()
teacher1.role()

print(f"Name: {student1.name}")
student1.get_age()
student1.study()
student1.role()
# It is better to access the private age value through get_age() as it ensures that the age is not accidentally changed, as well as being simple to use to access the age.