# Dictionary Loops 

car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Year": 1964,
  "Colors": ["red", "white", "blue"]
}

for a in car:
    # print(a)
    # print(car[a])
    print(a, ":", car[a])

for x in car.keys():
    print(x)

for y in car.values():
    print(y)

for x, y in car.items():
    print(f"{x} : {y}")