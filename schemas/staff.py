"""
This script defines the Staff of the hotel
Make use of composition in order to reduce repetition
"""


from abc import ABC, abstractmethod
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class Subscriber:
    """
    Defines the what/who is watching
    the object state."""

    name: Optional[str] = None

    @abstractmethod
    def update(self, message):
        """
        Definition of the method that notifies
        the state of the observable"""


@dataclass
class Publisher:
    """
    Defines the object that we want to observe
    """

    subscibers = []

    def register(self, who):
        """
        Register new object
        """
        self.subscibers.append(who)

    def unregister(self, who):
        """
        Remove object from observable
        """
        self.subscibers.remove(who)

    def dispatch(self, message):
        """
        Send message to subscibers
        """
        for subsciber in self.subscibers:
            subsciber.update(message)


@dataclass
class Employee:
    """
    Defining the class Employee
    """
    name: str = None
    surname: str = None
    employee_id: str = None
    shift: str = None
    publisher: Optional[Publisher] = None
    subsciber: Optional[Subscriber] = None

    def update(self, message):
        """
        Printing message
        """
        print(f"{self.name} got message {message}")
