# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input('Input the size of side a: '))
b = int(input('Input the size of side b: '))
c = int(input('Input the size of side c: '))

if a+b > c and a+c > b and b+c > a:
    print('Triangle exists')
    if a == b == c:
        print('Triangle is equilateral')
    elif a == b or b == c or a == c:
        print('Triangle isosceles')
    else:
        print('Triangle arbitrary')
else:
    print('Triangle not exists')
