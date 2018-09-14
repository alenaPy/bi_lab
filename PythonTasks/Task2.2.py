"""Total price calculating program."""
SENTENCE = "Total cost: {dollars} dollars {cents} cents"
price = float(input("Enter the item price:\n"))
num = int(input("Enter the number of items:\n"))

print(SENTENCE.format(dollars=round((price * 100 * num) // 100),
                      cents=round((price * 100 * num) % 100)))
