"""Fuel station."""


class Dispenser:
    """Class describes fuel dispensers on station."""

    def __init__(self, num, fuel_type, fuel_balance, capacity):
        """Init."""
        self.num = num
        self.fuel_type = fuel_type
        self.fuel_balance = fuel_balance
        self.capacity = capacity

    def refuel(self, litres):
        """Add fuel."""
        if (litres + self.fuel_balance) <= self.capacity:
            self.fuel_balance += litres
            print("Refuel dispenser number " + str(self.num) + " with " + str(litres) +
                  " litres. Total fuel balance = " + str(self.fuel_balance))
        else:
            print("Dispenser number: " + str(self.num) + " can be refueled only by " +
                  str(self.capacity - self.fuel_balance) + " litres")

    def refill_car(self, litres):
        """Refill car."""
        if (self.fuel_balance - litres) >= 0:
            self.fuel_balance -= litres
            print("Refill car from dispenser number " + str(self.num) + " with " + str(
                litres) + " litres. Total fuel balance = " + str(self.fuel_balance))
        else:
            print("Dispenser number: " + str(self.num) + " - not enough fuel.  Available " +
                  str(self.fuel_balance) + " litres")


class FuelStation:
    """Class describes fuel station."""

    dispenser_list = []

    def __init__(self, name):
        """Init."""
        self.name = name
        FuelStation.dispenser_list.append(Dispenser(1, '95', 0, 2000))
        FuelStation.dispenser_list.append(Dispenser(2, '92', 0, 5000))
        FuelStation.dispenser_list.append(Dispenser(3, 'D', 0, 3000))
        print("Station with name " + name + " created")


station = FuelStation("A100")

station.dispenser_list[0].refuel(2000)
station.dispenser_list[0].refuel(300)  # full
station.dispenser_list[1].refuel(2000)
station.dispenser_list[2].refuel(3000)
station.dispenser_list[0].refill_car(500)
station.dispenser_list[1].refill_car(500)
station.dispenser_list[0].refill_car(500)
station.dispenser_list[2].refill_car(500)
station.dispenser_list[0].refill_car(1005)  # not enough

d = Dispenser(4, 'D*', 0, 2000)  # add new dispenser
station.dispenser_list.append(d)
station.dispenser_list[3].refuel(2000)
