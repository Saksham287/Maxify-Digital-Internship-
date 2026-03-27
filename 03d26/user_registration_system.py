# Build a simple User Registration System

users = ["amit", "rohit", "amit", "saksham", "rohit123", "test@", "admin"]

def is_valid_username(username):
    return len(username) >= 4 and username.isalnum()

def categorize_user(username):
    has_number = False
    for c in username:
        if c.isdigit():
            has_number = True
            break
    
    if has_number:
        return "Advanced User"
    else:
        return "Basic User"

valid_users = []
invalid_users = []
seen = set()
duplicates_removed = 0

for user in users:
    if not is_valid_username(user):
        invalid_users.append(user)
    elif user in seen:
        duplicates_removed += 1
    else:
        seen.add(user)
        valid_users.append(user)


with open("users.txt", "w") as file:
    file.write("Valid Users:\n")
    for user in valid_users:
        file.write(f"{user} - {categorize_user(user)}\n")

    file.write("\nInvalid Users:\n")
    for user in invalid_users:
        file.write(f"{user}\n")


print(f"Total Users: {len(users)}")                     # Output: Total Users: 7
print(f"Valid Users: {len(valid_users)}")               # Output: Valid Users: 5
print(f"Invalid Users: {len(invalid_users)}")           # Output: Invalid Users: 1
print(f"Duplicates Removed: {duplicates_removed}")      # Output: Duplicates Removed: 1


print("\nFile Output:")
with open("users.txt", "r") as file:
    print(file.read())
    
'''
Entire Output:

Total Users: 7
Valid Users: 5
Invalid Users: 1
Duplicates Removed: 1

File Output:
Valid Users:
amit - Basic User
rohit - Basic User
saksham - Basic User
rohit123 - Advanced User
admin - Basic User

Invalid Users:
test@
'''
