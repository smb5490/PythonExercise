# Write a program that creates a tuple with 5 members and then adds new members in it.

tpl1 = (1,2,3,4,5)
print(tpl1)

# Adding element at the end of the tuple
tpl1 = tpl1 + (9,)
print(tpl1)

# Adding bunch of elements in between tuple
tpl1 = tpl1[:6] + (15, 20, 25) + tpl1[:6]
print(tpl1)
