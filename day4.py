#!/bin/env python3

"""day4.py - Advent of Code 2025 - Day 4."""

from util import *


def parse(input):
    return list(map(list, input))


TEST = parse(open("test/4.txt", "r").readlines())
INPUT = parse(open("input/4.txt", "r").readlines())

ROLL = "@"
EMPTY = "."


def is_accessible(grid, coord):
    if at(grid, coord) == ROLL:
        count = 0
        for adj in adjacent(coord, grid):
            if at(grid, adj) == ROLL:
                count += 1
        return count < 4


def count_accessible_rolls(grid):
    count = 0
    for coord in coords(grid):
        if is_accessible(grid, coord):
            count += 1
    return count


def part1(input):
    return count_accessible_rolls(input)


def remove_accessible_rolls(grid):
    count = 0
    for coord in coords(grid):
        if is_accessible(grid, coord):
            count += 1
            grid_set(grid, coord, EMPTY)
    return count


def part2(input):
    removed = 0
    while True:
        new = remove_accessible_rolls(input)
        removed += new
        if new == 0:
            return removed


print("part 1:", part1(INPUT))
print("part 2:", part2(INPUT))
