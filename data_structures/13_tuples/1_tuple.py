# Tuple

# Createa a tuple
new_tuple = ('a', 'b', 'c', 'd', 'e')
new_tuple = ('a',)
new_tuple = tuple('abcde')

print(new_tuple)

# Search for an element in tuple
new_tuple = ('a', 'b', 'c', 'd', 'e')

print('b' in new_tuple)
print('f' in new_tuple)

def searchTuple(p_tuple, element):
    for i in p_tuple:
        if i == element:
            return p_tuple.index(i)
    return 'The element does not exist.'

print(searchTuple(new_tuple, 'c'))


# Tuple Operations / Functions

my_tuple = (1,4,3,2,5)
my_tuple = (1,2,6,9,8,7)

print(my_tuple)
print(min(my_tuple))
print(tuple([1,2,3,4]))