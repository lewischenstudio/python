## Section 06: Array Question: Longest Substring Without Repetition (Medium)

#### Table of Contents
- Introduction to the problem
- Brute Force Intuition
- Psuedo code walkthrough
- Approach 2 Intuition
- Approach 2 psuedo code walkthrough
- Implementing the code


### Introduction to the problem
Given a string s, find the length of the longest substring without repeating
characters.

[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

#### Steps
- We can start from each character and find the longest substring 
- Loop over the rest of the characters until the end of the string
- `see_characters = { a: true, b: true, c: true, ... }`

```
lengthOfLongestSubstring(input) {
    if (input.length <= 1) return input.length
    max_length = 0
    for (L = 0, L < input.length, L++) {
        seen_characters = {}
        current_length = 0
        for (R = L, R < input.length, R++) {
            current_char = input[R]
            if (current_char in seen_characters) {
                break
            }
            current_length += 1
            seen_characters[currentChar] = true
            max_length = max(max_length, current_length)
        }
    }
}
```


### Approach 2 Intuition

#### Steps
- Left and right pointers
- `seen_characters = { a: 0, b: 1, c: 1, ...}`
- Update the left pointer when the right pointer gets a repeated 
  character in `seen_characters`
- Use the `while` loop

```
lengthOfLongestSubstring(input) {
    if (input.length <= 1) return input.length

    left = 0
    right = 0
    max_length = 0
    seen_characters = {}
    while (left < input.length and right < input.length) {
        current_char = input[right]
        if (current_cahr in seen_characters) {
            previous_character = seen_character[current_char]
            left = max(left, previous_character)
            seen_characters[current_char] += 1
        }
        seen_characters[current_char] = right
        max_length = max(max_length, right - left + 1)
        right += 1
    }
}
```