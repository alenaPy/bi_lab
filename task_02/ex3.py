"""FizzBuzz implementation."""

'''for i in range(1, 101):
    fizz = i % 3 == 0
    buzz = i % 5 == 0
    if fizz & buzz:
        print('FizzBuzz')
    elif fizz:
        print('Fizz')
    elif buzz:
        print('Buzz')
    else:
        print(i)'''

# the variant i like more
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
