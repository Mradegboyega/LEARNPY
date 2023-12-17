# A dictionary with string keys
user_details = {}
user_profile = {
    'name': "Michelle",
    'age': 2,
    'is_admin': False
}

# A dictionary with integer keys
fruits = {
    1: "Apple",
    2: "Oranges",
    3: "Banana"
}   

# Accessing dictionary elements by keys
print(user_profile["name"])
print(user_profile["age"])
print(user_profile["is_admin"])

# A dictionary is mutable, which means that its values can be changed
user_profile["name"] = "Adegboyega"
print(user_profile["name"])
print(user_profile)

# Adding elements to DICTIONARY
user_details["email"] = "username@domain.com"
user_details["username"] = "johndoedoe"
user_details["is_director"] = False
print(user_details)

