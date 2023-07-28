# Time Complexity: O(N)
# Space Complexity: O(1)
def maxArea(heights: list) -> int:
    left = 0
    right = len(heights) - 1
    max_area = 0
    while left < right:
        length = min(heights[left], heights[right])
        width = right - left
        area = length * width
        max_area = max(max_area, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area


if __name__ == "__main__":
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea([5, 3, 2, 1, 4]))
