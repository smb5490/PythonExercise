# 4. Write the program that prints the string by converting the first character to "Uppercase" and the rest of the string in the lowercase.
# For Example, "apple" should be converted to "Apple"
# The testing Strings:
# apple
# Apple
# aPple
# APPLE

str1 = "APPLE"

#str2 = str1.capitalize()

str2 = str1[0:1].upper() + str1[1:].lower()
print(str2)