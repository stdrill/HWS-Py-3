# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [23, 6, 90, 5, 1, 7]

def SumElements (lst):
    result = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            result = result + lst[i]
    return result

print(SumElements(lst))