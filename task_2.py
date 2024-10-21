"""
Модуль для реалізації алгоритмів пошуку шляхів BFS та DFS у графі.
"""


from collections import deque
from typing import List, Optional
import networkx as nx
from task_1 import create_financial_network


def bfs_path(graph: nx.Graph, start_node: str, end_node: str) -> Optional[List[str]]:
    """
    Реалізує пошук у ширину (BFS) для знаходження шляху між двома вершинами.

    Args:
        graph (nx.Graph): Граф для пошуку.
        start_node (str): Початкова вершина.
        end_node (str): Кінцева вершина.

    Returns:
        Optional[List[str]]: Шлях між початковою та кінцевою вершинами або None,
        якщо шлях не знайдено.
    """
    queue = deque([[start_node]])
    visited = set([start_node])

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        if vertex == end_node:
            return path

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


def dfs_path(graph: nx.Graph, start_node: str, end_node: str,
             path: Optional[List[str]] = None) -> Optional[List[str]]:
    """
    Реалізує пошук у глибину (DFS) для знаходження шляху між двома вершинами.

    Args:
        graph (nx.Graph): Граф для пошуку.
        start_node (str): Початкова вершина.
        end_node (str): Кінцева вершина.
        path (Optional[List[str]], optional): Поточний шлях. За замовчуванням None.

    Returns:
        Optional[List[str]]: Шлях між початковою та кінцевою вершинами або None,
        якщо шлях не знайдено.
    """
    if path is None:
        path = []
    path = path + [start_node]

    if start_node == end_node:
        return path

    for neighbor in graph[start_node]:
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, end_node, path)
            if new_path:
                return new_path

    return None


if __name__ == "__main__":
    # Створення графа та пошук шляхів
    FINANCIAL_NETWORK = create_financial_network()
    START_NODE = "Apple"
    END_NODE = "Facebook"

    bfs_result = bfs_path(FINANCIAL_NETWORK, START_NODE, END_NODE)
    dfs_result = dfs_path(FINANCIAL_NETWORK, START_NODE, END_NODE)

    print(f"BFS шлях від {START_NODE} до {END_NODE}: {' -> '.join(bfs_result or [])}")
    print(f"DFS шлях від {START_NODE} до {END_NODE}: {' -> '.join(dfs_result or [])}")
