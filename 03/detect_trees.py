
def detect_trees(data: list, right: int = 3, down: int = 1) -> int:
    pos = 0
    trees = 0
    first_row = True
    for line in data[::down]:
        line = line * 100

        if pos != 0:
            char = line[:pos][-1]

        if first_row:
            pos += right+1
            first_row = False
            continue
        else:
            pos += right

        if char == "#":
            trees += 1

    print(f"Number of trees: {trees}")
    return trees

def multiply_slopes(data: list) -> int:
    first = detect_trees(data, right=1, down=1)
    second = detect_trees(data, right=3, down=1)
    third = detect_trees(data, right=5, down=1)
    fourth = detect_trees(data, right=7, down=1)
    fifth = detect_trees(data, right=1, down=2)
    multiplied = first * second * third * fourth * fifth
    print(f'Slopes multiplied: {multiplied}')
    return multiplied

if __name__ == "__main__":
    data = """..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"""

    x = [i.strip() for i in data.split('\n')]

    data = []
    with open('input.txt') as f:
        for line in f:
            data.append(line.strip())
    multiply_slopes(data)
