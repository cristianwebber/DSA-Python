from __future__ import annotations

import heapq
import sys


class Vertex:
    def __init__(self, node: str):
        self.id: str = node
        self.adjacent: dict[str, int] = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous: None | str = None

    def add_neighbor(self, neighbor: str, weight: int = 0):
        self.adjacent[neighbor] = weight

    @property
    def connections(self) -> list[str]:
        return list(self.adjacent.keys())

    def get_weight(self, neighbor: str) -> int:
        return self.adjacent[neighbor]

    def set_distance(self, dist: int) -> None:
        self.distance = dist

    def get_distance(self) -> int:
        return self.distance

    def set_previous(self, prev: str) -> None:
        self.previous = prev

    def set_visited(self) -> None:
        self.visited = True

    def __lt__(self, other: str) -> bool:
        return id(self) > id(other)


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node: str) -> Vertex:
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n: str) -> Vertex | None:
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm: str, to: str, cost: int = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self) -> list[str]:
        return list(self.vert_dict.keys())

    def set_previous(self, current: str):
        self.previous = current

    def get_previous(self) -> str:
        return self.previous


def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.id)
        shortest(v.previous, path)
    return


def dijkstra(graph: Graph, start: Vertex | None) -> None:
    if start is None:
        raise Exception("Start can't be a empty vertex")
    else:
        start.set_distance(0)

    unvisited_queue = [(v.get_distance(), v) for v in graph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [
            (v.get_distance(), v)
            for v in graph if not v.visited
        ]
        heapq.heapify(unvisited_queue)


def test_dijkstra():
    graph = Graph()

    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')
    graph.add_vertex('e')
    graph.add_vertex('f')

    graph.add_edge('a', 'b', 7)
    graph.add_edge('a', 'c', 9)
    graph.add_edge('a', 'f', 14)
    graph.add_edge('b', 'c', 10)
    graph.add_edge('b', 'd', 15)
    graph.add_edge('c', 'd', 11)
    graph.add_edge('c', 'f', 2)
    graph.add_edge('d', 'e', 6)
    graph.add_edge('e', 'f', 9)

    dijkstra(
        graph=graph,
        start=graph.get_vertex('a'),
    )

    target = graph.get_vertex('e')
    if target is None:
        raise Exception("End can't be a empty vertex")
    path = [target.id]
    shortest(target, path)

    path = path[::-1]
    assert path == ['a', 'c', 'f', 'e']
