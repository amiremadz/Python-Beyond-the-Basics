#!/usr/bin/python

from assignments import MaxSizeList

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
print a.get_length()

a.push("hi")
print a.get_length()

a.push("let's")
print a.get_length()

a.push("go")
print a.get_length()


b.push("hey")
print b.get_length()

b.push("hi")
print b.get_length()

b.push("let's")
print b.get_length()

b.push("go")
print b.get_length()



print a.get_list()
print b.get_list()