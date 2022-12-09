
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import networkx as nx

G = nx.empty_graph()
nodes = [
    (4, {"color": "red"}),
    (5, {"color": "green"}),
    (10, {"color": "green"}),
    ("Popcorn", {"color": "green", "size": 1000}),
    (3, {"color": "green"}),
]
G.add_nodes_from(nodes)
G.add_edge(5,4, color="blue")

colored_dict = nx.get_node_attributes(G, 'color')
default_color = 'blue'
color_seq = [colored_dict.get(node, default_color) for node in G.nodes()]

sized_dict = nx.get_node_attributes(G, 'size')
default_size = 100
size_seq = [sized_dict.get(node, default_size) for node in G.nodes()]

nx.draw(G, with_labels=True, node_color= color_seq, node_size= size_seq)
plt.show()