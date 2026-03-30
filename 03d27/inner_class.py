# Inner Classes 

class Outer: 
    def __init__(self):
        self.name = "Outer Class"
    
    class Inner: 
        def __init__(self):
            self.name = "Inner Class"
            
        def display(self):
            print("This is Inner Class")


outer = Outer()
print(outer.name)           # This is accessing only Outer class
# Output: Outer Class

inner = Outer.Inner()
inner.display()             # This is accessing inner class
# Output: This is Inner Class

class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:
        def process(self):
            print("Processing data...")

    class RAM:
        def store(self):
            print("Storing data...")

computer = Computer()   
computer.cpu.process()      # Output: Processing data...
computer.ram.store()        # Output: Storing data...
