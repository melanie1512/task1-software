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
    assert (ret == (-12.0621065, -77.0365256)), "Incorrect answer"

def test_the_result_is_correct_for_all_inputs():
    detected = example.get_coordinates("Lima,Peru")