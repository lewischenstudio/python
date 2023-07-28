# Time Complexity: O(N^2)
# Space Complexity: O(1)
def maxArea(heights: list) -> int:
    max_area = 0
    for i in range(len(heights) - 1):
        for j in range(i + 1, len(heights)):
            length = min(heights[i], heights[j])
            width = j - i
            area = length * width
            max_area = max(max_area, area)
    return max_area


if __name__ == "__main__":
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea([5, 3, 2, 1, 4]))
