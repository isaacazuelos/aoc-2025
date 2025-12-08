def at(grid, coord):
    (x, y) = coord
    return grid[y][x]


def grid_set(grid, coord, value):
    (x, y) = coord
    old = grid[y][x]
    grid[y][x] = value
    return old


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


def show_grid(grid):
    for r in grid:
        for c in r:
            print(c, end=" ")
        print("")


def range_contains(range, value):
    (start, end) = range
    return start <= value and value <= end


def range_overlap(r1, r2):
    (s1, e1) = r1
    (s2, e2) = r2
    return range_contains(r1, s2) or range_contains(r2, s1)


def range_merge(r1, r2):
    (s1, e1) = r1
    (s2, e2) = r2
    return (min(s1, s2), max(e1, e2))


def product(nums):
    p = 1
    for n in nums:
        p *= n
    return p


def transpose(grid):
    return list(map(list, zip(*grid)))
