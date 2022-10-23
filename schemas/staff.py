"""This script defines the Staff of the hotel
 Make use of composition in order to reduce repetition"""


from pydantic import BaseModel


class Employee(BaseModel):
    """Defining the class Employee"""
    name: str = None
    surname: str = None
    employee_id: str = None
    shift: str = None


class Recepcionist(Employee):
    """Defining the recepcionist class and its methods"""

    def subs(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.remove(who)
    def dispatch(self, message):
        for subscribers in self.subscribers:
            subscribers.update(message)


class Manager(Employee):

    def __init__(self, name):
        self.name = name
    def update(self, message):
        print(f'{self.name} got message {message}')


class RoomService(Employee):

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} got message {message}")
