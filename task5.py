# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

a = int(input('Введите число: '))

fib = [1,1]
nefib = [1,-1]

def neFib():
    for i in range(2, a):
        next_fib = fib[i-1] + fib[i-2]
        fib.append(next_fib)

        next_nefib = nefib[i-2] - nefib[i-1]
        nefib.append(next_nefib)

    nefib.reverse()
    nefib.append(0)

    return nefib+fib

print(neFib())
