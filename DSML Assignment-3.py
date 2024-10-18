import random

# Creating a list of 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]
print("List of random numbers:", random_numbers)

# Inserting 3 new values
random_numbers.extend([101, 102, 103])
print("Updated list after insertion:", random_numbers)

print("Elements in the list:")
for number in random_numbers:
    print(number)

# Creating a dictionary
person_info = {
    'name': 'John',
    'age': 25,
    'address': 'New York'
}
print("Dictionary:", person_info)

# Adding a new key-value pair
person_info['phone'] = '1234567890'
print("Updated dictionary:", person_info)

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Adding a value to the set
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing a value from the set
my_set.remove(3)
print("Set after removing 3:", my_set)

# Creating a tuple
my_tuple = (1, 2, 3, 4)
print("Tuple:", my_tuple)

# Printing the length of the tuple
print("Length of the tuple:", len(my_tuple))





