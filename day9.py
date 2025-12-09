#!/bin/env python3

"""day9.py - Advent of Code 2025 - Day 9."""

from util import *


def parse(input):
    return [tuple(map(int, r.split(","))) for r in input]


TEST = parse(open("test/9.txt", "r").readlines())
INPUT = parse(open("input/9.txt", "r").readlines())


def area(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    length = abs(x1 - x2) + 1
    height = abs(y1 - y2) + 1
    return length * height


def candidates(points):
    for p1 in points:
        for p2 in points:
            if p1 != p2:
                yield (p1, p2)


def part1(points):
    return max(area(*box) for box in candidates(points))


print("part 1:", part1(TEST))


def boxes_by_area(points):
    areas = [(area(p1, p2), (p1, p2)) for (p1, p2) in candidates(points)]
    return [a[1] for a in sorted(areas, reverse=True)]


def box_to_points(box):
    """
    Turn our two-point box representation into a series of vertices like the
    shape. This also is implicitly closed by looping back to the first point.
    """
    (p1, p2) = box
    (x1, y1) = p1
    (x2, y2) = p2
    return [p1, (x1, y2), p2, (x2, y1)]


def point_in_polygon(point, polygon):
    """https://en.wikipedia.org/wiki/Point_in_polygon"""

    ray = (point, (0, point[1]))  # We cast our ray from the point straight left.

    intersections = 0
    for edge in polygon_edges(polygon):
        if rectilinear_line_segment_intersect(ray, edge):
            intersections += 1

    # odd means inside
    return (intersections % 2) == 1


def polygon_edges(points):
    last = points[0]
    for point in points[1:]:
        yield (last, point)

    # and it loops back around to close
    yield (points[-1], points[0])


def is_horizontal(s):
    return s[0][1] == s[1][1]


def is_vertical(s):
    return s[0][0] == s[1][0]


def rectilinear_line_segment_intersect(l1, l2):
    pass


def box_in_polygon(box, polygon):
    """
    A box (represented as two corners) in inside another polygon (vertex
    list) when each point is 'inside' and edge of the box is does not intersect
    an edge of the polygon.
    """
    box_points = box_to_points(box)

    for point in box_points:
        if not point_in_polygon(point, polygon):
            print(f"rejecting {box_points} because {point} not in polygon")
            return False

    for be in polygon_edges(box_points):
        for pe in polygon_edges(polygon):
            if rectilinear_line_segment_intersect(be, pe):
                print(f"rejecting {box_points} because {be} intersects {pe}")
                return False

    return True


def segments(points):
    """
    Use a vertex list to create a sequence of line segments that form the
    perimeter of the polygon.
    """
    last = points[0]
    for vertex in points[1:]:
        yield (last, vertex)


def part2(points):
    """
    if all points in a polygon are inside another polygon, and none of the edges
    intersect, then the first polygon is inside the other.


    If all points of a shape corners are inside and none of the shapes' edges
    intersect the box's edges, it's inside. Intersect here means non-parallel
    intersection, which we can cheat on a bit since the lines are all
    rectilinear.


    https://en.wikipedia.org/wiki/Intersection_(geometry)#Two_line_segments
    """

    # Area is cheap, so we find and sort by largest area, and then find the
    # first one that's inside (expensive), so we only need to consider one
    # to success, instead of every possible box to find the largest area.

    for box in boxes_by_area(points):
        print(f"considering {box} with area {area(*box)}")
        if box_in_polygon(box, points):
            # return area(*box)
            print(f"box {box} has area {area(*box)}")


print("part 2:", part2(TEST))
