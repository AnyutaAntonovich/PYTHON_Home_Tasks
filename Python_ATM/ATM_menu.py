from art import tprint



def atm_menu():
    tprint('ATM')
    while True:
        print('-' * 25)
        print('МЕНЮ ПРОГРАММЫ:\n'
              '\t1 - Снять\n'
              '\t2 - Пополнить\n'
              '\t0 - Выход из программы')
        print('-' * 25)
        command = int(input('Ваш выбор: '))
        print('-' * 25)
        if command == 1:
            input_data()
        elif command == 2:
            print_data()
        elif command == 0:
            print('Хороший выбор! ;)')
            return False
        else:
            print('\033[31m' + '\nВведите цифру из пункта меню:' + '\033[0m')