""" house Robber Problem using Dynamic Programming"""


# Top Down Approach
def houseRobberTD(houses, currentIndex, memo):
    if currentIndex >= len(houses):
        return 0
    elif currentIndex not in memo:
        stealFirstHouse = houses[currentIndex] + houseRobberTD(
            houses,
            currentIndex + 2,
            memo,
        )
        skipFirstHouse = houseRobberTD(houses, currentIndex + 1, memo)
        memo[currentIndex] = max(stealFirstHouse, skipFirstHouse)
    return memo[currentIndex]


# Bottom Up Approach
def houseRobberBU(houses):
    tempArr = [0] * (len(houses) + 2)
    for i in range(len(houses) - 1, -1, -1):
        tempArr[i] = max(houses[i] + tempArr[i + 2], tempArr[i + 1])
    return tempArr[0]


houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobberTD(houses, 0, {}))
print(houseRobberBU(houses))
