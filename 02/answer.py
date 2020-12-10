def verify_password(line: str, version: int = 1) -> bool:
    policy, password = [item.strip() for item in line.split(':')]
    bounds = policy[:-2]
    letter = policy[-1]
    low, high = [int(item) for item in bounds.split('-')]

    if version == 1:
        letter_count = password.count(letter)
        if low <= letter_count <= high:
            return True
    elif version == 2:
        letters = [password[low-1], password[high-1]]
        if letters.count(letter) == 1:
            return True
    return False

def count_good_passwords(data: list, version: int = 1) -> int:
    good_passwords = 0
    for line in data:
        if verify_password(line, version):
            good_passwords += 1
    print(f'Number of good password: {good_passwords}')
    return good_passwords

if __name__ == "__main__":
    data = []
    with open('passwords.txt') as f:
        for line in f:
            data.append(line.strip())

    count_good_passwords(data, version=2)