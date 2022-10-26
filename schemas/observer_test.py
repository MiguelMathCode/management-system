"""
Test of observer development
"""

from observer_dev import Publisher, Subscriber

pub = Publisher()

bob = Subscriber("Bob")
alice = Subscriber("Alice")
john = Subscriber("John")

pub.register(bob)
pub.register(alice)
pub.register(john)

pub.dispatch("Sape")
