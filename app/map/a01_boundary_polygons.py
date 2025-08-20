# https://gdsl-ul.github.io/wma/labs/w07_OSM.html

import matplotlib.pyplot as plt
import osmnx as ox

city = ox.geocode_to_gdf("Balaton")
ax = city.plot(fc="gray", ec="none")
ax.axis("off")

# get boundary polygons for several authorities and plot
place_names = ["Budapest", "Kaposvár", "Székesfehérvár"]
places = ox.geocode_to_gdf(place_names)
ax = places.plot(fc="gray", ec="red")
ax.axis("off")

place_names = ["Somogy megye", "Baranya megye", "Zala megye", "Tolna megye"]
places = ox.geocode_to_gdf(place_names)
ax = places.plot(fc="gray", ec="red")

if __name__ == "__main__":
    plt.show()
