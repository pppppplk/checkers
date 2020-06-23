import sys
import numpy as num
a=int(input('Введите цвет шашек, за которые вы хотите играть\nЧёрный-1\nБелый-2:'))
if a == 1:
    print('Ваш цвет-чёрный!')
    B = 'Ч'
    W = 'Б'
    A = '+'
    Y = ' '
    QW = 'ДБ'
    QB = ' ДЧ'

    table = num.array([[1, B, Y, B, Y, B, Y, B, Y],
                       [2, Y, B, Y, B, Y, A, Y, A],
                       [3, A, Y, W, Y, A, Y, W, Y],
                       [4, Y, W, Y, A, Y, A, Y, A],
                       [5, A, Y, A, Y, A, Y, A, Y],
                       [6, Y, A, Y, A, Y, A, Y, A],
                       [7, A, Y, A, Y, W, Y, A, Y],
                       [8, Y, A, Y, W, Y, A, Y, A]])

    print('       A   B   C   D   E   F   G   H')
    print(table)


    class Black: #создаем класс для черных шашек

        def __init__(self, tab,str_for_file):
            self.tab = tab
            self.count_xod = 1
            self.str_for_file = str_for_file

        def out(out1):
            d = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
                 "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
            if out1 in d:
                return d[out1]
            else:
                print('Ошибка')

        def chip(self, a_line, b, c_line, d): # ходы пользователя, игравшего за черные шашки
            B = 'Ч'
            W = 'Б'
            A = '+'
            Y = ' '
            QW = 'ДБ'
            QB = 'ДЧ'
            if self.tab[a_line][b] == B:
                if 0 <= b <= 8:
                    self.tab[a_line][b] = A
                    if 0 <= d <= 8:
                        if self.tab[c_line][d] == A:
                            if b < d:
                                if self.tab[c_line - 1][d - 1] == W:
                                    self.tab[c_line - 1][d - 1] = A
                                    self.tab[c_line][d] = B
                                    self.str_for_file += ('{}{}:{}{}'.format(outt, out2, place1, place2))
                                else:
                                    self.tab[c_line][d] = B
                                    self.str_for_file += ('{}{}-{}{}'.format(outt, out2, place1, place2))
                            elif b > d:
                                if self.tab[c_line - 1][d + 1] == W:
                                    self.tab[c_line - 1][d + 1] = A
                                    self.tab[c_line][d] = B
                                    self.str_for_file += ('{}{}:{}{}'.format(outt, out2, place1, place2))
                                else:
                                    self.tab[c_line][d] = B
                                    self.str_for_file += ('{}{}-{}{}'.format(outt, out2, place1, place2))
                            if c_line == 7:
                                self.tab[c_line][d] = QB
                                self.str_for_file+='X'
                                print('Ты выиграл!')
                                print(self.str_for_file)
                                file = open("shashki.txt", "a")
                                file.write(self.str_for_file)
                                file.close()
                        elif self.tab[c_line][d] == Y:
                            self.tab[a_line][b] = B
                            print('Ошибка! На пустые клетки  ходить нельзя!')
                        elif self.tab[c_line][d] == B:
                            self.tab[a_line][b] = B
                            print('Клетка занята, выберите другую!')
                        elif self.tab[c_line][d] == W:
                            self.tab[a_line][b] = B
                            print('Клетка занята, выберите другую!')
                        elif self.tab[c_line + 1][d - 1] == W and self.tab[c_line + 2][d - 2] == W:
                            self.tab[c_line][d] = B
                        elif self.tab[c_line + 1][d + 1] == W and self.tab[c_line + 2][d + 2] == W:
                            self.tab[c_line][d] = B
            elif self.tab[a_line][b] == W:
                print('Вы походили шашкой соперника. Это невозможно. Походите еще раз своей шашкой! ')
            self.str_for_file +=' '
            self.count_xod += 1
            return self.tab




    class ComputerB(Black): # белые шашки(компьютер против пользователя)
        def __init__(self, tab, str_for_file):
            self.tab = tab
            self.str_for_file=str_for_file
        def oute(out1):
            d = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
                 "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
            dobr=dict((v,k) for k,v in d.items())
            if out1 in dobr:
                return dobr[out1]
            if out1 in d:
                return d[out1]
            else:
                return ('Ошибка')


        def choice(self, q_line, w): #ходы компьютера, играющего за белые шашки
            B = 'Ч'
            W = 'Б'
            A = '+'
            Y = ' '
            QW = 'ДБ'
            QB = 'ДЧ'
            count_black=0
            count_white=0
            count = 0
            self.winner = False
            flag = True
            if 1 <= w <= 8 and 0 <= q_line <= 7:
                for w in range(1,8):
                    for q_line in range(8):
                        if self.tab[q_line][w]==B:
                            count_black+=1
                        elif self.tab[q_line][w]==W:
                            count_white+=1
                if count_black==0:
                    print('Игра закончилась, компьютер выиграл!')
                    self.str_for_file+='X'
                    file=open("shashki.txt",'a')
                    file.write(self.str_for_file)
                    file.close()
                    sys.exit()
                elif count_white==0:
                    print('Игра закончилась, ты выиграл!')
                    self.str_for_file += 'X'
                    file = open("shashki.txt", 'a')
                    file.write(self.str_for_file)
                    file.close()
                    sys.exit()


                for w in range(1, 8):
                    if flag == False:
                        break
                    else:
                        for q_line in range(8):
                            if flag == False:
                                break
                            else:
                                if self.tab[q_line][w] == W:
                                    flag = False
                                    if self.tab[q_line - 1][w + 1] == B and 1 <= w + 2 <= 8 and 0 <= q_line - 2 <= 7:
                                        if self.tab[q_line - 2][w + 2] == B:
                                            self.tab[q_line][w] = W
                                        else:
                                            self.tab[q_line][w] = A
                                            self.tab[q_line - 1][w + 1] = A
                                            self.tab[q_line - 2][w + 2] = W
                                            self.str_for_file += ('{}{}:{}{}'.format(ComputerB.oute(w), q_line+1,ComputerB.oute(w+2), q_line - 1))
                                            count += 1
                                            if q_line - 2 == 0:
                                                self.tab[q_line - 2][w + 2] = QW
                                                print('Компьютер выиграл!')
                                                self.str_for_file+='X'
                                                self.winner = True
                                                print(self.tab)


                                    elif self.tab[q_line - 1][w - 1] == B and 1 <= w - 2 <= 8 and 0 <= q_line - 2 <= 7:
                                        if  self.tab[q_line-2][w-2]==B:
                                                self.tab[q_line][w]=W
                                        else:
                                            self.tab[q_line][w] = A
                                            self.tab[q_line - 1][w - 1] = A
                                            self.tab[q_line - 2][w - 2] = W
                                            self.str_for_file += ('{}{}:{}{}'.format(ComputerB.oute(w), q_line+1,ComputerB.oute(w-2), q_line - 1))
                                            count += 1
                                            if q_line - 2 == 0:
                                                self.tab[q_line - 2][w - 2] = QW
                                                print('Компьютер выиграл!')
                                                self.str_for_file+='X'
                                                self.winner = True
                                                print(self.tab)

                                    else:
                                        if self.tab[q_line - 1][w + 1] == A and 1 <= w + 1 <= 8 and 0 <= q_line - 1 <= 7:
                                            self.tab[q_line][w] = A
                                            self.tab[q_line - 1][w + 1] = W
                                            self.str_for_file += ('{}{}-{}{}'.format(ComputerB.oute(w), q_line + 1,ComputerB.oute(w+1), q_line))
                                            count += 1
                                            if q_line - 1 == 0:
                                                self.tab[q_line - 1][w + 1] = QW
                                                print('Компьютер выиграл!')
                                                self.str_for_file+='X'
                                                self.winner = True
                                                print(self.tab)

                                        elif self.tab[q_line - 1][w - 1] == A and 1 <= w - 1 <= 8 and 0 <= q_line - 1 <= 7:
                                            self.tab[q_line][w] = A
                                            self.tab[q_line - 1][w - 1] = W
                                            self.str_for_file += ('{}{}-{}{}'.format(ComputerB.oute(w), q_line+1,ComputerB.oute(w-1), q_line))
                                            count += 1
                                            if q_line - 1 == 0:
                                                self.tab[q_line - 1][w - 1] = QW
                                                print('Компьютер выиграл!')
                                                self.str_for_file+='X'
                                                self.winner = True
                                                print(self.tab)


            print('       A   B   C   D   E   F   G   H')
            print(self.tab)
            print(self.str_for_file)
            file=open("shashki.txt","a")
            file.write(self.str_for_file+'\n')
            file.close()
            return self.winner


    out2 = 0
    q_line = 0
    place2 = 0
    file=open("shashki.txt","w")
    file.write('Приветсвую Вас! Здесь будут отображаться все ходы при игре в шашки!\n')
    file.close()
    count_xod=1
    while True:
        str_for_file =('{}'.format(count_xod)+'.')
        A = Black(table,str_for_file)
        A.tab
        outt = input('Введите  столбец, в котором находится ваша шашка:')
        out2 = int(input('Введите строку, в которой находится ваша шашка:'))
        place1 = input('Введите  столбец, в который хотите передвинуть шашку:')
        place2 = int(input('Введите строку, в которую хотите передвинуть шашку:'))

        print('       A   B   C   D   E   F   G   H')
        print(A.chip(out2 - 1, Black.out(outt), place2 - 1, Black.out(place1)))
        if place2 == 8:
            break
        T = ComputerB(table,A.str_for_file)

        T.tab
        w = outt
        q_line = out2
        r_line = place2
        e = place1
        print('       A   B   C   D   E   F   G   H')

        if T.choice(q_line, ComputerB.oute(w)) == True:
            break
        count_xod+=1
    pass
