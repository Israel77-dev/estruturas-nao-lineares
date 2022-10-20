"""
Implementação da estrutura de grafo
"""

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Any, List
from abc import ABC, abstractmethod


class Graph(ABC):
    @abstractmethod
    def __init__(self, connections):
        """
        Cria a estrutura de grafo baseada numa lista de conexões
        representadas por uma iterável de tuplas indicando as conexões entre
        os vértices. Por exemplo, o grafo:
        A ----- B
        |
        C

        Poderia ser criado a partir da lista [('A','B'), ('A', 'C')]
        ficando a cargo das implementações concretas a possibilidade do grafo
        ser direcionado ou não e ter um custo na ligação das arestas
        """
        self._graph = defaultdict(set)

        for connection in connections:
            self.add_connection(*connection)

    @abstractmethod
    def add_connection(self, node_1, node_2):
        pass

    @abstractmethod
    def remove_connection(self, node_1, node_2):
        pass

    @property
    def order(self):
        return len(self._graph)

    @property
    def size(self):
        return sum(len(x) for x in self._graph)

    def bfs(self, start, target=None):
        """
        Implementação de algoritmo de breadth-first search para
        encontrar um nó ("target") a partir do ponto de saída
        ("start")
        """

        q = deque()
        visited = set()

        # Se não for especificado um alvo, apenas percorrer o grafo
        if target == None:
            q.append(start)
            result = []

            while q:
                v = q.popleft()
                visited.add(v)
                result.append(v)

                for node in self._graph[v]:
                    if node not in visited:
                        q.append(node)
                        visited.add(node)

            return result

        # Armazenar os nós e o caminho até eles ao procurar um alvo específico
        q.appendleft((start, [start]))

        while q:
            v: Any
            path: List[Any]

            v, path = q.popleft()
            visited.add(v)

            for node in self._graph[v]:
                if node == target:
                    path.append(target)
                    return path
                else:
                    if node not in visited:
                        q.append((node, path + [node]))
                        visited.add(node)


class WeightedGraph(Graph):
    @abstractmethod
    def add_connection(self, node_1, node_2, weight=1):
        pass


class UndirectedGraph(Graph):
    def __init__(self, connections):
        super().__init__(connections)

    def add_connection(self, node_1, node_2):
        self._graph[node_1].add(node_2)
        self._graph[node_2].add(node_1)

    def remove_connection(self, node_1, node_2):
        self._graph[node_1].remove(node2)
        self._graph[node2].remove(node_1)


class DirectedGraph(Graph):
    def __init__(self, connections):
        super().__init__(connections)

    def add_connection(self, connection):
        node_1, node2 = connection
        self._graph[node_1].add(node2)

    def remove_connection(self, connection):
        node_1, node2 = connection
        self._graph[node_1].remove(node2)


if __name__ == "__main__":
    q = UndirectedGraph(
        [
            ("A", "B"),
            ("B", "C"),
            ("B", "D"),
            ("C", "D"),
            ("C", "E"),
            ("D", "E"),
        ]
    )
    print(q.bfs("B"))
