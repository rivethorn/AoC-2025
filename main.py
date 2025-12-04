import sys


def main() -> None:
    print("=== Advent of Code 2025 ===")

    if len(sys.argv) > 1:
        match sys.argv[1]:
            case "1":
                from days import day01

                day01.part1()
                day01.part2()
            case "2":
                from days import day02

                day02.part1()
                day02.part2()
            case "3":
                from days import day03

                day03.part1()
                day03.part2()
            case _:
                print("Please enter a correct day")
    else:
        print("Please enter the day")


if __name__ == "__main__":
    main()
