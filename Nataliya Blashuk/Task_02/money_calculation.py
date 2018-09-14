"""Purchase money calculation."""
itemCost = input("Enter the cost of the item (in format dd.cc): \n")
itemsNum = input("Enter the number of bought items: \n")


def total_cost(cost, items):
    """total_cost calculate the total coat of the bought items."""
    print("Total cost: %d dollars and %s cents" %
          (((float(cost) * 100 * int(items)) // 100),
           (float(cost) * 100 * int(items)) % 100))


total_cost(itemCost, itemsNum)
