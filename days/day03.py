from utils import read_lines


def part1() -> None:
    total = 0

    lines: list[str] = read_lines("03")
    for line in lines:
        i = max(enumerate(line[:-1]), key=lambda x: x[1])[0]
        j = max(enumerate(line[i + 1 :]), key=lambda x: x[1])[0] + i + 1

        total += int(line[i] + line[j])

    print(f"Total output: {total}")


def part2() -> None:
    total = 0

    def rejolt(line, many=0):
        if many > 0:
            i = max(enumerate(line[:-many]), key=lambda x: x[1])[0]
            return line[i] + rejolt(line[i + 1 :], many=many - 1)
        else:
            return max(line)

    lines = read_lines("03")
    for line in lines:
        total += int(rejolt(line, 11))

    print(f"Total 12 battery output: {total}")
