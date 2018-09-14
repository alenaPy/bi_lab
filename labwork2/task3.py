"""Labwork2"""

#Task3. FizzBuzz
for n in range(1,101):
    if n%3==0 and n%5!=0:
        print('Fizz,')
    elif n%5==0 and n%3!=0:
        print('Bizz,')
    elif n%5==0 and n%3==0:
        print('FizzBizz,')
    else:
        print (n,",")