str_percent = ['процент', ] * 100


for num, str_per in enumerate(str_percent, 1):
    if 10 <= num <= 20:
        str_per = str_per + 'ов'
    elif num % 10 == 2 or num % 10 == 3 or num % 10 == 4:
        str_per = str_per + 'а'
    elif num % 10 == 5 or num % 10 == 6 or num % 10 == 7 or num % 10 == 8 or num % 10 == 9 or num % 10 == 0:
        str_per = str_per + 'ов'

    print(num, str_per)