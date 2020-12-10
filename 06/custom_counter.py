
def process(answers):
    total = len(set(list(answers)))
    print(f'{answers=} - {total=}')
    return total


def get_answer_count(data):
    lines = [line.strip() for line in data.split('\n')] + ['']
    count = 0
    s = ''
    for line in lines:
        if line == '':
            count += process(s)
            s = ''
        s += line
    print(f'Total answers: {count}')

if __name__ == '__main__':
    data = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    with open('input.txt') as f:
        data = f.read()
    get_answer_count(data)