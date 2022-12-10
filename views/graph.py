
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import networkx as nx
import json
import random


G = nx.empty_graph()

communities_by_id = {}
kc_followers = []
popcorn_followers = []

with open("popcorn_followers_december_2022.json", "r") as f:
    popcorn_followers = json.load(f)
    for id in popcorn_followers:
        if id in communities_by_id:
            communities_by_id[id].append("Popcorn")
        else:
            communities_by_id[id] = ["Popcorn"]

with open("kc_followers_december_2022.json", "r") as f:
    kc_followers = json.load(f)
    for id in kc_followers:
        if id in communities_by_id:
            communities_by_id[id].append("KC")
        else:
            communities_by_id[id] = ["KC"]

intersection = list(filter(lambda item: len(item[1]) == 2, communities_by_id.items()))

# print(f"Popcorn followers : {len(popcorn_followers)}")
# print(f"KC followers : {len(kc_followers)}")
# print(f"Intersection followers : {len(intersection)}")

print(f"{round(100*len(intersection)/len(kc_followers),2)}% des followers KC followent popcorn")
print(f"{round(100*len(intersection)/len(popcorn_followers),2)}% des followers popcorn followent kc")

nodes = [
    ("Popcorn", {"color": "red", "size": 1000}),
    ("KC", {"color": "blue", "size": 1000}),
]
edges = []

shuffled_list = list(communities_by_id.items())
random.shuffle(shuffled_list)

for id, communities in shuffled_list[:2000]:
    nodes += id
    if("KC" in communities):
        G.add_edge(id, 'KC', color= 'blue')
    if("Popcorn" in communities):
        G.add_edge(id, 'Popcorn', color= 'red')

G.add_nodes_from(nodes)


colored_dict = nx.get_node_attributes(G, 'color')
default_color = 'pink'
color_seq = [colored_dict.get(node, default_color) for node in G.nodes()]

sized_dict = nx.get_node_attributes(G, 'size')
default_size = 1
size_seq = [sized_dict.get(node, default_size) for node in G.nodes()]

edge_colors = nx.get_edge_attributes(G,'color').values()

print("Drawing graph...")
nx.draw(G, with_labels=False, node_color= color_seq, node_size= size_seq, edge_color= edge_colors)

print("Showing graph...")
plt.show()