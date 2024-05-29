import requests
import json
from decimal import Decimal
import urllib.parse


def get_coordinates(query):
    """
    Input: City name and Country in string query
    Output: Latitude and Longitude of the City in query
    """

    encoded_query = urllib.parse.quote(query)
    url = f"https://nominatim.openstreetmap.org/search?q={encoded_query}&format=json"

    headers = {"User-Agent": "Testing App"}

    city, country = query.split(",")
    print(city)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if len(data) == 0:
            return 1, 1
        for i in range(len(data)):
            if data[i]["name"] == city:
                lat = float(data[i]["lat"])
                lon = float(data[i]["lon"])
                return lat, lon
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
        return lat, lon

    else:
        print(f"Failed to retrieve data: {response.status_code}")
    return "", ""
