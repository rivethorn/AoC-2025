from __future__ import annotations
from typing import Any, Generator, NamedTuple

from utils import read_lines


class Point(NamedTuple):
    x: int
    y: int

    def yield_neighbors(self) -> Generator[Point, Any, None]:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                yield Point(self.x + dx, self.y + dy)


class ForkliftGrid:
    def __init__(self, grid_array: list) -> None:
        self.array = [list(row) for row in grid_array]
        self._width: int = len(self.array[0])
        self._height: int = len(self.array)

    def all_points(self) -> list[Point]:
        points: list[Point] = [
            Point(x, y) for x in range(self._width) for y in range(self._height)
        ]
        return points

    def val(self, point: Point):
        return self.array[point.y][point.x]

    def set_val(self, point: Point, value) -> None:
        self.array[point.y][point.x] = value

    def is_valid(self, point: Point) -> bool:
        if 0 <= point.x < self._width and 0 <= point.y < self._height:
            return True
        return False


def get_locations(grid: ForkliftGrid):
    accessible = []

    for point in grid.all_points():
        if grid.val(point) == "@":
            rolls = 0
            for neighbor in point.yield_neighbors():
                if grid.is_valid(neighbor):
                    if grid.val(neighbor) == "@":
                        rolls += 1
            if rolls < 4:
                accessible.append(point)

    return accessible


def part1() -> None:
    lines: list[str] = read_lines("04")

    grid = ForkliftGrid(lines)

    accessible = get_locations(grid)

    print(f"{len(accessible)} rolls can be picked")


def part2() -> None:
    lines: list[str] = read_lines("04")

    grid = ForkliftGrid(lines)

    rolls_removed = 0

    while True:
        accessible = get_locations(grid)
        if not accessible:
            break
        for loc in accessible:
            grid.set_val(loc, "X")
            rolls_removed += 1

    print(f"{rolls_removed} rolls were removed.")
