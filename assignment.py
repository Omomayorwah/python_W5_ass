# Assignment 1
class Stundents:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, student_id={self.student_id})"

class graduate(Stundents):
    def __init__(self, name, age, student_id, degree):
        super().__init__(name, age, student_id)
        self.degree = degree

    def __str__(self):
        return f"Graduate(name={self.name}, age={self.age}, student_id={self.student_id}, degree={self.degree})"
    
# Assignment 2
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def speak(self):
        return "Meow"

class Dog(Pet):
    def speak(self):
        return "bark"