#!/bin/env python3

"""day6.py - Advent of Code 2025 - Day 6."""


TEST = open("test/6.txt", "r").readlines()
INPUT = open("input/6.txt", "r").readlines()


def product(nums):
    p = 1
    for n in nums:
        p *= n
    return p


def transpose(grid):
    return list(map(list, zip(*grid)))


def parse1(input):
    grid = []
    for line in input[:-1]:
        row = []
        for n in line.split():
            row.append(int(n))
        grid.append(row)

    ops = list(input[-1].split())
    grid = transpose(grid)
    return grid, ops


def parse2(input):
    ops = list(reversed(input[-1].split()))
    grid = list(map(lambda s: list(s[:-1]), input[:-1]))

    grid = list(map(reversed, grid))
    grid = transpose(list(grid))
    grid = list(map(concat, grid))

    new = [[]]
    for n in grid:
        if n.isspace():
            new.append([])
        else:
            new[-1].append(int(n))

    return new, ops


def math(ops, rows):
    acc = 0
    for op, row in zip(ops, rows):
        if op == "*":
            acc += product(row)
        else:
            acc += sum(row)
    return acc


def concat(strings):
    acc = ""
    for s in strings:
        acc += s
    return acc


def part1(input):
    (grid, ops) = parse1(input)
    return math(ops, grid)


print("part 1:", part1(INPUT))


def part2(input):
    (grid, ops) = parse2(input)
    return math(ops, grid)


print("part 2:", part2(INPUT))
