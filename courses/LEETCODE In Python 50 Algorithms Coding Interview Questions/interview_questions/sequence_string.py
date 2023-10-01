"""
Given a sequence string, return a sequence string in a way that
when the sum of the last nodes is greater than the node, return the node value.

Example:
Input: (5, 10(1,2,3), 15(10,30,10), 2(0,0,0), 3(2(1,1,1), 1))

Output: (5, 10(1,2,3), 15, 2(0,0,0), 3(2, 1))

Explanation:
- For node 15(10,30,10), the sum of the (10,30,10) is greater than 15
- For node 2(1,1,1), the sum of (1,1,1) is greater than 2
- For node 3(2,1), the sum of (2,1) is 3, so we keep (2,1)
"""
import re

sequence_string = "(5, 10(1,2,3), 15(10,30,10), 2(0,0,0), 3(2(1,1,1), 1))"


# print(sequence_string[1:-1].replace(" ", ""))

sequence_string = sequence_string[1:-1].replace(" ", "")

result = re.split(r"[\d(\S\d)]", sequence_string)

print("result: ", result)

# my_numbers = [str(number) for number in range(0, 10)]
# my_string = ""
# left = 0
# right = 0
# while right < len(sequence_string):
#     char = sequence_string[left]
#     if char == ",":
#         my_string += char
#         left += 1
#         right += 1
#     if char == "(": # 3(2(1,1,1),1)
#         right = left
#         end = 0
#         total1 = 0
#         total2 = 0
#         for j in range(right + 1, len(sequence_string)):
#             if sequence_string[j] == "(":
#                 try:
#                     total1 += int(sequence_string[j-1])
#                 except Exception:
#                     pass
#             if sequence_string[j] == ")":
