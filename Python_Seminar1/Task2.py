# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number = int(input('Input the number: '))
count = 0

if number < 0 or number > 100000:
    print('An invalid number was entered. Valid numbers are from 0 to 100000.')
elif number == 1 or number == 0:
    print('The number is neither prime nor composite.')
else:
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    if count <= 0:
        print('The number is prime.')
    else:
        print('The number is composite.')
