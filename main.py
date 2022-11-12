#Прикрутить бота к игре ""Крестики-нолики""

# Игра "Крестики-нолики".
#  площадка 3 X 3.

desk = list(map(str, range(1, 10)))


def desk_redraw():
    print('*' * 20)
    for i in range(3):
        for j in range(3):
            print(f"{desk[i * 3 + j]:^5}", end=" ")
        print(f"\n{'*' * 20}")
    print()


def put_figure_on_desk(cur_figure):
    global desk
    while True:
        cur_str = input(f"Введите число 1 to 9.\nВыберите позицию {cur_figure}? ")
        if cur_str.isdigit() and int(cur_str) in range(1, 10):
            cur_pos = int(cur_str)
            pos = desk[cur_pos - 1]
            if pos not in (chr(10060), chr(11093)):
                desk[cur_pos - 1] = chr(10060) if cur_figure == "X" else chr(11093)
                break
            else:
                print(f"Эта ячейка уже занята{chr(9995)}{chr(129292)}")
        else:
            print(f"Неверный ввод{chr(9940)}. Введите допустимое число.")


def define_winner():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    n = [desk[x[0]] for x in win_coord if desk[x[0]] == desk[x[1]] == desk[x[2]]]
    return n[0] if n else n


def main():
    i = 0
    desk_redraw()
    while True:
        put_figure_on_desk("O") if i % 2 else put_figure_on_desk("X")
        desk_redraw()

        if i > 3:
            if define_winner():
                print(f"{define_winner()} - Вы победили!")
                break
        if i == 8:
            print(f"Ничья!")
            break
        i += 1

main()
