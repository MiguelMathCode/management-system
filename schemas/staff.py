"""
This script defines the Staff of the hotel
Make use of composition in order to reduce repetition
"""


from abc import ABC, abstractmethod
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class Employee():
    """
    Defining the class Employee
    """
    name: str = None
    surname: str = None
    employee_id: str = None
    shift: str = None
