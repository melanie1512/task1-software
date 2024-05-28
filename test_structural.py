import pytest
import example

def test_can_call_existing_endpoints_of_theAPI():
    try:
        ret = example.get_coordinates("Lima,Peru")
        assert(ret is not None)
    except:
        assert False, "Exception while calling an existing function"

# raises exception when the endpoint exists
def test_cannot_call_non_existing_endpoints_of_the_API():
    try:
        ret = example.something_not_existent("blah blah")
        assert False, "Exception not raised"
    except:
        pass

# raises exception when the testcase does not give correct answer
def test_the_result_is_correct_for_simple_cases():
    ret = example.get_coordinates("Lima,Peru")
    assert (ret == ("-12.0621065", "-77.0365256")), "Incorrect answer"

def test_the_result_is_correct_for_all_inputs():
    # lima
    detected = example.get_coordinates("Lima,Peru")
    expected = "-12.0621065", "-77.0365256"
    assert (detected == expected), "Incorrect answer for Lima, Peru"
    # nyc
    detected = example.get_coordinates("New York,USA")
    expected = "40.7127281", "-74.0060152"
    assert (detected == expected), "Incorrect answer for New York, USA"

    # london
    detected = example.get_coordinates("London,UK")
    expected = "51.5074456", "-0.1277653"
    assert (detected == expected), "Incorrect answer for London, UK"

    # paris
    detected = example.get_coordinates("Paris,France")
    expected = "48.8588897", "2.3200410217200766"
    assert (detected == expected), "Incorrect answer for Paris, France"

    # barcelona
    detected = example.get_coordinates("Barcelona,Spain")
    expected = "41.3828939", "2.1774322"
    assert (detected == expected), "Incorrect answer for Barcelona, Spain"

    # melbourne
    detected = example.get_coordinates("Melbourne,Australia")
    expected = "-37.8142454", "144.9631732"
    assert (detected == expected), "Incorrect answer for Melbourne, Australia"
