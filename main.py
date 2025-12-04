import sys


def main():
    print("=== Advent of Code 2025 ===")

    if len(sys.argv) > 1:
        match sys.argv[1]:
            case "1":
                from days import day1

                day1.part1()
                day1.part2()
            case _:
                print("Please enter a correct day")
    else:
        print("Please enter the day")


if __name__ == "__main__":
    main()
