# Dictionary Method 

# Access

car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Year": 1964,
  "Colors": ["red", "white", "blue"]
}

x = car["Brand"]
print(x)
y = car.get("Model")
print(y)

z = car.keys()
print(z)
a = car.values()
print(a)
    
# Changes 

car["Year"] = 2022
car.update({"Year": 2025})
print(car)

# Adding 

car["Condition"] = "New"
if "Condition" in car:
    print("Yes, 'Condition' is one of the keys in the thisdict dictionary")
    
car.update({"Electric": False})
print(car)

# Removing

car.pop("Condition")
car.popitem()   # This will remove the last added item from the dictionary 
print(car)

car.clear()
print(car)

'''
Entire Output:

Ford
Mustang
dict_keys(['Brand', 'Model', 'Year', 'Colors'])
dict_values(['Ford', 'Mustang', 1964, ['red', 'white', 'blue']])
{'Brand': 'Ford', 'Model': 'Mustang', 'Year': 2025, 'Colors': ['red', 'white', 'blue']}
Yes, 'Condition' is one of the keys in the thisdict dictionary
{'Brand': 'Ford', 'Model': 'Mustang', 'Year': 2025, 'Colors': ['red', 'white', 'blue'], 'Condition': 'New', 'Electric': False}
{'Brand': 'Ford', 'Model': 'Mustang', 'Year': 2025, 'Colors': ['red', 'white', 'blue']}
{}

'''
