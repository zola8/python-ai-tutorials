#  https://www.latlong.net/#google_vignette -- kaposvar


import matplotlib.pyplot as plt
import osmnx as ox

# create bikeable network from point, inside bounding box of N, S, E, W each 750m from point
location_point = (46.366531, 17.782480)
G = ox.graph_from_point(location_point, dist=750, dist_type="bbox", network_type="bike")
ox.plot_graph(G, node_color="r", figsize=(5, 5))

# Kaposvar, HU
# create network only of nodes within 750m along the network from point
location_point = (46.345678, 17.785292)
G1 = ox.graph_from_point(location_point, dist=1000, dist_type="network")
ox.plot_graph(G1, node_color="none", figsize=(5, 5))

if __name__ == '__main__':
    plt.show()
