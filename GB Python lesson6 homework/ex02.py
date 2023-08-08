import random
items = [random.randint(0, 10) for i in range(15)]
print(items)
min_ = int(input('Укажите диапозон. От: '))
max_ = int(input('До: '))
for i in range(len(items)):
    if min_ < items[i] < max_:
        print(i)