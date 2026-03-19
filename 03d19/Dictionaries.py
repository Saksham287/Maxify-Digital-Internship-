# Dictionary Structures

thisdict = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Year": 1964,
  "colors": ["red", "white", "blue"],
  "electric": False
}
print(thisdict)     # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(thisdict["Brand"])    # Output: Ford
print(thisdict["Model"])    # Output: Mustang
print(thisdict["Year"])     # Output: 1964

for key, value in thisdict.items():
    print(f"{key} : {value}")
'''
Output: 
brand : Ford
model : Mustang
year : 1964
'''

print(len(thisdict)) # Output: 5