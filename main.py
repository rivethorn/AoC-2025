import sys
import logging
import time

logging.basicConfig(
    format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main() -> None:
    print("=== Advent of Code 2025 ===")
    print("———————————————————————————")

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
            case "4":
                from days import day04

                day04.part1()
                day04.part2()
            case "5":
                from days import day05

                day05.part1()
                day05.part2()
            case _:
                print("Please enter a correct day")
    else:
        print("Please enter the day")


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print("———————————————————————————")
    logger.info("Execution time: %0.4f seconds", t2 - t1)
