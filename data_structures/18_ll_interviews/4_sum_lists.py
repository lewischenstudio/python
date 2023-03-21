"""
You have two numbers represented by a linked list, where each node contains
a single digit. The digits are stored in reverse order, such that the 1's
digit is at the head of the list. Write a function that adds the two numbers
and returns the sum as a linked list.
list 1 = 7 -> 1 -> 6 --> 617
list 2 = 5 -> 9 -> 2 --> 295
--> 617 + 295 = 912
--> SumList = 2 -> 1 -> 9

Time complexity: O(n)
Space complexity: O(1)
"""

from linked_list import LinkedList

def getNumber(ll):
    index = 1
    current_node = ll.head
    value = 0
    while current_node:
        value += current_node.value * index
        index = index * 10
        current_node = current_node.next
    return value

# my function 1
def sumList(list1, list2):
    value1 = getNumber(list1)
    value2 = getNumber(list2)
    value = value1 + value2
    print('value1: ', value1)
    print('value2: ', value2)
    print('sum: ', value)
    num_list = [int(x) for x in str(value)]
    num_list.reverse()
    sum_list = LinkedList()
    for i in num_list:
        sum_list.add(i)
    return sum_list

customLL1 = LinkedList()
customLL2 = LinkedList()
customLL1.generate(3, 1, 9)
customLL2.generate(3, 1, 9)
print(customLL1)
print(customLL2)
print(sumList(customLL1,customLL2))

# my function 2
def sumListRecur(list1, list2):
    current_node1 = list1.head
    current_node2 = list2.head
    list3 = LinkedList()
    value = 0
    index = 1
    increment = 0
    while current_node1 and current_node2:
        node_sum = current_node1.value + current_node2.value + increment
        if node_sum > 9:
            increment = 1
            value += (node_sum - 10) * index
            list3.add(node_sum - 10)
        else:
            increment = 0
            value += node_sum * index
            list3.add(node_sum)
        current_node1 = current_node1.next
        current_node2 = current_node2.next
        index = index * 10
    if increment == 1:
        list3.add(1)
        value += 1000
    return value


print('sumListRecur: ', sumListRecur(customLL1,customLL2))


# his function
def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    if carry > 1:
        ll.add(1)
    return ll

llA = LinkedList()
# llA.add(7)
llA.add(7)
llA.add(7)

llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)

print('llA: ', llA)
print('llB: ', llB)
print('sumList: ', sumList(llA, llB))