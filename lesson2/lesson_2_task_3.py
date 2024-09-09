from math import ceil

num_items = float(input("Введите cторону квадрата: "))


def square(num_items):
    formula = num_items * num_items
    return formula


rounded = ceil(square(num_items))

print("Площадь квадрата: " + str(rounded))
