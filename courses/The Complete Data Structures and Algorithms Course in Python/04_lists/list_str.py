"""Lists and Strings"""


a = "spam spam spam"
b = a.split()
c = "spam-spam-spam"
delimiter = "-"
d = c.split(delimiter)
e = delimiter.join(d)
print(a)
print(b)
print(c)
print(d)
print(e)
