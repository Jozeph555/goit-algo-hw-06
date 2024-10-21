"""
Модуль для створення, візуалізації та аналізу фінансової мережі.
"""


import networkx as nx
import matplotlib.pyplot as plt


def create_financial_network():
    """
    Створює граф фінансової мережі.

    Returns:
        networkx.Graph: Граф, що представляє фінансову мережу.
    """
    fin_network = nx.Graph()

    # Визначення вузлів (компанії та банки)
    companies = ["Apple", "Microsoft", "Amazon", "Google", "Facebook"]
    banks = ["JP Morgan", "Bank of America", "Citigroup", "Wells Fargo", "Goldman Sachs"]

    # Додавання вузлів до графа
    fin_network.add_nodes_from(companies, node_type="company")
    fin_network.add_nodes_from(banks, node_type="bank")

    # Визначення зв'язків між вузлами
    edges = [
        ("Apple", "JP Morgan"), ("Apple", "Citigroup"),
        ("Microsoft", "Bank of America"), ("Microsoft", "Goldman Sachs"),
        ("Amazon", "JP Morgan"), ("Amazon", "Wells Fargo"),
        ("Google", "Citigroup"), ("Google", "Goldman Sachs"),
        ("Facebook", "Bank of America"), ("Facebook", "Wells Fargo"),
        ("JP Morgan", "Bank of America"), ("Citigroup", "Wells Fargo"),
        ("Goldman Sachs", "JP Morgan")
    ]
    fin_network.add_edges_from(edges)

    return fin_network


def visualize_graph(fin_network: nx.Graph):
    """
    Візуалізує граф фінансової мережі з вагами ребер.

    Args:
        fin_network (nx.Graph): Граф для візуалізації.
    """
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(fin_network)
    
    # Малюємо вузли
    node_colors = ['lightblue' if fin_network.nodes[node]['node_type'] == 'company' \
                   else 'lightgreen' for node in fin_network.nodes()]
    nx.draw_networkx_nodes(fin_network, pos, node_color=node_colors, node_size=3000)
    
    # Малюємо ребра
    nx.draw_networkx_edges(fin_network, pos)
    
    # Додаємо підписи вузлів
    nx.draw_networkx_labels(fin_network, pos, font_size=10, font_weight='bold')
    
    # Додаємо ваги ребер
    edge_labels = nx.get_edge_attributes(fin_network, 'weight')
    nx.draw_networkx_edge_labels(fin_network, pos, edge_labels=edge_labels)
    
    plt.title("Фінансова мережа компаній та банків", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def analyze_graph(fin_network):
    """
    Аналізує основні характеристики графа.

    Args:
        fin_network (networkx.Graph): Граф для аналізу.
    """
    print(f"Кількість вершин: {fin_network.number_of_nodes()}")
    print(f"Кількість ребер: {fin_network.number_of_edges()}")

    print("\nСтупінь вершин:")
    for node in fin_network.nodes():
        print(f"{node}: {fin_network.degree(node)}")

    print("\nЦентральність за посередництвом:")
    betweenness = nx.betweenness_centrality(fin_network)
    for node, centrality in sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{node}: {centrality:.4f}")


if __name__ == "__main__":
    # Створення, візуалізація та аналіз графа
    financial_network = create_financial_network()
    visualize_graph(financial_network)
    analyze_graph(financial_network)
