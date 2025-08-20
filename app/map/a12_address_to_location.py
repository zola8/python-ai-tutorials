from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="z-app")

if __name__ == '__main__':
    location = geolocator.geocode("Hauensteinstraße, Säckingen, Baden-Württemberg, Deutschland")
    print(location.address)
    print(location.latitude, location.longitude)

    location = geolocator.geocode("Fridolinsbrücke, Stein, Aargau, Schweiz/Suisse/Svizzera/Svizra")
    print(location.address)
    print(location.latitude, location.longitude)


# DMS (degrees, minutes, seconds)*
# 47°24'42.0"N 8°33'47.7"E

# DD (decimal degrees)*
# 47.411672 , 8.563253
