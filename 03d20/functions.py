# Functions 

def my_function():
    print("Hello, through my first function")

my_function()                       # Hello, through my first function


def get_greetings():
    return "Hello! How are you?"

message = get_greetings()
print(message)                      # Hello! How are you?


def its_empty():
    pass


def my_name(fname):                  # Arguments can be passed within the parentheses to identify it
    print(fname + " Python")

my_name("John")
my_name("Shaq")
my_name("Java")
'''
Output:

John Python
Shaq Python
Java Python
'''

# Parameters vs Arguments
def get_hello(name):            # name is a parameter 
    print("hello!", name)
    
get_hello("John")               # John is an argument 
get_hello("Ben")
get_hello("Sam")
'''
Output:

hello! John
hello! Ben
hello! Sam
'''

# Number of Arguments
def full_name(frname, lname):           # If function except 2 arguments then 2 arguments should be provided 
    print("Hello!", frname, lname)      # Otherwise the method call is incomplete
    
full_name("Ben", "Cook")
full_name("Louis", "Litt")
full_name("Mike", "Ross")
'''
Output:

Hello! Ben Cook
Hello! Louis Litt
Hello! Mike Ross
'''

# Default Parameter Values
def game_players(player = "Bot"):               # This means that if the argument is missing, the default value will be used
    print("Welcome to the game!!", player)
    
game_players("Sam")
game_players("John")
game_players("Ninja")
game_players()                      # Since there is no value for the function called, it will print the default value "Bot"
'''
Output:

Welcome to the game!! Sam
Welcome to the game!! John
Welcome to the game!! Ninja
Welcome to the game!! Bot
'''


# Keyword Arguments
def my_animal(animal, petName):
    print("I have a", animal)
    print("My", animal + "'s name is", petName)
    
my_animal(animal= "dog", petName= "John")          # When using the keywords we don't need to worry about the order of the input
my_animal(petName= "ben", animal= "Cat")           # It will be correlated to argument specified for.
'''
Output:

I have a dog
My dog's name is John
I have a Cat
My Cat's name is ben
'''

# Positional Arguments
my_animal("Fish", "Fisher")             # Same method just using the the positional arguments in order
my_animal("Hamster", "Jerry")
'''
Output:

I have a Fish
My Fish's name is Fisher
I have a Hamster
My Hamster's name is Jerry
'''

# Mixing Positional and Keyword Arguments
my_animal("Rabbit", petName= "Tom")         # Can also be mixed with positional and keyword
'''
Output:

I have a Rabbit
My Rabbit's name is Tom
'''
