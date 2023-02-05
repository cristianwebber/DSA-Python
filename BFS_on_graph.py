from __future__ import annotations

from collections import deque


class Graph:
    def __init__(self, graph: dict[int, list[int]]) -> None:
        self.graph = graph

    def BFS(self, needle: int, starting_node: int) -> list[int]:
        visited = {i: False for i in self.graph}
        prev: dict[int, int] = {i: -1 for i in self.graph}
        queue = deque([starting_node])

        visited[starting_node] = True
        while queue:
            curr = queue.popleft()

            for i in self.graph[curr]:
                if i == needle:
                    prev[i] = curr
                    curr = i
                    del queue
                    break

                if visited[i]:
                    continue

                visited[i] = True
                queue.append(i)
                prev[i] = curr
                queue.append(i)

        path = []
        while prev[curr] != -1:
            path.append(curr)
            curr = prev[curr]
        return [starting_node] + list(reversed(path))


def test_BFS_on_graph():
    graph = {
        5: [3, 7],
        3: [2, 4],
        7: [8],
        2: [],
        4: [8, 9],
        8: [],
    }
    g = Graph(graph)

    path = g.BFS(needle=9, starting_node=5)
    assert path == [5, 3, 4, 9]
