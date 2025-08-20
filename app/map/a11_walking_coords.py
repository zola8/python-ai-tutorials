from typing import List, Tuple

from geopy.exc import GeocoderServiceError
from geopy.geocoders import Nominatim

# Initialize geolocator with a user agent
geolocator = Nominatim(user_agent="geo_city_lookup")


def extract_coordinate(latitude: float, longitude: float):
    try:
        # Perform reverse geocoding
        location = geolocator.reverse(f"{latitude}, {longitude}")

        # Extract address components
        if location and location.raw and 'address' in location.raw:
            address = location.raw['address']
            city = address.get('city') or address.get('town') or address.get('village') or address.get('hamlet')
            state = address.get('state', '')
            country_code = address.get('country_code', '').upper()
            country = address.get('country', '')
            road = address.get('road', '')
            return {
                "city": city,
                "state": state,
                "country": country,
                "country_code": country_code,
                "road": road,
            }
        else:
            return {
                "error": "City could not be determined for these coordinates."
            }
    except GeocoderServiceError as e:
        return {
            "error": f"Geocoding error: {e}"
        }


if __name__ == '__main__':
    # example walking:
    my_walking: List[Tuple[float, float]] = [
        (47.548321, 7.953877),
        (47.546976, 7.952395),
        (47.545849, 7.950863),
        (47.546188, 7.949330),
        (47.546533, 7.947865),
        (47.547326, 7.944595),
        (47.547786, 7.944595),
    ]

    for lat, lon in my_walking:
        result = extract_coordinate(lat, lon)
        print(result)


# {'city': 'Stein', 'state': 'Aargau', 'country': 'Schweiz/Suisse/Svizzera/Svizra', 'country_code': 'CH', 'road': 'Rheinbrückstrasse'}
# {'city': 'Stein', 'state': 'Aargau', 'country': 'Schweiz/Suisse/Svizzera/Svizra', 'country_code': 'CH', 'road': 'Schaffhauserstrasse'}
# {'city': 'Stein', 'state': 'Aargau', 'country': 'Schweiz/Suisse/Svizzera/Svizra', 'country_code': 'CH', 'road': 'Fridolinsbrücke'}
# {'city': 'Stein', 'state': 'Aargau', 'country': 'Schweiz/Suisse/Svizzera/Svizra', 'country_code': 'CH', 'road': 'Fridolinsbrücke'}
# {'city': 'Stein', 'state': 'Aargau', 'country': 'Schweiz/Suisse/Svizzera/Svizra', 'country_code': 'CH', 'road': 'Fridolinsbrücke'}
# {'city': 'Säckingen', 'state': 'Baden-Württemberg', 'country': 'Deutschland', 'country_code': 'DE', 'road': 'Fricktalstraße'}
# {'city': 'Säckingen', 'state': 'Baden-Württemberg', 'country': 'Deutschland', 'country_code': 'DE', 'road': 'Hauensteinstraße'}
