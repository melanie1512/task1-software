from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import requests
import urllib.parse

app = FastAPI()


class CoordinatesResponse(BaseModel):
    latitude: float
    longitude: float


def get_coordinates(query):
    """
    Input: City name and Country in string query
    Output: Latitude and Longitude of the queried city/country

    Function requests the url with the query.
    It returns the latitude and longitude of the matched city
    or, if the city is not found, the coordinates of the best matched
    location.
    If the get request returns nothing or if it is unsuccessful,
    the function returns blank coordinates.
    """

    encoded_query = urllib.parse.quote(query)

    url = f"https://nominatim.openstreetmap.org/search?q={encoded_query}&format=json"

    headers = {"User-Agent": "Testing App"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if len(data) == 0:
            return "", ""
        city = ""
        if "," in query:
            city, country = query.split(",")
        for i in range(len(data)):
            if data[i]["name"] == city and data[i]["addresstype"] == "city":
                lat = float(data[i]["lat"])
                lon = float(data[i]["lon"])
                return lat, lon
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
        return lat, lon

    else:
        print(f"Failed to retrieve data: {response.status_code}")
    return "", ""


@app.get(
    "/coordinates",
    response_model=CoordinatesResponse,
    summary="Get coordinates",
    description="Returns the latitude and longitude of a given city.",
)
def read_coordinates(
    query: str = Query(
        ...,
        description="The city and the country to be queried in the format 'City, Country'",
    )
):
    lat, lon = get_coordinates(query)
    if lat == "" and lon == "":
        raise HTTPException(status_code=404, detail="Location not found")
    return {"latitude": lat, "longitude": lon}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
