"""Write a program which accepts a sequence of comma-separated numbers from the console (or user) and generate a list and a tuple
which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""
print("Enter value with comma: ")
num1 = input()
list1 = num1.split(",")
print("List : ", list1)

tuple1 = tuple(list1)
print("Tuple: ", tuple1)
