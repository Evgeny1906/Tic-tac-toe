
sq = [[' '] * 3 for q in range(3)]


def h():
    len_ = (f"   0 | 1 | 2 |")
    print(len_)

    for qs, s in enumerate(sq):

        row = f"{qs}| {' | '.join(s)} | "
        print(row)
        L = len(row)
        print("_" * L)

h()


def question_X():
    num = 0
    while True:
        num += 1
        if num % 2 == 0:
            n = "O"
        else:
            n = "X"

        dl = input(f"       введите координаты {n} :  ").split()
        if len(dl) != 2:
            print("введите 2 координаты")
            num -= 1
            continue

        d, l = dl
        if not(d.isdigit()) or not(l.isdigit()):
            print("введите цифры")
            num -= 1
            continue

        d, l = int(d), int(l)
        if 0 > d or d > 2 or 0 > l or l > 2:
            print("координаты в не диапазона")
            num -= 1
            continue


        if sq[d][l] != " ":
            print("клетка занята")
            num -= 1
            continue

        sq[d][l] = n
        if num == 9:
            print("Ничья!")
            return dl


        for i in range(3):
            f = []
            for j in range(3):
                f.append(sq[j][i])
                if f == [n, n, n]:
                    print(h())
                    print(f"ПОБЕДИЛ {n}!!!")
                    return dl
        for i in range(3):
            f = []
            for j in range(3):
                f.append(sq[i][j])
                if f == [n, n, n]:
                    print(h())
                    print(f"ПОБЕДИЛ {n}!!!")
                    return dl
        f = []
        for i in range(3):
            f.append(sq[i][i])
            if f == [n, n, n]:
                print(h())
                print(f"ПОБЕДИЛ {n}!!!")
                return dl

        f = []
        for i in range(3):
            f.append(sq[i][2 - i])
            if f == [n, n, n]:
                print(h())
                print(f"ПОБЕДИЛ {n}!!!")

                return dl

        h()

question_X()


