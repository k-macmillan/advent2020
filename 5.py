

def main():
    with open('5_seat_ids.txt', 'r') as f:
        seat_strings = [line.rstrip('\n') for line in f]

    # Walk each seat string to get the seat id
    seats = sorted([get_seat_id(get_row(seat), get_column(seat)) for seat in seat_strings])
    print(f'Last seat: {seats[-1]}')

    # Find my seat
    for seat in range(seats[0], seats[-1]):
        if seat not in seats:
            print(f'My seat: {seat}')


def get_row(row_index: str) -> int:
    """
    Seat rows go from 0-127 and the character representation is for a binary search. Walked each of the characters
    added 2^power if it represented the upper half. Decrement power every character.

    :param row_index: 10 character string representing seat location
    :return: row of this seat
    """
    total = 0
    power = 6
    for direction in row_index[:-3]:
        if direction == 'B':
            total += 2**power
        power -= 1
    return total


def get_column(row_index: str) -> int:
    """
    Seat columns go from 0-7 and the character representation is for a binary search. Walked each of the characters
    added 2^power if it represented the upper half. Decrement power every character.

    :param row_index: 10 character string representing seat location
    :return: column of this seat
    """
    total = 0
    power = 2
    for direction in row_index[7:]:
        if direction == 'R':
            total += 2**power
        power -= 1
    return total


def get_seat_id(row: int, col: int) -> int:
    """
    Identifies the specific seat id.

    :param row: Row of the seat
    :param col: Column of the seat
    :return: seat id
    """
    return row * 8 + col


if __name__ == '__main__':
    main()
