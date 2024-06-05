import pytest
import main
import requests
from fastapi.testclient import TestClient
from main import app


def test_can_call_existing_endpoints_of_theAPI():
    # Function that asserts if the endpoints of the API works.
    try:
        ret = main.get_coordinates("Lima,Peru")
        assert ret is not None
    except:
        assert False, "Exception while calling an existing function"


def test_cannot_call_non_existing_endpoints_of_the_API():
    # Function that raises exception when the endpoint called exists.
    try:
        ret = main.something_not_existent("blah blah")
        assert False, "Exception not raised"
    except:
        pass


def test_the_response_status_code_404(requests_mock):
    # Function that tests the get_coordinates response when the get request is unsuccessful.
    url = "https://nominatim.openstreetmap.org/search?q=Lima%2CPeru&format=json"
    requests_mock.get(url, status_code=404)
    result = main.get_coordinates("Lima,Peru")
    assert result == ("", ""), "Should return blank"


def test_the_result_is_correct_for_simple_cases():
    # Function that raises exception when the testcase does not give correct answer for Lima, Peru
    ret = main.get_coordinates("Lima,Peru")
    assert ret == (float(-12.0621065), float(-77.0365256)), "Incorrect answer"


def test_the_result_is_correct_for_no_cases():
    # Function that raises exception when it gives an incorrect answer for nothing
    ret = main.get_coordinates("")
    assert ret == ("", ""), "Incorrect answer"


def test_the_result_is_correct_for_all_inputs():
    # Function that raises exception when the testcase does not give correct answer for most inputs

    # lima
    detected = main.get_coordinates("Lima,Peru")
    expected = float(-12.0621065), float(-77.0365256)
    assert detected == expected, "Incorrect answer for Lima, Peru"

    # miami
    detected = main.get_coordinates("Miami,USA")
    expected = float(25.7741728), float(-80.19362)
    assert detected == expected, "Incorrect answer for Miami, USA"

    # barcelona
    detected = main.get_coordinates("Barcelona,Spain")
    expected = float(41.3828939), float(2.1774322)
    assert detected == expected, "Incorrect answer for Barcelona, Spain"

    # melbourne
    detected = main.get_coordinates("Melbourne,Australia")
    expected = float(-37.8142454), float(144.9631732)
    assert detected == expected, "Incorrect answer for Melbourne, Australia"

    # buenos aires
    detected = main.get_coordinates("Buenos Aires,Argentina")
    expected = float(-34.6037181), float(-58.38153)
    assert detected == expected, "Incorrect answer for Buenos Aires, Argentina"

    # rio de janeiro
    detected = main.get_coordinates("Rio de Janeiro,Brazil")
    expected = float(-22.9110137), float(-43.2093727)
    assert detected == expected, "Incorrect answer for Rio de Janeiro, Brazil"

    # santiago
    detected = main.get_coordinates("Santiago, Chile")
    expected = float(-33.4377756), float(-70.6504502)
    assert detected == expected, "Incorrect answer for Santiago, Chile"

    # berlin
    detected = main.get_coordinates("Berlin, Germany")
    expected = float(52.5170365), float(13.3888599)
    assert detected == expected, "Incorrect answer for Berlin, Germany"

    # monza
    detected = main.get_coordinates("Monza, Italy")
    expected = float(45.5834418), float(9.2735257)
    assert detected == expected, "Incorrect answer for Monza, Italy"

    # montreal
    detected = main.get_coordinates("Montreal, Canada")
    expected = float(45.5031824), float(-73.5698065)
    assert detected == expected, "Incorrect answer for Montreal, Canada"


# test api

client = TestClient(app)


def test_get_coordinates_valid_city():
    response = client.get("/coordinates?query=Paris,France")
    assert response.status_code == 200
    data = response.json()
    assert "latitude" in data
    assert "longitude" in data
    assert isinstance(data["latitude"], float)
    assert isinstance(data["longitude"], float)


def test_get_coordinates_invalid_city():
    response = client.get("/coordinates?query=")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Location not found"
