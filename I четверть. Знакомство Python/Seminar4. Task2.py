"""
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты 
высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на
грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число 
ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит 
из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает 
ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один 
заход собирающий модуль, находясь перед некоторым кустом. На входе задано количество ягод 
на каждом кусте. Не обязательно вводить их с клавиатуры, можно задать 
непосредственно в коде программы
    Примеры/Тесты:
    Input1: 1, 2, 3, 4, 5, 6, 7, 8
    Output1: Макс. кол-во ягод 21, собрано для куста 7

    Input1: 11, 92, 1, 42, 15, 12, 11, 81
    Output1: Макс. кол-во ягод 184, собрано для куста 1
"""

lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
total_sum = 0
for idx in range(len(lst1)):
    idx_next = idx + 1 if idx != len(lst1) - 1 else idx - len(lst1) + 1
    sum_current = lst1[idx - 1] + lst1[idx] + lst1[idx_next]
    if sum_current > total_sum:
        total_sum = sum_current
        find_idx = idx
print(f"Макс. кол-во ягод {total_sum}, собрано для куста {find_idx+1}")