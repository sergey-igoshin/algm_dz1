"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
import random


def get_number(a):
    num = a[0]          # O(1)
    for i in a:         # O(n)
        if i < num:     # O(1)
            num = i     # O(1)
    return num          # O(1)
# T(n) = 1 + n * (1 + 1) + 1 = 2n + 2
# сложность O(n)


def get_num(a):
    n = 1                                   # O(1)
    while n < len(a):                       # O(n)
        for i in range(len(a) - n):         # O(n)
            if a[i] > a[n]:                 # O(1)
                a[i], a[n] = a[n], a[i]     # O(1 + 1)
        n += 1                              # O(1)
    return a[0]                             # O(1)
# T(n) = 1 + n * (n + 1 + 1 + 1 + 1) + 1 = n**2 + 4n + 2
# сложность O(n**2)


my_list = random.sample(range(0, 100), 10)
print(my_list, get_number(my_list), sep='\n')
print(get_num(my_list))
