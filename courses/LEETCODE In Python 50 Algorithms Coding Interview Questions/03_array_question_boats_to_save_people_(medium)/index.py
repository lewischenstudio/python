def numRescueBoats(people: list, limit: int) -> int:
    people.sort()

    heavyP = len(people) - 1
    lightP = 0

    boats = 0
    while heavyP >= lightP:
        if people[heavyP] + people[lightP] <= limit:
            boats += 1
            heavyP -= 1
            lightP += 1
        else:
            boats += 1
            heavyP -= 1

    return boats


if __name__ == "__main__":
    print(numRescueBoats([1, 2], 3))
    print(numRescueBoats([3, 2, 2, 1], 3))
    print(numRescueBoats([3, 5, 3, 4], 5))
