"""
Модуль для реалізації алгоритму Дейкстри на зваженому графі фінансової мережі.
"""


import random
from typing import Dict, Tuple
import networkx as nx
from task_1 import create_financial_network, visualize_graph


def add_weights_to_graph(financial_network: nx.Graph) -> nx.Graph:
    """
    Додає випадкові ваги до ребер графа.

    Args:
        financial_network (nx.Graph): Вхідний граф.

    Returns:
        nx.Graph: Граф зі зваженими ребрами.
    """
    for (u, v) in financial_network.edges():
        financial_network[u][v]['weight'] = random.randint(1, 10)
    return financial_network

def dijkstra(graph: nx.Graph, start_node: str) -> Tuple[Dict[str, float], Dict[str, str]]:
    """
    Реалізує алгоритм Дейкстри для знаходження найкоротших шляхів.

    Args:
        graph (nx.Graph): Зважений граф.
        start_node (str): Початкова вершина.

    Returns:
        Tuple[Dict[str, float], Dict[str, str]]: Кортеж, що містить:
            - Словник відстаней від початкової вершини до всіх інших.
            - Словник попередніх вершин для відновлення шляху.
    """
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_node] = 0
    unvisited = list(graph.nodes())
    previous_nodes = {vertex: None for vertex in graph}

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, attrs in graph[current_vertex].items():
            weight = attrs['weight']
            distance_to_neighbor = distances[current_vertex] + weight
            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                previous_nodes[neighbor] = current_vertex

        unvisited.remove(current_vertex)

    return distances, previous_nodes

def get_path(previous_nodes: dict, start_node: str, end_node: str) -> list:
    """
    Відновлює шлях від початкової до кінцевої вершини.

    Args:
        previous_nodes (dict): Словник попередніх вершин.
        start_node (str): Початкова вершина.
        end_node (str): Кінцева вершина.

    Returns:
        list: Шлях від початкової до кінцевої вершини.
    """
    path = []
    current = end_node
    while current:
        path.append(current)
        current = previous_nodes[current]
    return path[::-1]

if __name__ == "__main__":
    # Створення графа та додавання ваг
    financial_graph = create_financial_network()
    weighted_graph = add_weights_to_graph(financial_graph)
    visualize_graph(weighted_graph)

    # Знаходження найкоротших шляхів від кожної вершини до всіх інших
    all_shortest_paths = {}
    for start_vertex in weighted_graph.nodes():
        distances, previous = dijkstra(weighted_graph, start_vertex)
        paths = {}
        for end_vertex in weighted_graph.nodes():
            if end_vertex != start_vertex:
                path = get_path(previous, start_vertex, end_vertex)
                paths[end_vertex] = (distances[end_vertex], path)
        all_shortest_paths[start_vertex] = paths

    # Виведення результатів
    for start_vertex, paths in all_shortest_paths.items():
        print(f"\nНайкоротші шляхи від {start_vertex}:")
        for end_vertex, (distance, path) in paths.items():
            print(f"  До {end_vertex}: відстань = {distance}, шлях = {' -> '.join(path)}")
