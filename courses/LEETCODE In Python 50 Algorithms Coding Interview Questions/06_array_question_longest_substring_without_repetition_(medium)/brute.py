def lengthOfLongestSubstring(input: str):
    if len(input) <= 1:
        return len(input)

    max_length = 0
    for left in range(len(input)):
        seen_characters = {}
        current_length = 0
        for right in range(left, len(input)):
            current_character = input[right]
            if current_character in seen_characters:
                break
            current_length += 1
            seen_characters[current_character] = True
            max_length = max(max_length, current_length)
    return max_length


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcdea"))
    print(lengthOfLongestSubstring("acdceca"))
    print(lengthOfLongestSubstring("aaaaaa"))
    print(lengthOfLongestSubstring("pwwkew"))
