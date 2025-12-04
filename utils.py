def read_lines(num: str):
    with open(f"inputs/day{num}.txt") as f:
        return f.read().strip().split()
