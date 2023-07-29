# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

number = int(input('Input the number: '))

h = hex(number)

print(h)

def to_hex(number):
    hex_digits = "0123456789abcdef"
    hex_str = ""
    while number > 0:
        hex_str = hex_digits[number % 16] + hex_str
        number = number // 16
    return hex_str

hex_str = to_hex(number)
print(f"Hexadecimal representation of a number {number} - {hex_str}")
