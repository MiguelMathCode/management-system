"""This script defines the Staff of the hotel
 Make use of composition in order to reduce repetition"""


from pydantic import BaseModel
from abc import ABC, abstractmethod

class Publisher(ABC):

    def __init__(self):
        self.subscribers = set()

    @abstractmethod
    def register(self, who):
        self.subscribers.add(who)


class Employee(BaseModel, Publisher):
    """Defining the class Employee"""
    name: str = None
    surname: str = None
    employee_id: str = None
    shift: str = None

    def register(self, who):
        self.subscribers.add(who)
