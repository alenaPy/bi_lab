"""Count purchase amount according to input amount of price and quantity."""


def purchase_count(dollar, cent, number):
    """Count purchase amount."""
    if dollar < 0:
        print('Invalid number of dollars: it should be positive')
        return
    if cent > 100:
        print('Invalid number of cents: it should be less then 100')
        return
    elif cent < 0:
        print('Invalid number of cents: it should be positive')
        return
    if quantity < 0:
        print('Invalid quantity: it should be positive')
        return
    print('Purchase amount is %d dollars %d cents' %
          ((dollar * 100 + cent) * number // 100,
           (dollar * 100 + cent) * number % 100))


dollars = int(input('Input item price part of dollars:'))
cents = int(input('Input item price part of cents:'))
quantity = int(input('Input item quantity:'))
purchase_count(dollars, cents, quantity)
