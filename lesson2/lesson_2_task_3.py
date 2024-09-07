import math

def square(Сторона_квадрата):
    return math.ceil(Сторона_квадрата)

num_items = int(input("Введите cторону квадрата: "))
print(f"Площадь квадрата: {square(num_items*num_items)}")