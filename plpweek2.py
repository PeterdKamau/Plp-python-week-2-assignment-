# Initialize an empty list named my_list
my_list = []

# Add the specified numerical values to the end of my_list
my_list.extend([10, 20, 30, 40])
print("List after adding initial elements:", my_list)  # [10, 20, 30, 40]

# Place the number 15 between 10 and 20 in the sequence
my_list.insert(1, 15)  # Position 1 comes after index 0
print("List after inserting 15 at second position:", my_list)  # [10, 15, 20, 30, 40]

# Combine my_list with additional values [50, 60, 70]
additional_numbers = [50, 60, 70]
my_list = my_list + additional_numbers
print("List after concatenation with new elements:", my_list)  # [10, 15, 20, 30, 40, 50, 60, 70]

# Eliminate the final item from the collection
del my_list[-1]
print("List after deleting the last entry:", my_list)  # [10, 15, 20, 30, 40, 50, 60]

# Arrange all elements in increasing numerical sequence
my_list = sorted(my_list)
print("List in ascending order:", my_list)  # [10, 15, 20, 30, 40, 50, 60]

# Locate and display the position of value 30
position = my_list.index(30)
print("The numerical value 30 is located at index:", position)  # 3
