def parse_data():
    with open("inputs/day05.txt") as f:
        lines = f.read().strip()

    ranges, ids = lines.split("\n\n")
    ranges = [list(map(int, line.split("-"))) for line in ranges.splitlines()]
    ids = list(map(int, ids.splitlines()))

    return ranges, ids


def part1() -> None:
    ranges, ids = parse_data()

    fresh_ids = [
        id for id in ids if any(id >= start and id <= end for start, end in ranges)
    ]

    print(f"{len(fresh_ids)} ingredients are fresh.")


def part2() -> None:
    ranges, _ = parse_data()

    ranges.sort()
    stack = []
    stack.append(ranges[0])

    for r in ranges[1:]:
        if stack[-1][0] <= r[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], r[-1])
        else:
            stack.append(r)

    fresh_ids = sum(end - start + 1 for start, end in stack)

    print(f"{fresh_ids} ingredient IDs are fresh.")
