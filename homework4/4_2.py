"""Task 2."""


class Bar(object):
    """Class Bar."""

    client_count = 0

    def __init__(self, name, age):
        """Attributes."""
        self.name = name
        self.age = age
        self.total_price = 0
        self.food = []
        self.alcohol = []
        Bar.client_count += 1

    def display_count(self):
        """Count."""
        print('Total number of visits %d' % Bar.client_count)

    def display_visit(self):
        """Visit."""
        print()

        print('Name : ', self.name)

        print('Age : ', self.age)

        print('Total price : ', self.total_price)

        print('Food ordered: ')

        for i in self.food:

            print(i)

        print('Alcohol ordered: ')

        for i in self.alcohol:

            print(i)

    def add_food(self, food, price):
        """Add Food."""
        self.food.append(food)

        self.total_price += price

    def add_alcohol(self, alcohol, price):
        """Add alcohol."""
        if self.age >= 18:

            self.alcohol.append(alcohol)

            self.total_price += price

        else:

            print()

            print("You can't drink alcohol! ")


bar1 = Bar('Tatsiana', 19)

bar1.add_food('  Beef', 14)

bar1.add_food('  Eggs', 3)

bar1.add_alcohol('  Vine', 5)

bar1.add_alcohol('  Cocktail', 12)

bar1.display_visit()

bar2 = Bar('Viktoriya', 20)

bar2.add_food('  Tacos', 12)

bar2.add_food('  Corn', 6)

bar2.add_alcohol('  Vine', 5)

bar2.add_alcohol('  Blood Mary', 10)

bar2.display_visit()

bar3 = Bar('Andrey', 17)

bar3.add_food('  Pizza', 4)

bar3.add_alcohol('  Beer', 12)

bar3.display_visit()
