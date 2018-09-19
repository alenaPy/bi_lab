"""Class Vehicle implementation."""


class Vehicle(object):
    """Vehicle."""

    def __init__(self, color, doors, vtype):
        """Constructor."""
        self.color = color
        self.doors = doors
        self.vtype = vtype

    def brake(self):
        """Stop the vehicle."""
        return "I'm braking"

    def drive(self):
        """Drive the vehicle."""
        return "I'm driving!"

    def beep(self):
        """Beep."""
        return "BEEP!"


v1 = Vehicle('Red', 5, 'car')
v2 = Vehicle('Blue', 2, 'truck')
v3 = Vehicle('Green', None, 'bike')

print(v1.brake())
print(v2.drive())
print(v3.beep())

v1.color = 'Blue'
v2.type = 'truck'

print(v1.color, v1.doors, v1.vtype)
print(v2.color, v2.doors, v2.vtype)
print(v3.color, v3.doors, v3.vtype)
