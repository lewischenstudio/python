"""
Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not
value. That is, if the kth node of the first linked list is the exact same node
(by referece) as the jth node of the second linked list, then they are intersecting.

Time complexity: O(n)
Space complexity: O(1)
"""

from linked_list import LinkedList, Node

# my way
def my_intersection(llA, llB):
    n1 = llA.head
    n2 = llB.head
    m = len(llA)
    if len(llA) > len(llB):
        for i in range(len(llA) - len(llB)):
            n1 = n1.next
        m = len(llB)
    elif len(llA) < len(llB):
        for i in range(len(llB) - len(llA)):
            n2 = n2.next
    for j in range(m):
        if n1.value == n2.value:
            if n1.next and n2.next:
                if n1.next.value == n2.next.value:
                    return f'The two lists intersect at node {n1.value}'
            else:
                return f'The two lists intersect at node {n1.value}'
        n1 = n1.next
        n2 = n2.next
    return 'The two linked lists do not intersect'

customLL1 = LinkedList()
customLL2 = LinkedList()
customLL1.add(3)
customLL1.add(1)
customLL1.add(5)
customLL1.add(9)
customLL1.add(7)
customLL1.add(3)
customLL1.add(1)

customLL2.add(2)
customLL2.add(4)
customLL2.add(6)
customLL2.add(7)
customLL2.add(2)
customLL2.add(1)

print('customLL1: ', customLL1)
print('customLL2: ', customLL2)

print('my_intersection: ', my_intersection(customLL1, customLL2))

customLL1.generate(6, 0, 10)
customLL1.add(8)
customLL1.add(3)
customLL2.generate(4, 0, 10)
customLL2.add(8)
customLL2.add(3)
print('customLL1: ', customLL1)
print('customLL2: ', customLL2)
print('my_intersection: ', my_intersection(customLL1, customLL2))


# his way
def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longer_node = longer.head
    shorter_node = shorter.head

    for i in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next
    
    return longer_node

# Helper addition method
def addSameNode(llA, llB, value):
    temp_node = Node(value)
    llA.tail.next = temp_node
    llA.tail = temp_node
    llB.tail.next = temp_node
    llB.tail = temp_node

llA = LinkedList()
llA.generate(3, 0, 10)
llB = LinkedList()
llB.generate(4, 0, 10)

addSameNode(llA, llB, 11)

addSameNode(llA, llB, 14)

print(llA)
print(llB)
print(intersection(llA, llB))

