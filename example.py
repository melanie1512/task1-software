import requests
import json
from decimal import Decimal
import urllib.parse

def get_coordinates(query):
    encoded_query = urllib.parse.quote(query)
    url = f"https://nominatim.openstreetmap.org/search?q={encoded_query}&format=json"

    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; YourAppName/1.0; +http://yourwebsite.com)'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if (len(data) == 0):
            return 1, 1
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return lat, lon
    else:
        print(f"Failed to retrieve data: {response.status_code}")
    return 0, 0