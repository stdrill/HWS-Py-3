# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

nums = [23, 4, 3, 8, 2]

def Multiplication_elements (nums):
    res = []
    for i in range(len(nums) // 2):
        res.append(nums[i] * nums[int(len(nums) - i - 1)])
    if len(nums) % 2 != 0:
        mid = len(nums) // 2 
        res.append(nums[mid] * nums[mid])
    return res

print(Multiplication_elements(nums))
