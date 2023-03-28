# List and List Indexing

fav_fruits = ["Apple","Mango","Banana","Grapes","Orange"]
print(type(fav_fruits))

print(f"List of my favourite Fruits: {fav_fruits}")

print(f"My all time favourite fruit is {fav_fruits[1]}")


print("\n")


# Tuple and Tuple Indexing

my_marks = (75,89,88,93,85,90)
print(type(my_marks))

print(f"Marks of Roll no. 98: {my_marks}")

print(f"Marks of Roll no. 98 in English sunject: {my_marks[-3]} marks")


print("\n")


# Dictionary and Dictionary Indexing

Employee_data = { "Name": "Ronak",
            "Age" : "25",
            "Company": "CloudEQ",
            "Address" : "Jammu and Kashmir" } 

print(type(Employee_data))

print(f"The name of the trainee is: {Employee_data['Name']}")
print(f"The age of the trainee \"{Employee_data['Name']}\" is: {Employee_data['Age']} years")


print("\n")


# Set 

set_of_cars = {"BMW","Audi","KIA","TATA"}
print(type(set_of_cars))

print(f"List of my favourite cars: {set_of_cars}")

# Sets cannot be Indexed beacuse it is not supported by Python
