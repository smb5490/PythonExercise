# Write a Python Program that uses the following built-in methods for Lists and Tuples
# Sum()
# Max()
# Min()
# Len()

list1 = []

num1 = int(input("Enter number of elements : "))

for i in range(0, num1):
    element1 = int(input())

    list1.append(element1)


print("List", list1)

Sum = sum(list1)
Max = max(list1)
Min = min(list1)
Len = len(list1)

print("Sum of List: ", Sum, "\n" "Max num in List: ", Max, "\n" "Min num in List: ", Min, "\n" "Length of List:", Len, "\n")

tuple1 = tuple(list1)
print("Tuple: ", tuple1)

t_Sum = sum(tuple1)
t_Max = max(tuple1)
t_Min = min(tuple1)
t_Len = len(tuple1)

print("Sum of Tuple: ", t_Sum, "\n" "Max num in Tuple: ", t_Max, "\n" "Min num in Tuple: ", t_Min, "\n" "Length of Tuple:", t_Len)
