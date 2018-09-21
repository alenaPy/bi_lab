"""Task4."""

from random import randint
from re import sub


class Coffee(object):
    """Class for coffe machine."""

    coffee_types = ['latte', 'mocaccino', 'macchiato',
                    'ristretto', 'americano', 'espresso',
                    'cappuccino', 'glace', 'irish',
                    'fredo', 'breve', 'corretto']

    def __init__(self, name, water_amount, sugar_amount,
                 coffee_amount, item_amount):
        """Initialize coffee machine."""
        self.name = name
        self.sugar_amount = sugar_amount
        self.coffee_amount = coffee_amount
        self.water_amount = water_amount
        self.items = []
        while len(self.items) < item_amount:
            item = [Coffee.coffee_types[randint(0,
                                                len(Coffee.coffee_types) - 1)]]
            if item not in self.items:
                self.items.append(item)

    def display_items(self):
        """Display all items in machine."""
        print("***Available coffee in {0}***".format(self.name))
        for i in self.items:
            print('--> {0}'.format(sub('[\'\][]', '', str(i))))

    def display_amount(self):
        """Display components amount in machine."""
        print("***Components amount in {0}***".format(self.name))
        print("Sugar amount: {0}".format(self.sugar_amount))
        print("Coffee amount: {0}".format(self.coffee_amount))
        print("Water amount: {0}".format(self.water_amount))

    def get_coffee(self, with_sugar):
        """Display your choice."""
        self.display_items()
        choice = [input("Make your choice --> ").lower()]
        if choice in self.items:
            if self.water_amount > 10 and \
                    self.sugar_amount > 10 and \
                    self.coffee_amount > 10:
                if with_sugar is True:
                    self.water_amount -= 10
                    self.sugar_amount -= 10
                    self.coffee_amount -= 5
                    print("Here is your your {0} with sugar."
                          .format(sub('[\'\][]', '', choice[0])))
                    return sub('[\'\][]', '', choice[0])
                else:
                    self.water_amount -= 10
                    self.coffee_amount -= 5
                    print("Here is your your {0}."
                          .format(sub('[\'\][]', '', choice[0])))
                    return sub('[\'\][]', '', choice[0])
            else:
                print("Sorry, machine is empty.")
        else:
            print("Sorry, we don't have this coffee.")

    def fill_the_machine(self, sugar, water, coffee):
        if(sugar > 0 and water > 0 and coffee > 0):
            self.sugar_amount += sugar
            self.coffee_amount += coffee
            self.water_amount += water
            return True
        else:
            return False
