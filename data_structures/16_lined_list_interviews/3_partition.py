"""
Question 3 - Partition
Write code to partition a linked list around a value x, such that all
nodes less than x come before all nodes greater than or equal to x.

Time complexity: O(n)
Space complexity: O(1)
"""

from LinkedList import LinkedList


def partition(linked_list, x):
    current_node = linked_list.head
    linked_list.tail = linked_list.head

    while current_node:
        next_node = current_node.next
        current_node.next = None
        # if next node is less than x, move it to the head
        if current_node.value < x:
            current_node.next = linked_list.head
            linked_list.head = current_node
        # else move it to the tail
        else:
            linked_list.tail.next = current_node
            linked_list.tail = current_node
        current_node = next_node

    if linked_list.tail.next is not None:
        linked_list.tail.next = None
    return linked_list


customLL = LinkedList()
customLL.generate(10, 0, 9)
print(customLL)
print(partition(customLL, 5))
