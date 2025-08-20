import json
from json import JSONEncoder
from typing import List

import overpy
from geopy import Nominatim

overpass_api = overpy.Overpass()
geolocator = Nominatim(user_agent="my_searching_application")


# ----------------------------------------------------------    DTO

class MyLocation:
    def __init__(self, **kwargs):
        self.full_address = kwargs.get("address")
        self.latitude = kwargs.get("latitude")
        self.longitude = kwargs.get("longitude")
        self.boundingbox = kwargs.get("boundingbox")
        self.address: MyAddress = kwargs.get("address")

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(**dict_obj)

    def toJSON(self, indent=4):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=indent)


class MyAddress:
    def __init__(self, **kwargs):
        self.country = kwargs.get("country")
        self.postcode = kwargs.get("postcode")
        self.county = kwargs.get("county")
        self.city = kwargs.get("city")
        self.town = kwargs.get("town")
        self.village = kwargs.get("village")

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(**dict_obj)

    def get_city_name(self):
        if self.city is not None:
            return self.city
        if self.town is not None:
            return self.town
        if self.village is not None:
            return self.village
        return ""


class MyNode:
    def __init__(self, id: int, latitude: float, longitude: float, tags: dict = None):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.tags = tags


class MyWay:
    def __init__(self, id: int, node_ids: List[MyNode], tags: dict = None):
        self.id = id
        self.node_ids = node_ids
        self.tags = tags


# ----------------------------------------------------------

def get_search_results(query: str) -> List[MyLocation]:
    result = []
    data_list = geolocator.geocode(query, exactly_one=False)
    for data in data_list:
        result.append(MyLocation.from_dict({
            'address': data.address,
            'latitude': data.latitude,
            'longitude': data.longitude,
            'boundingbox': data.raw['boundingbox']
        }))

    return result


def get_reversed_address(latitude: str, longitude: str) -> MyAddress:
    location = geolocator.reverse(f"{latitude}, {longitude}")
    addr = location.raw['address']
    return MyAddress.from_dict({
        'country': addr.get('country'),
        'postcode': addr.get('postcode'),
        'county': addr.get('county'),
        'city': addr.get('city'),
        'town': addr.get('town'),
        'village': addr.get('village'),
    })


def search_streets_in_location(location_name):
    # fetch
    result = overpass_api.query(f"""
            [out:json];
            area[name="{location_name}"];
            way(area)[highway][name];
            (._;>;);
            out;
    """)
    return result


def convert_ways_and_nodes(streets_and_nodes) -> List[MyWay]:
    way_list = []

    for way in streets_and_nodes.ways:
        node_list = []
        for node in way.nodes:
            node_list.append(MyNode(node.id, float(node.lat), float(node.lon), node.tags))
        way_list.append(MyWay(way.id, node_list, way.tags))

    return way_list


class MyJsonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def save_json_to_file(ways: List[MyWay], filename = "my_ways.json"):
    with open(filename, 'w') as file:
        json.dump(ways, file, indent=2, cls=MyJsonEncoder)


if __name__ == '__main__':
    # I search a city name... I have multiple results
    # search_city = 'Balaton'
    search_city = 'Kaposvár'

    locations: List[MyLocation] = get_search_results(search_city)

    # I choose one element
    # location: MyLocation = locations[2]
    location: MyLocation = locations[0]

    # reverse address / other entry point -> I know the coordinates, I decode it again
    location.address = get_reversed_address(location.latitude, location.longitude)
    print(location.toJSON())

    # search streets in the given address
    # --- if we have multiple results --> add postal code, otherwise no need
    if len(locations) > 1:
        searching_address = f"{location.address.postcode} {location.address.get_city_name()}"
    else:
        searching_address = f"{location.address.get_city_name()}"

    ways_and_nodes = search_streets_in_location(searching_address)
    print(len(ways_and_nodes.nodes))
    print(len(ways_and_nodes.ways))

    # 3347 Balaton -- node: 284, ways: 43
    # Kaposvár -- 5890 , 1581

    # node: ez tartalmazza a geo koordinátát
    # way: utcanév, node-ok, tags
    # tags: ki kell szűrni:
    # ha van layer tag, az a way nem kell, droppolni
    # akár több way tesz ki egy utcát (node-okat majd össze kell mergelni)

    # példa: Kaposvár, Keceli bejáró
    # 7 találat van, mindegyik way. a térképen 2 tesz ki egy utcát: xx81, xx20
    # 53, 41, 45, 81, 12, 20, 73 -- mi a különbség?
    # tag-ek, amiket ki kell szűrni, nem kell: layer, "highway": "service" ? --> marad 3 = 53, 41, 73 (de akkor a 81, 20 ami a térképen van, miért azok?)
    # TODO --- itt ezt ki kell szűrni! (egyelőre nem tudom, hogy)
    # TODO node tag-eket is szűrni kellene

    converted_ways: List[MyWay] = convert_ways_and_nodes(ways_and_nodes)

    save_json_to_file(converted_ways)

    print("--- END ---")

# In Overpass, which queries OpenStreetMap data,
# nodes are fundamental points on a map with a specific latitude and longitude,
# representing single entities like an ATM or a street sign.
# Ways are ordered lists of these nodes that form lines or closed shapes,
# used to represent features like roads, rivers, or building outlines that cannot be defined by a single point.

# https://stackoverflow.com/questions/39283795/what-are-nodes-and-ways-in-overpass-api

# Geographic lat/lon information is always stored in nodes.
# some nodes may have tags, if they represent a node-like object in real life (could be an amenity or maybe a stop-sign).
# For a highway (=way which uses a number of nodes), the individual nodes don't need to have any tag at all.
