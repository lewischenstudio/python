"""
Fractional Knapsack Problem  in Python
Time complexity: O(NlogN)
Space complexity: O(1)
"""


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)  # O(NlogN)
    usedCapacity = 0
    totalValue = 0
    for i in items:  # O(N)
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value

        if usedCapacity == capacity:
            break
    print("Total value obtained: " + str(totalValue))


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
cList = [item1, item2, item3]

knapsackMethod(cList, 50)


def my_knapsck_method():
    densities = [(5, 20), (4, 30), (6, 10)]
    densities.sort(key=lambda x: x[0], reverse=True)
    weight_limit = 50
    total = 0
    for item in densities:
        weight = item[1]
        density = item[0]
        remain_weight = weight_limit - weight
        if remain_weight > 0:
            total = total + density * weight
            weight_limit = weight_limit - weight
        elif weight - weight_limit > 0:
            remain_weight = weight_limit
            total = total + density * remain_weight
            weight_limit = weight - weight_limit
        if weight_limit <= 0:
            break
    print("Total value obtained: : ", total)
