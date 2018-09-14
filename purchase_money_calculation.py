"""
Description of script.

It takes data for one item and calculate total cost.
    Example.
    Input: one item price is 3 dollars 20 cents, calculate price for 3 items
    Output data: Total cost:  9 dollars 20 cents.

"""
import re
data_in = input("Type your data: ")

# Find space between numbers for dollars and cents
_dollars = data_in.find(" dollar")
_is = data_in.find(" is ")
_cents = data_in.find(" cent")
_for = data_in.find("for ")

# remove possible whitespaces
dollars = data_in[(_is + 3):_dollars].strip()
cents = data_in[_dollars+8:_cents].strip()
amount = re.sub('[a-zA-Z]', '', data_in[_for::]).strip()

# calculate totals
total_dollars = int(dollars)*int(amount)
amount_cents = int(cents)*int(amount)
dollars_in = int(amount_cents)/100

# check cents for overflow
if int(cents)*int(amount) < 100:
    total_cents = int(cents) * int(amount)
else:
    total_dollars += int(dollars_in)
    total_cents = amount_cents % 100

print("Total cost: {0} dollars {1} cents".format(total_dollars, total_cents))
