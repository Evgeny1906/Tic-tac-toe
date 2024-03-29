from random import randint

sq = [[' '] * 3 for q in range(3)]

def grate():                        # Создаём решётку
    coord_y = '  | 0 | 1 | 2 |'
    print(coord_y)
    print('_' * len(coord_y))
    for coord_x, fild in enumerate(sq):
        row = f"{coord_x} | {' | '.join(fild) } | "
        print(row)
        print('_' * len(coord_y))

grate()
r = randint(1, 2)
count = r
while True:

    count += 1
    if count % 2 == 0:
        n = 'O'
    else:
        n = 'X'

    hv = input(f"Введите координаты '{n}' через пробел: ").split()
    if len(hv) != 2:
        print("Введите 2 цифры")
        count -= 1
        continue

    h, v = hv
    if not(h.isdigit()) or not(v.isdigit()):
        print('Введите цифры')
        count -= 1
        continue

    h, v = int(h), int(v)
    if h < 0 or h > 2 or v < 0 or v >2:
        print('Координаты в не диапазона')
        count -= 1
        continue

    if sq[h][v] == 'O' or sq[h][v] == 'X':   #Проверка на занятость клетки
        print('Эта клетка занята, выберите другую.')
        count -= 1
        continue
    else:
        sq[h][v] = n
# Проверка выйгрышных вариантов:
    if sq[0][0] == sq[0][1] == sq[0][2] == n or sq[1][0] == sq[1][1] == sq[1][2] == n \
            or sq[2][0] == sq[2][1] == sq[2][2] == n or sq[0][0] == sq[1][0] == sq[2][0] == n \
            or sq[0][1] == sq[1][1] == sq[2][1] == n or sq[0][2] == sq[1][2] == sq[2][2] == n \
            or sq[0][0] == sq[1][1] == sq[2][2] == n or sq[0][2] == sq[1][1] == sq[2][0] == n:
        grate()
        print('Winner :', n)
        break

    if count == 9:
        grate()
        print('Ничья!')
        break

    grate()

