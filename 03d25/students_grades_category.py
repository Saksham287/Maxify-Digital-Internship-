# Count how many student fall in each category 

score = [45, 78, 90, 34, 67, 45, 90, 23]
print(score)

unique_score = set(score)
print(unique_score)

d = 0
p = 0
f = 0

def category(score):
    if score >= 75:
        return "Distinction"
    elif 50 <= score <= 74:
        return "Pass"
    else:
        return "Fail"
    
for x in score:
    result = category(x)
    if result == "Distinction":
        d += 1
    elif result == "Pass":
        p += 1
    else:
        f += 1
        
# print("Students Results")
# print(f"Distinction: {d} \nPass: {p} \nFail: {f}")

with open("Student_Results.txt", "wt") as file:
    file.write("Students Results\n")
    file.write(f"Distinction: {d} \nPass: {p} \nFail: {f}")
    
with open("Student_Results.txt", "r") as file:
    print(file.read())

'''
[45, 78, 90, 34, 67, 45, 90, 23]
{34, 67, 45, 78, 23, 90}
Students Results
Distinction: 2 
Pass: 1 
Fail: 3
'''
