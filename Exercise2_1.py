# 1. Write a program that uses variables and the numbers with the following methods:
# ceil
# floor
# log
# sqrt
# range

import math

num1 = 100
num2 = -65.10
num3 = -65.77
num4 = 14.24
num5 = 14.85

print("--------Program to use Floor() method--------")

print("Floor value of ",num1, "is :", math.floor(num1))
print("Floor value of ",num2, "is :", math.floor(num2))
print("Floor value of ",num3, "is :", math.floor(num3))
print("Floor value of ",num4, "is :", math.floor(num4))
print("Floor value of ",num5, "is :", math.floor(num5))

print("--------Program to use Ceil() method--------")

print("Ceil value of ",num1, "is :", math.ceil(num1))
print("Ceil value of ",num2, "is :", math.ceil(num2))
print("Ceil value of ",num3, "is :", math.ceil(num3))
print("Ceil value of ",num4, "is :", math.ceil(num4))
print("Ceil value of ",num5, "is :", math.ceil(num5))

print("--------Program to use Log() method--------")

print("Logarithem of ",num1, "is :", math.log(num1))
print("Logarithem of ",num4, "is :", math.log(num4,3))
print("Logarithem of ",num5, "is :", math.log(num5,4.67))

print("--------Program to use Sqrt() method--------")

print("Square root of ", num1, "is :", math.sqrt(num1))
print("Square root of ", num4, "is :", math.sqrt(num4))
print("Square root of ", num5, "is :", math.sqrt(num5))

print("--------Program to use range() method--------")

for i in range(num1):
    print(i, end =" ")
print("\n")

for i in range(num1,150):
    print(i, end =" ")
print("\n")

for i in range(num1,200,10):
    print(i, end =" ")
