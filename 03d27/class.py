# Class

class MyClass:
    x = 5
    
a1 = MyClass()
a2 = MyClass()
a3 = MyClass()
print(a1.x)         # Output: 5
print(a2.x)         # Output: 5
print(a3.x)         # Output: 5

# The __init__() Method
class Person: 
    def __init__(self, name, age = 18):             # By adding age = 18, we set the default value to 18.
                                                    # You can also add multiple parameters
        self.name = name 
        self.age = age

p1 = Person("John", 24)
print(p1.name, p1.age)          # Output: John 24
p2 = Person("Ben")  
print(p2.name, p2.age)          # Output: Ben 18

p2.age = 26                     # This modifying the age properties
print(p2.name, p2.age)          # Output: Ben 26

#p1.city = "New York"            # This adding new properties
#print(p1.city)                  # Output: New York

# Accessing Properties with self
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
        
car1 = Car("Toyota", "Corolla", 2022)   
car1.display_info()                     # Output: 2022 Toyota Corolla


# Calling Methods with self
class PersonAgain:
    def __init__(self, names = "Name"):
        self.names = names

    def greet(self):
        return f"Hello, {self.names}"

    def welcome(self):
        message = self.greet()              # calling other methods within the class using "self"
        print(f"{message}! Welcome to our website.")

p3 = PersonAgain("Sam")
p3.welcome()            # Outout: Hello, Sam! Welcome to our website.