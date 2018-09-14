"""Print a string."""


price = float(input('Input price item: '))

count = int(input('Input count items: '))

a = round((price * 100 * count) // 100)
b = round((price * 100 * count) % 100)
print('Total cost: {0} dollars {1} cents'.format(a, b))
