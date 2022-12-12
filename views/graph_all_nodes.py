
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import networkx as nx
import json
import random
from networkx.drawing.nx_pydot import write_dot
G = nx.empty_graph()


# ForceAtlas2 is a force directed layout: it simulates a physical system in order to spatialize a network. Nodes repulse each other like charged particles, while edges attract their nodes, like springs. These forces create a movement that converges to a balanced state.

communities = {
    "kc": {"color": "#00D8EC"},
    "popcorn": {"color": "#E4202E"},
    "ponce": {"color": "#FFCE01"},
    "otp": {"color": "#E34D2E"},
    "zevent": {"color": "#57AF37"},
}

communities_by_user_id = {}
nodes = []

for community_name, community_info in communities.items():
    nodes.append((community_name, {"color": community_info["color"], "size": 1}))
    with open(f"{community_name}_followers_december_2022.json", "r") as f:
        community_info["followers"] = json.load(f)
        for id in community_info["followers"]:
            if id in communities_by_user_id:
                communities_by_user_id[id].append(community_name)
            else:
                communities_by_user_id[id] = [community_name]

kc_x_popcorn = list(set(communities["kc"]["followers"]) & set(communities["popcorn"]["followers"]))
popcorn_x_ponce = list(set(communities["ponce"]["followers"]) & set(communities["popcorn"]["followers"]))
print(f"{100*len(kc_x_popcorn) /len(communities['popcorn']['followers']) }% des followers popcorn followent KC")
print(f"{100*len(popcorn_x_ponce) /len(communities['popcorn']['followers']) }% des followers de popcorn followent ponce")

edges = []

shuffled_list = list(communities_by_user_id.items())
random.shuffle(shuffled_list)

for id, communities_membership in shuffled_list[:3000]:
    for community_membership in communities_membership:
        nodes.append((id+"-"+community_membership, {"color": communities[community_membership]["color"], "size": 1}))
        G.add_edge(id+"-"+community_membership, community_membership, color=communities[community_membership]["color"])
        for community_membership2 in communities_membership:
            G.add_edge(community_membership2, id+"-"+community_membership, color=communities[community_membership]["color"])

G.add_nodes_from(nodes)


colored_dict = nx.get_node_attributes(G, 'color')
default_color = 'black'
color_seq = [colored_dict.get(node, default_color) for node in G.nodes()]

sized_dict = nx.get_node_attributes(G, 'size')
default_size = 0.1
size_seq = [sized_dict.get(node, default_size) for node in G.nodes()]

edge_colors = nx.get_edge_attributes(G, 'color').values()

print("Drawing graph...")

fig = plt.figure()
nx.write_gexf(G, "views/graph_all_nodes.gexf")

#nx.draw(G, with_labels=False, node_color=color_seq, alpha=0.2, node_size=size_seq, edge_color=edge_colors)
fig.set_facecolor("#00000F")

print("Showing graph...")
#plt.show()
