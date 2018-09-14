"""Purchase money calculation."""

dollars = int(input('Please enter dollars:'))
cents = int(input('Please enter cents:'))
items = int(input('Please enter the number of items:'))


def total_cost(dollars, cents, items):
    """Total cost calculation."""
    total_dollars = int((dollars * 100 + cents) * items // 100)
    total_cents = int((dollars * 100 + cents) * items % 100)
    text = "Total cost is %d dollars and %d cents"
    print(text % (total_dollars, total_cents))


total_cost(dollars, cents, items)
