from __future__ import annotations

from collections import deque
from typing import Deque
from typing import NamedTuple

DIR = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]


class Point(NamedTuple):
    x: int
    y: int


def walk(
        maze: list[str],
        wall: str,
        curr: Point,
        end: Point,
        seen: list[list[bool]],
        path: Deque[Point],
) -> bool:
    print(curr)
    # Base Cases:
    # 1. off the map
    if ((curr.x < 0 or curr.x >= len(maze[0])) or
            (curr.y < 0 or curr.y >= len(maze))):
        return False

    # 2. on a wall
    if maze[curr.y][curr.x] == wall:
        return False

    # 3. is the end
    if curr.x == end.x and curr.y == end.y:
        path.append(end)
        return True

    # 4. seen
    if seen[curr.y][curr.x] is True:
        return False

    # pre
    seen[curr.y][curr.x] = True
    path.append(curr)

    # recurse
    for x, y in DIR:
        new_curr = Point(curr.x + x, curr.y + y)
        if walk(maze, wall, new_curr, end, seen, path):
            return True

    # pos
    path.pop()

    return False


def solve(
    maze: list[str],
    wall: str,
    start: Point,
    end: Point,
) -> Deque[Point]:
    seen: list[list[bool]] = [
        [False for _ in range(len(maze[0]))] for _ in range(len(maze))
    ]
    path: Deque[Point] = deque()

    walk(maze, wall, start, end, seen, path)

    return path


MAZE = [
    'xxxxxxxxxx x',
    'x        x x',
    'x        x x',
    'x xxxxxxxx x',
    'x          x',
    'x xxxxxxxxxx',
]

MAZE_SOLUTION = [
    {'x': 10, 'y': 0},
    {'x': 10, 'y': 1},
    {'x': 10, 'y': 2},
    {'x': 10, 'y': 3},
    {'x': 10, 'y': 4},
    {'x': 9, 'y': 4},
    {'x': 8, 'y': 4},
    {'x': 7, 'y': 4},
    {'x': 6, 'y': 4},
    {'x': 5, 'y': 4},
    {'x': 4, 'y': 4},
    {'x': 3, 'y': 4},
    {'x': 2, 'y': 4},
    {'x': 1, 'y': 4},
    {'x': 1, 'y': 5},
]


def test_solve_maze(maze=MAZE, expected=MAZE_SOLUTION):
    solution = solve(maze, wall='x', start=Point(10, 0), end=Point(1, 5))
    solution_dict = [{'x': x, 'y': y} for x, y in solution]
    assert solution_dict == expected
