def is_double_sequence(s: str) -> bool:
    half = len(s) // 2
    return len(s) % 2 == 0 and s[:half] == s[half:]


def is_invalid_id(s: str) -> bool:
    n = len(s)
    for size in range(1, n // 2 + 1):
        if n % size != 0:
            continue
        if s == s[:size] * (n // size):
            return True
    return False


def load_ranges() -> list[tuple[int, ...]]:
    with open("inputs/day02.txt") as f:
        return [tuple(map(int, r.split("-"))) for r in f.read().strip().split(",")]


def part1() -> None:
    total = 0

    for lower, higher in load_ranges():
        for x in range(lower, higher):
            if is_double_sequence(str(x)):
                total += x

    print(f"The sum of part 1 is: {total}")


def part2() -> None:
    total = 0

    for lower, higher in load_ranges():
        for x in range(lower, higher):
            if is_invalid_id(str(x)):
                total += x

    print(f"The sum of part 2 is: {total}")
