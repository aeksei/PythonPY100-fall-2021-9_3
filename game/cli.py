from random import randint
from typing import Tuple

from logic import init_field, is_empty_ceil, set_ceil, is_win, is_available_ceil


def print_field(field: list):
    for row in field:
        for ceil in row:
            print(ceil, end=" ")
        print()


def get_step(field: list, player_symbol: str):
    size = 3  # размер поля
    while True:
        coord_str = input(f"Игрок {player_symbol} введите координату от 1 до {size * size}: ")

        if not coord_str.isdigit():
            print("Вы ввели не число. Повторите ввод")
            continue

        coord = int(coord_str)
        if not 1 <= coord <= size * size:
            print("Вы ввели неверную координату. Повторите ввод")
            continue

        x, y = single_to_double_coord(coord, size)
        if not is_empty_ceil(field, x, y):
            print("Ячейка занята. Повторите ввод")
            continue

        return x, y


def single_to_double_coord(coord: int, size: int) -> Tuple[int, int]:
    coord = coord - 1
    row_index = coord // size
    col_index = coord % size

    return row_index, col_index


def first_player_step(field, player_symbol):
    x, y = get_step(field, player_symbol)
    set_ceil(field, x, y, player_symbol)
    print_field(field)


def second_player_step(field, player_symbol):
    first_player_step(field, player_symbol)
    # size = 3
    # print("Ходит компьютер ...")
    # while True:
    #     random_ceil_index = randint(1, size * size)
    #     x, y = single_to_double_coord(random_ceil_index, size)
    #     if is_empty_ceil(field, x, y):
    #         set_ceil(field, x, y, player_symbol)
    #         break
    # print_field(field)


def is_win_cli(field, player_symbol) -> bool:
    if is_win(field):
        print(f"Выиграл игрок {player_symbol}!!!")
        return True

    return False


def main():
    field = init_field()
    print_field(field)

    first_player, second_player = "X", "O"

    while True:
        first_player_step(field, first_player)

        if is_win_cli(field, first_player):
            break

        if not is_available_ceil(field):
            print("Ходы закончились. Ничья")
            break

        second_player_step(field, second_player)

        if is_win_cli(field, second_player):
            break

        if not is_available_ceil(field):
            print("Ходы закончились. Ничья")
            break


if __name__ == '__main__':
    main()
