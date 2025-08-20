# https://gdsl-ul.github.io/wma/labs/w07_OSM.html#method-6-passing-a-poylgon-in-the-wgs-crs

import osmnx as ox

city = ox.geocode_to_gdf("Budapest, Hungary")
polygon = city["geometry"].iloc[0]
G = ox.graph_from_polygon(polygon, network_type="drive_service")

if __name__ == '__main__':
    ox.plot_graph(G, node_size=0, edge_color="w", edge_linewidth=0.3)
