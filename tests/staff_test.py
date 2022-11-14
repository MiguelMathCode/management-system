"""
This is the unit test for Staff
structure
"""

from schemas.staff import Employee, Publisher, Subscriber


manager = Employee(
        name="Asuna", surname="Yuuki",
        employee_id="858698", shift="day", subsciber=Subscriber())

counter = Employee(name="Kirigaya", surname="Kazuto",
                   employee_id="9958390", shift="day", publisher=Publisher())

counter.publisher.register(manager)


def test_data():
    assert manager.name == "Asuna"


def test_subscriber():
    assert counter.publisher.register(manager) == None
