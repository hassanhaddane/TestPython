from multiprocessing import Process


n = int(input('Entrer un nombre: '))
for i in range(3):

    if n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz.')
    else:
        print(n)
    break
