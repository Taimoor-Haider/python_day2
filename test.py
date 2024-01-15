"""name="Taimoor Haider"
def input_name():
    name=input("Enter the name:- ");

input_name()
print(name)


# Using global keywork
print("============Using 'global' keywork")

def change_name():
    global name
    name=input("Enter your name:- ")

change_name()
print(name)

"""
from itertools import chain
def find_element(my_list, target):
    for index, value in enumerate(my_list):
        print(f"Index is {index} and value is {value}")
        if value == target:
            return index
    return None  # Return None if the target element is not found in the list

my_list = [10, 20, 30, 40, 50]
target_element = 35

result = find_element(my_list, target_element)

if result is not None:
    print(f"The target element {target_element} is found at index {result}.")
else:
    print(f"The target element {target_element} is not present in the list.")



my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in enumerate(my_dict):
    print(key, value)



my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(key, value)



list=[1,2,3,4,5]
list2=[[6],[7],[8]]

list.extend(chain(*list2))
print(list)

for index in range(len(list)):
    list[index]=str(list[index])
    print(type(list[index]))


def unlimited_arguments(*args):
    #print(type(args))  type --> tuple
    for arguments in args:
        print(arguments)


unlimited_arguments(*[1,2,3,4])
print('{} {} {} {} {} {}'.format(*[1,2,3,4,5,6]))