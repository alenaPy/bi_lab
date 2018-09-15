"""Purchase money calculation."""

import math

# input parameters initialization

# cents are floor rounded (e.g., 98.259 will me converted into 98.25
# as cents cannot be more than 100)
item_price = math.floor(float(
    input("Please input item's price in 999.99 format (dollars.cents): "
          )) * 100) / 100
if item_price < 0:
    raise Exception("Item/'s price cannot be negative")

item_num = int(input("Please input number of items: "))
if item_num < 0:
    raise Exception("Number of items cannot be negative")

# evaluating total cost
total_cost = round(item_price * item_num, 2)
print("Total cost:", int(total_cost), "dollars",
      int(round(total_cost % 1, 2) * 100), "cents")
