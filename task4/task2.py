"""Task4."""

from random import randint


class Coffemachine:
    """Class for coffe machine."""

    coffee_types = ['latte', 'mocaccino', 'macchiato',
                    'hot milk', 'ristretto', 'hot chocolate',
                    'espresso']

    def __init__(self, name, milk_amount, water_amount,
                 coffee_amount, item_amount):
        """Initialize coffee machine."""
        self.name = name
        self.milk_amount = milk_amount
        self.coffee_amount = coffee_amount
        self.water_amount = water_amount
        self.items = []
        for i in range(1, item_amount + 1):
            item = [Coffemachine.coffee_types[
                        randint(0, len(Coffemachine.coffee_types)-1)]]
            if item not in self.items:
                self.items.append(item)

    def display_items(self):
        """Display all items in machine."""
        print("Total items are: ")
        for i in self.items:
            print(i)


machine1 = Coffemachine('BaristaMax', 200, 200, 200, 4)
machine1.display_items()
