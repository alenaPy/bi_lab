price = float(input("Enter the item price:\n"))
num = int(input("Enter the number of items:\n"))

print("Total cost: {0} dollars {1} cents".format(round((price*100*num)//100),
                                                 round((price*100*num)%100)))


