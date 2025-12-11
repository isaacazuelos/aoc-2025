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


def max_joltage(bank, n=2):

    def inner(b, n, digits):
        if n == 1:
            digits.append(max(b))
            return digits

        d = max(b[: -n + 1])  # we must leave digits
        i = b.index(d)

        digits.append(d)
        return inner(b[i + 1 :], n - 1, digits)

    digits = inner(bank, n, [])

    product = 0
    for p, d in enumerate(reversed(digits)):
        product += d * (10**p)
    return product


def part1(input):
    return sum(max_joltage(b) for b in input)


def part2(input):
    return sum(max_joltage(b, 12) for b in input)


print("part 1:", part1(INPUT))
print("part 2:", part2(INPUT))
