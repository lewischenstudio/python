def lengthOfLongestSubstring(input: str):
    n = len(input)
    if n <= 1:
        return n

    left = 0
    right = 0
    seen_character = {}
    max_length = 0
    while left < n and right < n:
        current_character = input[right]
        if current_character in seen_character:
            previous_position = seen_character[current_character]
            left = max(left, previous_position + 1)
        seen_character[current_character] = right
        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcdea"))
    print(lengthOfLongestSubstring("acdceca"))
    print(lengthOfLongestSubstring("aaaaaa"))
    print(lengthOfLongestSubstring("pwwkew"))
