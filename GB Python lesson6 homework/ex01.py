a1 = int(input('Первый элемент арифметической прогрессии: '))
n = int(input('Количество элементов: '))
d = int(input('Разность: '))
a = []
for i in range(1, n + 1):
    a_ = a1 + (i - 1)*d
    a.append(a_)
print(a)