"""
Implement an algorithm to find the nth to last element
of a singly linked list

Time complexity: O(n)
Space complexity: O(1)
"""

from linked_list import LinkedList

def nthToLast(ll, n):
    pointer1 = ll.head  # pointer that follows
    pointer2 = ll.head  # pointer that leads

    # let the pointer move n step a head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    
    # both pointers move at the same time
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print('\nn = 2:')
print(nthToLast(customLL, 2))
print('\nn = 5:')
print(nthToLast(customLL, 5))

    
