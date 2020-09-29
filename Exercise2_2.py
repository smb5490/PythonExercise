# 2. Write the program that uses variables and strings with the following methods:
# find
# lower
# upper
# strip
# replace
# join
# split

str1 = 'This is first string'
str2 = 'STRING IN LOWER CASE'
str3 = 'string in upper case'
str4 = '   This is second string   '
str5 = 'test with java...java for test...test without java...java without test'
list1 = ['P','y','t','h','o','n',' ','i','s',' ','b','e','s','t']

print("-----Program to use Find() method in string-----")
print(str1.find('is'))
print(str1.find('first',7,13))

print("-----Program to use lower() method in string-----")
print(str2.lower())

print("-----Program to use Upper() method in string-----")
print(str3.upper())

print("-----Program to use Strip() method in string-----")
print(str4.strip())
print(str4.strip(' string'))

print("-----Program to use Strip() method in string-----")
print(str5.replace("java", "python"))
print(str5.replace("java", "python", 2))

print("-----Program to use Join() method in string-----")
str6 = ''
print(str6.join(list1))

print("-----Program to use Split() method in string-----")
print(str1.split())