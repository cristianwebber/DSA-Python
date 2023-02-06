from __future__ import annotations

from typing import NamedTuple


class GraphEdge(NamedTuple):
    to: int
    weight: int


def walk(
        graph: list[list[GraphEdge]],
        curr: int,
        needle: int,
        seen: list[bool],
        path: list[int],
) -> bool:
    if seen[curr]:
        return False
    seen[curr] = True

    path.append(curr)
    if curr == needle:
        return True

    # recurse
    lst = graph[curr]
    for i in range(len(graph[curr])):
        edge = lst[i]
        if walk(graph, edge.to, needle, seen, path):
            return True

    path.pop()

    return False


def dfs(graph: list[list[GraphEdge]], source: int, needle: int) -> list[int]:
    seen = [False for _ in graph]
    path: list[int] = []

    walk(graph, source, needle, seen, path)

    return path


def test_DFS_on_graph():
    #
    # 1 -> 2 -> 3
    # ↳ 4 -> 5↗
    #   ↳ 6↗
    #     ↳ 7
    #
    graph = [
        [],
        [GraphEdge(1, 1), GraphEdge(4, 1)],
        [GraphEdge(3, 1)],
        [],
        [GraphEdge(5, 1), GraphEdge(6, 1)],
        [GraphEdge(3, 1)],
        [GraphEdge(5, 1), GraphEdge(7, 1)],
        [],
    ]

    assert dfs(graph, 1, 7) == [1, 4, 6, 7]
