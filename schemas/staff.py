"""This script defines the Staff of the hotel
 Make use of composition in order to reduce repetition"""


from abc import ABC, abstractmethod
from typing import Optional
from dataclasses import dataclass

class Publisher(ABC):

    def __init__(self):
        self.subscribers = set()

    @abstractmethod
    def register(self, who):
        pass


@dataclass
class Employee():
    """Defining the class Employee"""
    name: str = None
    surname: str = None
    employee_id: str = None
    shift: str = None
    subscribers: Optional[set] = None
    publisher: Optional[Publisher] = None

    def register(self, who):
        self.subscribers.add(who)
