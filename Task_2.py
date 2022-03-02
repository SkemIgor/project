cube_list = []                       # создаем пустые списки
my_list = []
my_list_17 = []

for i in range(1, 1001, 2):          # с помощью цикла создаем список из нечетных чисел от 1 до 1000
    cube_list.append(i ** 3)         # возводим эти числа в куб

for j in cube_list:                  # перебираем список
    sum_num = 0                      # создаем переменную в которую будем записывать сумму числа из списка
    while j != 0:                    # пока j не равно 0...
        sum_num += j % 10            # к переменной добавляется последняя цифра числа
        j //= 10                     # убираем последнюю цифру у числа
    if sum_num % 7 == 0:             # если сумма числа делится на 7 без остатка
        my_list.append(sum_num)      # записываем число в список
    for k in my_list:                # с помощью цикла
        sum_num += k                 # находим сумму чисел которые делятся нацело на 7

print(sum_num)                       # выводим сумму чисел которые делятся нацело на 7

cube_list = [x + 17 for x in cube_list]  # добавляем к каждому элементу списка 17

for j in cube_list:                  # перебираем список
    sum_num_17 = 0                   # создаем переменную в которую будем записывать сумму числа из списка
    while j != 0:                    # пока j не равно 0...
        sum_num_17 += j % 10         # к переменной добавляется последняя цифра числа
        j //= 10                     # убираем последнюю цифру у числа
    if sum_num_17 % 7 == 0:          # если сумма числа делится на 7 без остатка
        my_list_17.append(sum_num_17)      # записываем число в список
    for k in my_list_17:             # с помощью цикла
        sum_num_17 += k              # находим сумму чисел которые делятся нацело на 7

print(sum_num_17)                    # выводим сумму чисел которые делятся нацело на 7


