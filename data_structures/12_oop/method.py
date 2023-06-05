"""Class Methods"""


class YouTube:
    def __init__(self, username, subscribers=0, subscriptions=0) -> None:
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1


user1 = YouTube("Lewis", 0)
user2 = YouTube("Jack", 4)
print(user1.username)
print(user1.subscribers)
print(user1.subscriptions)

print(user2.username)
print(user2.subscribers)
print(user2.subscriptions)

user1.subscribe(user2)
user2.subscribe(user1)
print(f"User 1 subscribers: {user1.subscribers}")
print(f"User 1 subscriptions: {user1.subscriptions}")
print(f"User 2 subscribers: {user1.subscribers}")
print(f"User 2 subscriptions: {user1.subscriptions}")
