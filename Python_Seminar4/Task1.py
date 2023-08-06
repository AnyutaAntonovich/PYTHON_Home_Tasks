# Напишите функцию для транспонирования матрицы.
# НЕ СПИСАНО! Долго мучалась, но всё заработало. (P.S. Я преподаватель высшей математики, поэтому с
# пониманием математической части проблем не было)

#Решение первое (без функции), для себя
# matrix = [[5, 6, 3], [1, 4, 8]]
# trans_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
# print(matrix)
# print(trans_matrix)

#Решение второе (с функцией)
def trans_matrix(matrix):

    # Задаем пустую матрицу обратную
    trans_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # Используем вложенный цикл for в матрице
    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            # Сохраняем результат транспонирования в пустой матрице
            trans_matrix[b][a] = matrix[a][b]
    return(trans_matrix)

# Задаем матрицу
matrix = [[5, 4, 3], [2, 4, 6], [4, 7, 9], [8, 1, 3]]

# Выводим результат
print("The transpose of matrix is: ")

for res in trans_matrix():
    print(res)
