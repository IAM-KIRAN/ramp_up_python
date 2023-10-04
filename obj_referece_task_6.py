user_profile = {
    'username': 'kiran',
    'email': 'kiran@gmail.com',
    'age': 23
}

print("Before Update:")
print(user_profile)

def update_profile(user_profile, new_username, new_email, new_age):
    user_profile['username'] = new_username
    user_profile['email'] = new_email
    user_profile['age'] = new_age

new_username = input("Enter new username: ")
new_email = input("Enter new email: ")
new_age = int(input("Enter new age: "))

update_profile(user_profile, new_username, new_email, new_age)

print("\nAfter Update:")
print(user_profile)

