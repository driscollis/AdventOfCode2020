def find_seat_id(identifier):
    row_identifier = identifier[:7]
    col_identifier= identifier[7:]
    row_identifier = row_identifier.replace('F', '0')
    row_identifier = row_identifier.replace('B', '1')
    col_identifier = col_identifier.replace('R', '1')
    col_identifier = col_identifier.replace('L', '0')

    row = int(row_identifier, 2)
    col = int(col_identifier, 2)
    seat_id = row * 8 + col
    print(f'{identifier}={row_identifier}-{col_identifier}: row {row}, col {col}, seat ID {seat_id}')

    return seat_id, row, col

def find_highest_seat():
    highest = 0
    with open('input.txt') as f:
        for line in f:
            seat_id = find_seat_id(line.strip())
            if seat_id > highest:
                highest = seat_id, _, _
    print(f'Highest seat ID = {highest}')

def find_missing_seats():
    seats = {}
    with open('input.txt') as f:
        for line in f:
            seat_id, row, col = find_seat_id(line.strip())
            if row not in seats:
                seats[row] = [col]
            else:
                seats[row].append(col)
    keys = list(seats.keys())
    keys.sort()
    for key in keys:
        if len(seats[key]) < 8:
            print(f'Row {key}, Col {seats[key]}')
    print()

def convert_bin_to_seat_id(row, col):
    c_row = bin(row)[2:].zfill(7)
    c_col = bin(col)[2:].zfill(3)
    c_row = c_row.replace('0', 'F')
    c_row = c_row.replace('1', 'B')
    c_col = c_col.replace('1', 'R')
    c_col = c_col.replace('0', 'L')
    print(f'{row=}, {col=} => {c_row}{c_col}')

if __name__ == '__main__':
    identifier = 'FFFBBBFRRR'
    _, row, col = find_seat_id(identifier)
    convert_bin_to_seat_id(122, 7)
    find_missing_seats()