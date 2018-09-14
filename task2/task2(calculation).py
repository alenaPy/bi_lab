dollar = int(input('Please enter dollars\n'))
cent = int(input('Please enter cents\n'))
items = int(input('Please enter items\n'))

dollar = int(dollar) * 100
sum = ((int(dollar) + int(cent)) * items) / 100
print('Total cost: %.2f' % sum)
