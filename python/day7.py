#!/bin/env python3

"""day7.py - Advent of Code 2025 - Day 7."""

from util import *

EMITTER = "S"
EMPTY = "."
SPLITTER = "^"
BEAM = "0"


def parse(input):
    return list(map(lambda r: list(r[:-1]), input))


TEST = parse(open("test/7.txt", "r").readlines())
INPUT = parse(open("input/7.txt", "r").readlines())


def mark_beams(grid):
    for y in range(len(grid) - 1):
        for x in range(len(grid[y])):
            if grid[y][x] == EMITTER or grid[y][x] == BEAM:
                if grid[y + 1][x] == EMPTY:
                    grid[y + 1][x] = BEAM
                if grid[y + 1][x] == SPLITTER:
                    grid[y + 1][x + 1] = BEAM
                    grid[y + 1][x - 1] = BEAM


def sim(grid, x):
    # This works, but the recurrence relation is awful, something like 2^n for
    # each splitter, where that O(n^2) on grid size, so yikes.
    if not grid:
        return 1
    elif grid[0][x] == SPLITTER:
        return sim(grid[1:], x - 1) + sim(grid[1:], x + 1)
    else:
        return sim(grid[1:], x)


def is_beam(a):
    return isinstance(a, int)


def count_paths(grid):
    mark_beams(grid)

    # Set the beams to 0 so they're ints we can add to.
    for c in coords(grid):
        if at(grid, c) == BEAM:
            grid_set(grid, c, 0)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == EMITTER:
                grid[y + 1][x] = 1

            above = grid[y - 1][x]
            if grid[y][x] == SPLITTER and is_beam(above):

                grid[y][x + 1] += above
                grid[y][x - 1] += above

            if is_beam(grid[y][x]) and is_beam(grid[y - 1][x]):
                grid[y][x] += grid[y - 1][x]


def part1(grid):
    mark_beams(grid)
    t = 0
    for y in range(len(grid) - 1):
        for x in range(len(grid[y])):
            if grid[y][x] == SPLITTER and grid[y - 1][x] == BEAM:
                t += 1
    show_grid(grid)
    return t


print("part 1:", part1(INPUT))


def part2(grid):
    count_paths(grid)
    t = 0
    for c in grid[-1]:
        if is_beam(c):
            t += c
    show_grid(grid)
    return t


print("part 2:", part2(INPUT))
