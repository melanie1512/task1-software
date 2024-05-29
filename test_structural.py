import pytest
import example


def test_can_call_existing_endpoints_of_theAPI():
    try:
        ret = example.get_coordinates("Lima,Peru")
        assert ret is not None
    except:
        assert False, "Exception while calling an existing function"


# raises exception when the endpoint exists
def test_cannot_call_non_existing_endpoints_of_the_API():
    try:
        ret = example.something_not_existent("blah blah")
        assert False, "Exception not raised"
    except:
        pass


# raises exception when the testcase does not give correct answer for Lima, Peru
def test_the_result_is_correct_for_simple_cases():
    ret = example.get_coordinates("Lima,Peru")
    assert ret == (float(-12.2001093), float(-76.2850579)), "Incorrect answer"


# raises exception when the testcase does not give correct answer for most inputs
def test_the_result_is_correct_for_all_inputs():
    # lima
    detected = example.get_coordinates("Lima,Peru")
    expected = float(-12.2001093), float(-76.2850579)
    assert detected == expected, "Incorrect answer for Lima, Peru"

    # miami
    detected = example.get_coordinates("Miami,USA")
    expected = float(25.7741728), float(-80.19362)
    assert detected == expected, "Incorrect answer for Miami, USA"

    # paris
    detected = example.get_coordinates("Paris,France")
    expected = float(48.8588897), float(2.3200410217200766)
    assert detected == expected, "Incorrect answer for Paris, France"

    # barcelona
    detected = example.get_coordinates("Barcelona,Spain")
    expected = float(41.3828939), float(2.1774322)
    assert detected == expected, "Incorrect answer for Barcelona, Spain"

    # melbourne
    detected = example.get_coordinates("Melbourne,Australia")
    expected = float(-37.8142454), float(144.9631732)
    assert detected == expected, "Incorrect answer for Melbourne, Australia"

    # buenos aires
    detected = example.get_coordinates("Buenos Aires,Argentina")
    expected = float(-34.6037181), float(-58.38153)
    assert detected == expected, "Incorrect answer for Buenos Aires, Argentina"

    # rio de janeiro
    detected = example.get_coordinates("Rio de Janeiro,Brazil")
    expected = float(-22.9110137), float(-43.2093727)
    assert detected == expected, "Incorrect answer for Rio de Janeiro, Brazil"

    # santiago
    detected = example.get_coordinates("Santiago, Chile")
    expected = float(-33.4377756), float(-70.6504502)
    assert detected == expected, "Incorrect answer for Santiago, Chile"

    # berlin
    detected = example.get_coordinates("Berlin, Germany")
    expected = float(52.5170365), float(13.3888599)
    assert detected == expected, "Incorrect answer for Berlin, Germany"

    # monza
    detected = example.get_coordinates("Monza, Italy")
    expected = float(45.5834418), float(9.2735257)
    assert detected == expected, "Incorrect answer for Monza, Italy"

    # montreal
    detected = example.get_coordinates("Montreal, Canada")
    expected = float(45.5031824), float(-73.5698065)
    assert detected == expected, "Incorrect answer for Montreal, Canada"

    # shanghai
    detected = example.get_coordinates("Shanghai, China")
    expected = float(31.2312707), float(121.4700152)
    assert detected == expected, "Incorrect answer for Shanghai, China"
