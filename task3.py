# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = [1.1, 1.2, 3.1, 5, 10.01]

lst = list(filter(lambda num: type(num) != int , lst))

for i in range(len(lst)):
    lst[i] = round(lst[i] - int(lst[i]), 2)
print(lst)

result = max(lst) - min(lst)
print(result)