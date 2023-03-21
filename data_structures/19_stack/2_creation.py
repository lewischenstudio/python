"""
Stack creation

Stack using List
    - Easy to implement
    - Speed problem when it grows

Stack using Linked List
    - Fast performance
    - Implementation is not easy

WHen to use / avoid Stack

Use:
    - LIFO (Last-In-First-Out) functionality
    - The chance of data corruption is minimum

Avoid:
    - Random access is not possible
"""

class Stack:
    def __init__(self) -> None:
        self.list = []
    
    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)