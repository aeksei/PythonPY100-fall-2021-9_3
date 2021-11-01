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


def main():
    field = init_field()
    print_field(field)

    first_player, second_player = "X", "O"

    while True:
        x, y = get_step(field, first_player)
        set_ceil(field, x, y, first_player)
        print_field(field)

        if is_win(field):
            print(f"Выиграл игрок {first_player}")
            break

        if not is_available_ceil(field):
            print("Ходы закончились. Ничья")
            break

        x, y = get_step(field, second_player)
        set_ceil(field, x, y, second_player)
        print_field(field)

        if is_win(field):
            print(f"Выиграл игрок {second_player}")
            break

        if not is_available_ceil(field):
            print("Ходы закончились. Ничья")
            break





if __name__ == '__main__':
    main()
