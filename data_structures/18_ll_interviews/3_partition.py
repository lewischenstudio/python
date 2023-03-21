"""
Write code to partition a linked list around a value x, such that all
nodes less than x come before all nodes greater than or equal to x.

Time complexity: O(n)
Space complexity: O(1)
"""

from linked_list import LinkedList

def partition(ll, x):
    current_node = ll.head
    ll.tail = ll.head

    while current_node:
        next_node = current_node.next
        current_node.next = None
        # if next node is less than x, move it to the head
        if current_node.value < x:
            current_node.next = ll.head
            ll.head = current_node
        # else move it to the tail
        else:
            ll.tail.next = current_node
            ll.tail = current_node
        current_node = next_node
    
    if ll.tail.next is not None:
        ll.tail.next = None
    return ll


customLL = LinkedList()
customLL.generate(10, 0, 9)
print(customLL)
print(partition(customLL, 5))