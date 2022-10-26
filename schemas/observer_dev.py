"""
Development of observer pattern
"""

from dataclasses import dataclass
from typing import Optional


class Subscriber:

    def __init__(self, name=None):
        self.name = name

    def update(self, message):
        print(f"{self.name} got message {message}")


class Publisher:

    def __init__(self):
        self.subscribers = []

    def register(self, who):
        self.subscribers.append(who)

    def unregister(self, who):
        self.subscribers.remove(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


@dataclass
class User:
    name: str = None
    publisher: Optional[Publisher] = None
    subscriber: Optional[Subscriber] = None

    def update(self, message):
        print(f"{self.name} got message {message}")


pub = Publisher()
sub = Subscriber()
user_1 = User("Kirito", pub)

user_2 = User("Asuna", sub)

user_1.publisher.register(user_2)

user_1.publisher.dispatch("sape!")
