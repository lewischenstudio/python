"""
Remove duplicate elements in a linked list

Time complexity: O(n^2)
Space complexity: O(1)
"""

from linked_list import LinkedList

def remove_duplicates(ll):
    if ll.head is None:
        return None
    current_node = ll.head
    visited = set([current_node.value])
    while current_node.next:
        if current_node.next.value in visited:
            current_node.next = current_node.next.next
        else:
            visited.add(current_node.next.value)
            current_node = current_node.next
    return ll

def remove_duplicates_while(ll):
    if ll.head is None:
        return None
    current_node = ll.head
    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current_node = current_node.next
    return ll.head


customLL = LinkedList()
print('generate:')
customLL.generate(10, 0, 99)
print(customLL)
remove_duplicates(customLL)
print(customLL)

print('\nrepeated:')
customLL.repeated(10, 0, 99)
print(customLL)
remove_duplicates(customLL)
print(customLL)

print('\nwhile:')
customLL.repeated(10, 0, 99)
print(customLL)
remove_duplicates_while(customLL)
print(customLL)


