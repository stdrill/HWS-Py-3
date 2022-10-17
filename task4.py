# Напишите программу, которая будет преобразовывать десятичное число в двоичное

num = 8
bin = ''
while num > 0:
    ost = num % 2
    bin = str(ost) + bin
    num = num // 2
print(bin)
