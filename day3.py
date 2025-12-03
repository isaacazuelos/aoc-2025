#!/bin/env python3

"""day3.py - Advent of Code 2025 - Day 3."""


def parse(input):
    banks = []
    for b in input:
        bank = []
        for d in b.strip():
            bank.append(int(d))
        banks.append(bank)
    return banks


TEST = parse(open("test/3.txt", "r").readlines())
INPUT = parse(open("input/3.txt", "r").readlines())


def max_joltage_2(bank):
    first = max(bank[:-1])  # we can't use the last digit twice
    first_i = bank.index(first)
    second = max(bank[first_i + 1 :])

    return int(first * 10 + second)


def max_joltage(bank, n=2):

    def inner(bank, n, digits=[]):
        if n == 1:
            return max(bank)

        d = max(bank[: -(n - 1)])  # we must leave digits
        i = bank.index(first)

    digits = []
    first = max(bank[: -(n - 1)])

    product = 1
    for p, d in enumerate(reversed(digits)):
        product += d * (10**p)

    return product


def part1(input):
    return sum((max_joltage(b) for b in input))


def part2(input):
    return [max_joltage(b, n=12) for b in input]


print("part 1:", part1(INPUT))
print("part 2:", part2(TEST))
