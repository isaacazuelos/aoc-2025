#!/bin/env python3

"""day4.py - Advent of Code 2025 - Day 4."""


def parse(input):
    return list(map(list, input))


TEST = parse(open("test/4.txt", "r").readlines())
INPUT = parse(open("input/4.txt", "r").readlines())


def coords(grid):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            yield (x, y)


def adjacent(coord, grid):
    (x, y) = coord
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (
                x + dx >= 0
                and y + dy >= 0
                and x + dx < len(grid[0])
                and y + dy < len(grid)
                and not (dx == 0 and dy == 0)
            ):
                yield (x + dx, y + dy)


def count_accessible_rolls(grid):
    total = 0
    for cell in coords(grid):
        (x, y) = cell
        if grid[y][x] == "@":
            count = 0
            for adj in adjacent(cell, grid):
                (x, y) = adj
                if grid[y][x] == "@":
                    count += 1
            if count < 4:
                total += 1
    return total


def part1(input):
    return count_accessible_rolls(input)


def part2(input):
    pass


print("part 1:", part1(INPUT))
# print("part 2:", part2(TEST))
