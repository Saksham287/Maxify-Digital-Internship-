# Nested Dictionaries

Car4 = {
        "Make" : "BMW",
        "Year" : 2023
    } 
Car5 = {
        "Make" : "Lamborghini",
        "Year" : 2019
    }
my_Garage = {
    "Car1" : {
        "Make" : "Honda",
        "Year" : 2026
    },
    "Car2" : {
        "Make" : "Toyota",
        "Year" : 2025
    },
    "Car3" : {
        "Make" : "Acura",
        "Year" : 2025
    },
    "Car4" : Car4,
    "Car5" : Car5
}
print(my_Garage)
print(my_Garage["Car5"]["Make"])
print()
'''
Output:

{'Car1': {'Make': 'Honda', 'Year': 2026}, 'Car2': {'Make': 'Toyota', 'Year': 2025}, 'Car3': {'Make': 'Acura', 'Year': 2025}, 'Car4': {'Make': 'BMW', 'Year': 2023}, 'Car5': {'Make': 'Lamborghini', 'Year': 2019}}
Lamborghini
'''


for key, value in my_Garage.items():
    print(key)
    for x in value:
        print(x + ':', value[x])
        
'''
Output:

Car1
Make: Honda
Year: 2026
Car2
Make: Toyota
Year: 2025
Car3
Make: Acura
Year: 2025
Car4
Make: BMW
Year: 2023
Car5
Make: Lamborghini
Year: 2019
'''
