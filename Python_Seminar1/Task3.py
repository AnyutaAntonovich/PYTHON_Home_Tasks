# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(0, 1000)
guessesTaken = 0

while guessesTaken < 10:
    print('What number did I guess?')
    user_number = int(input('Input the number from 0 to 1000: '))
    guessesTaken +=1
    if user_number > num:
        print('Need less!')
    if user_number < num:
        print('Need more!')
    if user_number == num:
        break

if user_number == num:
    guessesTaken = str(guessesTaken)
    print('Yes! You guessed right on ', guessesTaken, ' try!')

if user_number != num:
    guessesTaken = str(guessesTaken)
    print('Sorry, but you have no more attempts.')
