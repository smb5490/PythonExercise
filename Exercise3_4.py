# Write a Program to create a set, then add a member in that set.
# After that convert that set into a frozen set and try to add any member of that frozen set.
# [To add a member in sets "set.add('argument')" the method is used]


set1 = {'orange', 'banana', 'grape'}
print("set: ", set1)

set1.add('pineapple')
print("After adding element in set: ", set1)

set2 = frozenset(set1)
print("frozenset: ", set2)

set2.add('cherries')        # adding elements in frozenset will returns Error
print("After adding element in frozenset: ", set2)