if a == 2:
    print('Ваш цвет-белый!')
    B = 'Ч'
    W = 'Б'
    A = '+'
    Y = ' '
    QW = 'ДБ'
    QB = ' ДЧ'

    table = num.array([[1, W, Y, W, Y, W, Y, W, Y],
                       [2, Y, W, Y, W, Y, A, Y, A],
                       [3, A, Y, B, Y, A, Y, B, Y],
                       [4, Y, B, Y, A, Y, A, Y, A],
                       [5, A, Y, A, Y, A, Y, A, Y],
                       [6, Y, A, Y, A, Y, A, Y, A],
                       [7, A, Y, A, Y, B, Y, A, Y],
                       [8, Y, A, Y, B, Y, A, Y, A]])

    print('       A   B   C   D   E   F   G   H')
    print(table)


    class White: #создаем класс для белых шашек
        def __init__(self, tab,str_for_file):
            self.tab = tab
            self.count_xod = 1
            self.str_for_file = str_for_file

        def out(out1):
            d = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
                 "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
            if out1 in d:
                return d[out1]
            else:
                print('Ошибка')

        def chip(self, a_line, b, c_line, d):
            B = 'Ч'
            W = 'Б'
            A = '+'
            Y = ' '
            QW = 'ДБ'
            QB = 'ДЧ'
            if self.tab[a_line][b] == W:
                if 0 <= b <= 8:
                    self.tab[a_line][b] = A
                    if 0 <= d <= 8:
                        if self.tab[c_line][d] == A:
                            if b < d:
                                if self.tab[c_line - 1][d - 1] == B:
                                    self.tab[c_line - 1][d - 1] = A
                                    self.tab[c_line][d] = W
                                    self.str_for_file += ('{}{}:{}{}'.format(outt, out2, place1, place2))
                                else:
                                    self.tab[c_line][d] = W
                                    self.str_for_file += ('{}{}-{}{}'.format(outt, out2, place1, place2))
                            elif b > d:
                                if self.tab[c_line - 1][d + 1] == B:
                                    self.tab[c_line - 1][d + 1] = A
                                    self.tab[c_line][d] = W
                                    self.str_for_file += ('{}{}:{}{}'.format(outt, out2, place1, place2))
                                else:
                                    self.tab[c_line][d] = W
                                    self.str_for_file += ('{}{}-{}{}'.format(outt, out2, place1, place2))
                            if c_line == 7:
                                self.tab[c_line][d] = QW
                                self.str_for_file+='X'
                                print('Ты выиграл!')
                                print(self.str_for_file)
                                file = open("shashki.txt", "a")
                                file.write(self.str_for_file)
                                file.close()
                        elif self.tab[c_line][d] == Y:
                            self.tab[a_line][b] = W
                            print('Ошибка! На пустые клетки  ходить нельзя!')
                        elif self.tab[c_line][d] == W:
                            self.tab[a_line][b] = W
                            print('Клетка занята, выберите другую!')
                        elif self.tab[c_line][d] == B:
                            self.tab[a_line][b] = W
                            print('Клетка занята, выберите другую!')
                        elif self.tab[c_line + 1][d - 1] == B and self.tab[c_line + 2][d - 2] == B:
                            self.tab[c_line][d] = W
                        elif self.tab[c_line + 1][d + 1] == B and self.tab[c_line + 2][d + 2] == B:
                            self.tab[c_line][d] = W
            elif self.tab[a_line][b] == B:
                print('Вы походили шашкой соперника. Это невозможно. Походите еще раз своей шашкой! ')
            self.str_for_file +=' '
            self.count_xod += 1
            return self.tab


    class ComputerW(White): # черные шашки(компьютер против пользователя)
        def __init__(self, tab, str_for_file):
            self.tab = tab
            self.str_for_file=str_for_file
        def oute(out1):
            d = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
                 "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
            dobr=dict((v,k) for k,v in d.items())
            if out1 in dobr:
                return dobr[out1]
            if out1 in d:
                return d[out1]
            else:
                return ('Ошибка')


        def choice(self, q_line, w): #ходы компьютера, играющего за черные шашки
            B = 'Ч'
            W = 'Б'
            A = '+'
            Y = ' '
            QW = 'ДБ'
            QB = 'ДЧ'
            count_black=0
            count_white=0
            count = 0
            self.winner = False
            flag = True
            if 1 <= w <= 8 and 0 <= q_line <= 7:
                for w in range(1,8):
                    for q_line in range(8):
                        if self.tab[q_line][w]==B:
                            count_black+=1
                        elif self.tab[q_line][w]==W:
                            count_white+=1
                if count_black==0:
                    print('Игра закончилась, ты выиграл!')
                    self.str_for_file+='X'
                    file=open("shashki.txt",'a')
                    file.write(self.str_for_file)
                    file.close()
                    sys.exit()
                elif count_white==0:
                    print('Игра закончилась, компьютер выиграл!')
                    self.str_for_file += 'X'
                    file = open("shashki.txt", 'a')
                    file.write(self.str_for_file)
                    file.close()
                    sys.exit()


                for w in range(1, 8):
                    if flag == False:
                        break
                    else:
                        for q_line in range(8):
                            if flag == False:
                                break
                            else:
                                if self.tab[q_line][w] == B:
                                    flag = False
                                    if self.tab[q_line - 1][w + 1] == W and 1 <= w + 2 <= 8 and 0 <= q_line - 2 <= 7:
                                        if self.tab[q_line - 2][w + 2] == W:
                                            self.tab[q_line][w] = B
                                        else:
                                            self.tab[q_line][w] = A
                                            self.tab[q_line - 1][w + 1] = A
                                            self.tab[q_line - 2][w + 2] = B
                                            self.str_for_file += ('{}{}:{}{}'.format(ComputerW.oute(w), q_line+1,ComputerW.oute(w+2), q_line - 1))
                                            count += 1
                                            if q_line - 2 == 0:
                                                self.tab[q_line - 2][w + 2] = QB
                                                print('Компьютер выиграл!')
                                                self.str_for_file+='X'
                                                self.winner = True
                                                print(self.tab)


                                    elif self.tab[q_line - 1][w - 1] == W and 1 <= w - 2 <= 8 and 0 <= q_line - 2 <= 7:
                                        if  self.tab[q_line-2][w-2]==W:
                                                self.tab[q_line][w]=B
                                        else:
                                            self.tab[q_line][w] = A
                                            self.tab[q_line - 1][w - 1] = A
                                            self.tab[q_line - 2][w - 2] = B
                                            self.str_for_file += ('{}{}:{}{}'.format(ComputerW.oute(w), q_line+1,ComputerW.oute(w-2), q_line - 1))
                                            count += 1
                                            if q_line - 2 == 0:
                                                self.tab[q_line - 2][w - 2] = QB
                                                print('Компьютер выиграл!')
                                                self.str_for_file+='X'
                                                self.winner = True
                                                print(self.tab)

                                    else:
                                        if self.tab[q_line - 1][w + 1] == A and 1 <= w + 1 <= 8 and 0 <= q_line - 1 <= 7:
                                            self.tab[q_line][w] = A
                                            self.tab[q_line - 1][w + 1] = B
                                            self.str_for_file += ('{}{}-{}{}'.format(ComputerW.oute(w), q_line + 1,ComputerW.oute(w+1), q_line))
                                            count += 1
                                            if q_line - 1 == 0:
                                                self.tab[q_line - 1][w + 1] = QB
                                                print('Компьютер выиграл!')
                                                self.str_for_file+='X'
                                                self.winner = True
                                                print(self.tab)

                                        elif self.tab[q_line - 1][w - 1] == A and 1 <= w - 1 <= 8 and 0 <= q_line - 1 <= 7:
                                            self.tab[q_line][w] = A
                                            self.tab[q_line - 1][w - 1] = B
                                            self.str_for_file += ('{}{}-{}{}'.format(ComputerW.oute(w), q_line+1,ComputerW.oute(w-1), q_line))
                                            count += 1
                                            if q_line - 1 == 0:
                                                self.tab[q_line - 1][w - 1] = QB
                                                print('Компьютер выиграл!')
                                                self.str_for_file+='X'
                                                self.winner = True
                                                print(self.tab)


            print('       A   B   C   D   E   F   G   H')
            print(self.tab)
            print(self.str_for_file)
            file=open("shashki.txt","a")
            file.write(self.str_for_file+'\n')
            file.close()
            return self.winner


    out2 = 0
    q_line = 0
    place2 = 0
    file=open("shashki.txt","w")
    file.write('Приветсвую Вас! Здесь будут отображаться все ходы при игре в шашки!\n')
    file.close()
    count_xod=1
    while True:
        str_for_file =('{}'.format(count_xod)+'.')
        A = White(table,str_for_file)
        A.tab
        outt = input('Введите  столбец, в котором находится ваша шашка:')
        out2 = int(input('Введите строку, в которой находится ваша шашка:'))
        place1 = input('Введите  столбец, в который хотите передвинуть шашку:')
        place2 = int(input('Введите строку, в которую хотите передвинуть шашку:'))

        print('       A   B   C   D   E   F   G   H')
        print(A.chip(out2 - 1, White.out(outt), place2 - 1, White.out(place1)))
        if place2 == 8:
            break
        T = ComputerW(table,A.str_for_file)

        T.tab
        w = outt
        q_line = out2
        r_line = place2
        e = place1
        print('       A   B   C   D   E   F   G   H')

        if T.choice(q_line, ComputerW.oute(w)) == True:
            break
        count_xod+=1
    pass

