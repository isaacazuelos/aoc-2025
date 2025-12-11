#!/bin/env python3

"""day10.py - Advent of Code 2025 - Day 11."""


def parse(input):
    graph = {}
    for row in input:
        (name, rest) = row.split(": ")
        graph[name] = set(rest.split(" "))

    return graph


# Just confirming we need to care about this.
#
# def are_there_loops():
#     seen = set("you")
#     frontier = set("you")
#     while frontier:
#         name = frontier.pop()
#         if name in seen:
#             print("loop found")
#             return
#         frontier.update(INPUT[name])
#         seen.add(name)
#
# are_there_loops()

TEST = parse(open("test/11.txt", "r").readlines())
INPUT = parse(open("input/11.txt", "r").readlines())


def part1(input):
    pass


print("part 1:", part1(TEST))


def part2(input):
    pass


print("part 2:", part2(TEST))
