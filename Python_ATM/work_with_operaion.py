


# Сумма на счету
cash_sum = 0

# Пополнение счета
def refill():
    ref = int(input('Введите сумму для пополнения счета: '))
    cash_sum = cash_sum + ref

    return cash_sum


# Снятие со счета
def withdrawal():
    cash_out = int(input('Введите сумму для снятия со счета: '))
    if cash_out <= cash_sum:
        cash_sum = cash_sum - cash_out
    else:
        print('Запрошенная сумма превышает сумму на счете!')
        print('Вы можете снять до', cash_sum, 'средств')

    return cash_sum

