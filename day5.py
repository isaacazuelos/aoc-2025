#!/bin/env python3

"""day5.py - Advent of Code 2025 - Day 5."""

from util import *


def parse(input: str):
    [fresh, available] = input.split("\n\n")

    ranges = []
    for r in fresh.splitlines():
        [start, end] = r.split("-")
        ranges.append((int(start), int(end)))

    ids = []
    for id in available.splitlines():
        ids.append(int(id))

    return (ranges, ids)


TEST = parse(open("test/5.txt", "r").read())
INPUT = parse(open("input/5.txt", "r").read())


def is_fresh(ranges, id):
    for r in ranges:
        if range_contains(r, id):
            return True
    return False


def part1(input):
    (ranges, ids) = input
    return sum(int(is_fresh(ranges, id)) for id in ids)


print("part 1:", part1(INPUT))


def merge_overlapping(ranges):
    # kind of nasty way of doing iterator invalidation, we replace both values
    # with the merged one, then dedup at the end. This means we end up checking
    # some ranges a whole lot of times, but at least this comparison is quick.
    for i1 in range(len(ranges)):
        for i2 in range(len(ranges)):
            r1 = ranges[i1]
            r2 = ranges[i2]
            if range_overlap(r1, r2):
                r3 = range_merge(r1, r2)
                ranges[i1] = r3
                ranges[i2] = r3

    return list(set(ranges))


def part2(input):
    (ranges, _) = input
    return sum((end - start + 1) for (start, end) in merge_overlapping(ranges))


print("part 2:", part2(INPUT))
