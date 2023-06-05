"""
Question 1 - Remove Dups
Remove duplicate elements in a linked list

Time complexity: O(n^2)
Space complexity: O(1)
"""

from LinkedList import LinkedList


def remove_duplicates(linked_list):
    if linked_list.head is None:
        return None
    current_node = linked_list.head
    visited = set([current_node.value])
    while current_node.next:
        if current_node.next.value in visited:
            current_node.next = current_node.next.next
        else:
            visited.add(current_node.next.value)
            current_node = current_node.next
    return linked_list


def remove_duplicates_while(linked_list):
    if linked_list.head is None:
        return None
    current_node = linked_list.head
    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current_node = current_node.next
    return linked_list.head


customLL = LinkedList()
print("generate:")
customLL.generate(10, 0, 99)
print(customLL)
remove_duplicates(customLL)
print(customLL)

print("\nrepeated:")
customLL.repeated(10, 0, 99)
print(customLL)
remove_duplicates(customLL)
print(customLL)

print("\nwhile:")
customLL.repeated(10, 0, 99)
print(customLL)
remove_duplicates_while(customLL)
print(customLL)
