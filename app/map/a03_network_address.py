# https://gdsl-ul.github.io/wma/labs/w07_OSM.html
# 6.2.2.4 Method #4, Passing an address and distance (bounding box or network) in meters

import osmnx as ox

# network from address, including only nodes within 1km along the network from the address
G = ox.graph_from_address(address="7400 Kaposvár, Ady Endre utca 1", dist=1000, dist_type="network",
                          network_type="drive")

if __name__ == '__main__':
    print("1: with nodes")
    ox.plot_graph(G, node_color="r", figsize=(5, 5))

    print("2: without nodes")
    ox.plot_graph(G, node_color="none")  # without plotting nodes
