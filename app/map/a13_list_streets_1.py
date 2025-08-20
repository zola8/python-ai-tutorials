import requests

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
area[name="Kaposvár"];
way(area)[highway][name];
out;
"""

response = requests.get(overpass_url, params={'data': overpass_query})

# NOK - its only highway?



if __name__ == '__main__':
    data = response.json()
    print(data)


# Relation: Zurich (1682248)
# https://www.openstreetmap.org/relation/1682248

# https://overpass-turbo.eu/

# [out:json]; area[name = "Zürich"]; (way(area)[highway]; ); (._;>;); out;



# --------------- OK:  https://gis.stackexchange.com/questions/480512/openstreetmap-overpass-ql-query-to-get-all-house-numbers-and-streets-of-a-city
# https://osm-queries.ldodds.com/misc/geocode-area.osm.html


# [out:csv(::lat, ::lon, "addr:street"; true; ",")];
# // fetch area to search in
# {{geocodeArea:Zurich}}->.searchArea;
# (
#   node(area.searchArea)["addr:street"];
# );
# out center;
