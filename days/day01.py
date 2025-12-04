from utils import read_lines


def sign(num: int) -> int:
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


def part1() -> None:
    print("Day 1, Part 1")
    position: int = 50
    password: int = 0

    lines = read_lines("01")
    for line in lines:
        rotation: int = int(line.replace("L", "-").replace("R", ""))
        position = (position + rotation) % 100

        password += 1 if position == 0 else 0

    print(f"The password is: {password}")


def part2() -> None:
    print("Day 1, Part 2")
    position: int = 50
    password: int = 0

    lines = read_lines("01")
    for line in lines:
        rotation: int = int(line.replace("L", "-").replace("R", ""))
        direction: int = sign(rotation)

        password += int(((direction * rotation) + ((direction * position) % 100)) / 100)
        position = (position + rotation) % 100

    print(f"The password is: {password}")
