def dis_year_leap(number):
    return "True" if number % 4 == 0 else "False"

num = int(input("Введите год: "))
result = dis_year_leap(num)
print(f"{num} - {result}")