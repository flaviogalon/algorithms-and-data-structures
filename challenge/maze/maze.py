from typing import TypedDict


class Point(TypedDict):
    x: int
    y: int


dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def _maze_solver(
    maze: list[str],
    wall: str,
    point: Point,
    end_point: Point,
    path: list[Point],
    visited: list[Point],
) -> bool:
    if (
        point["y"] < 0
        or point["x"] < 0
        or point["y"] >= len(maze)
        or point["x"] >= len(maze[0])
    ):
        return False
    if point == end_point:
        path.append(point)
        return True
    if maze[point["y"]][point["x"]] == wall:
        return False
    if point in visited:
        return False

    visited.append(point)
    path.append(point)

    for i in range(len(dir)):
        movement_y, movement_x = dir[i]
        next_position: Point = {
            "y": point["y"] + movement_y,
            "x": point["x"] + movement_x,
        }
        if _maze_solver(maze, wall, next_position, end_point, path, visited):
            return True

    path.pop()
    return False


def maze_solver(
    maze: list[str], wall: str, start_point: Point, end_point: Point
) -> list[Point]:
    path = []
    visited = []
    _maze_solver(maze, wall, start_point, end_point, path, visited)
    return path


maze = [
    "xxxxxxxxxx x",
    "x        x x",
    "x        x x",
    "x xxxxxxxx x",
    "x          x",
    "x xxxxxxxxxx",
]

expected_result = [
    {"x": 10, "y": 0},
    {"x": 10, "y": 1},
    {"x": 10, "y": 2},
    {"x": 10, "y": 3},
    {"x": 10, "y": 4},
    {"x": 9, "y": 4},
    {"x": 8, "y": 4},
    {"x": 7, "y": 4},
    {"x": 6, "y": 4},
    {"x": 5, "y": 4},
    {"x": 4, "y": 4},
    {"x": 3, "y": 4},
    {"x": 2, "y": 4},
    {"x": 1, "y": 4},
    {"x": 1, "y": 5},
]

result = maze_solver(maze, "x", {"x": 10, "y": 0}, {"x": 1, "y": 5})

assert expected_result == result
