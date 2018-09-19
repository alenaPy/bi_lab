"""Task4 part2."""


class ClothingStore(object):
    """Class ClothingStore."""

    client_count = 0

    def __init__(self, name, age, email, phone_number):
        """Object Initialization."""
        self.name = name
        self.age = age
        self.email = email
        self.phone_number = phone_number
        self.total_price = 0
        self.clothes = []

    def display_order(self):
        """Display the information about specific order."""
        print()
        print('Name : ', self.name)
        print('Age : ', self.age)
        print('Email : ', self.email)
        print('Phone : ', self.phone_number)
        print('Total price : ', self.total_price)
        print('Clothes ordered: ')
        for i in self.clothes:
            print(i)

    def add_clothes(self, clothes, price):
        """Add clothes in the order and count total price."""
        self.clothes.append(clothes)
        self.total_price += price


order1 = ClothingStore('Svetlana Nesenchuk', 20,
                       'svetlana_nesenchuk@epam.com', '65735487')
order1.add_clothes('  Jeans', 150)
order1.add_clothes('  Skirt', 120)
order1.add_clothes('  T-shirt', 135)
order1.add_clothes('  Sneakers', 200)

order1.display_order()

order2 = ClothingStore('Ann Kiryanava', 21,
                       'kiannet@gmail.com', '53453663')
order2.add_clothes('  Pullover', 100)
order2.add_clothes('  Dress', 200)
order2.add_clothes('  Shirt', 150)


order2.display_order()

order3 = ClothingStore('Anastasia', 18, 'nastya96@gmail.com', '234534656')
order3.add_clothes('  Skirt', 150)
order3.add_clothes('  Cardigan', 170)
order3.add_clothes('  Pants', 180)
