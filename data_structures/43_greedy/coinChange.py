"""Coin Change Problem  in Python"""


def coinChange(totalNumber, coins):
    coins.sort()
    index = len(coins) - 1
    result = 0
    while True:
        coinValue = coins[index]
        if totalNumber >= coinValue:
            print(coinValue)
            result += 1
            totalNumber = totalNumber - coinValue
        if totalNumber < coinValue:
            index -= 1

        if totalNumber == 0:
            break
    print("result: ", result)
    return result


def coinChangeForLoop(totalNumber, coins):
    """
    We can't really use for loop for this problem
    because we need to visit the previous index
    if totalNumber >= coinValue
    """
    coins.sort(reverse=True)
    result = 0
    for number in coins:
        coinValue = number
        if totalNumber >= coinValue:
            print(coinValue)
            result += 1
            totalNumber = totalNumber - coinValue
        if totalNumber < coinValue:
            pass
        if totalNumber == 0:
            break
    print("result: ", result)
    return result


coins = [1, 2, 5, 20, 50, 100]
coinChange(201, coins)
coinChangeForLoop(201, coins)
