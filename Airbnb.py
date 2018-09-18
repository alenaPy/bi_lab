"""Airbnb."""


class Hotel(object):
    """Hotel."""

    renter_count = 0

    def __init__(self, name, age):
        """Init."""
        self.name = name
        self.age = age
        self.total_cost = 0
        self.location = []
        self.discount = 0
        Hotel.renter_count += 1

    @staticmethod
    def display_count():
        """RenterCount."""
        print('Total number of visitors %d' % Hotel.renter_count)

    def display_renters(self):
        """Renters."""
        print()
        print('Name : ', self.name)
        print('Age : ', self.age)
        print('Total cost : ', self.total_cost)
        print('Location: ')
        for i in self.location:
            print(i)
        print('Discount:{0} '.format(self.discount))

    def add_location(self, location, cost):
        """Location."""
        self.location.append(location)
        self.total_cost += cost

    def add_discount(self, disc):
        """Discount."""
        self.discount = disc
        self.total_cost -= disc


hotel2 = Hotel('Armen', 65)
hotel2.add_location('  Amsterdam', 53)
hotel2.add_location('  Brussels', 42)
hotel2.add_discount(10)

hotel2.display_renters()

hotel3 = Hotel('Suren', 29)
hotel3.add_location('  Berlin', 87)
hotel3.add_location('  Madrid', 96)
hotel3.add_discount(20)

hotel3.display_renters()

hotel4 = Hotel('Tatevik', 18)
hotel4.add_location('  Vienna', 45)
hotel4.add_location('  Copenhagen', 140)
hotel4.add_discount(20)

hotel4.display_renters()

hotel4.display_count()
