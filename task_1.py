duration = 400153

s = duration % 60

m = (duration - s) // 60 % 60

h = (duration - s - m) // 3600 % 24

d = (duration - s - m - h) // 86400


if 0 <= duration <= 59:
    print(f'{s} сек')
elif 60 <= duration < 3599:
    print(f'{m} мин {s} сек')
elif 3600 <= duration < 86399:
    print(f'{h} час {m} мин {s} сек')
elif duration >= 86400:
    print(f'{d} дн {h} час {m} мин {s} сек')







