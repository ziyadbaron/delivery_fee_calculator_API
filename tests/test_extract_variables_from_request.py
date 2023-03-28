from functions import extract_the_variables

import constants
import functions_for_testing

'''test extract_the_variables function'''


# correct request body

def test_json_request_is_correct():
    '''test if the Json request is correct (normal)'''

    requests_time = functions_for_testing.generate_iso_time(rush_hour=False)

    request_json = functions_for_testing.create_json_body(
        time=requests_time)

    cart_value, delivery_distance, number_of_items, time = extract_the_variables(
        request_json)

    assert cart_value == constants.minimum_cart_value
    assert delivery_distance == constants.minimum_distance
    assert number_of_items == constants.additional_items_threshold
    assert time == requests_time


# test if json request has a None value


def test_json_request_cart_value_is_None():
    '''test if the cart value in Json request is None'''

    requests_time = functions_for_testing.generate_iso_time(rush_hour=False)

    request_json = functions_for_testing.create_json_body(
        cart_value=None, time=requests_time)

    cart_value, delivery_distance, number_of_items, time = extract_the_variables(
        request_json)

    assert cart_value == None
    assert delivery_distance == constants.minimum_distance
    assert number_of_items == constants.additional_items_threshold
    assert time == requests_time


def test_json_request_delivery_distance_is_None():
    '''test if the delivery distance in Json request is None'''

    requests_time = functions_for_testing.generate_iso_time(rush_hour=False)

    request_json = functions_for_testing.create_json_body(
        delivery_distance=None, time=requests_time)

    cart_value, delivery_distance, number_of_items, time = extract_the_variables(
        request_json)

    assert cart_value == constants.minimum_cart_value
    assert delivery_distance == None
    assert number_of_items == constants.additional_items_threshold
    assert time == requests_time


def test_json_request_number_of_items_is_None():
    '''test if the number of items in Json request is None'''

    requests_time = functions_for_testing.generate_iso_time(rush_hour=False)

    request_json = functions_for_testing.create_json_body(
        number_of_items=None, time=requests_time)

    cart_value, delivery_distance, number_of_items, time = extract_the_variables(
        request_json)

    assert cart_value == constants.minimum_cart_value
    assert delivery_distance == constants.minimum_distance
    assert number_of_items == None
    assert time == requests_time


def test_json_request_time_is_None():
    '''test if the time in Json request is None'''

    request_json = functions_for_testing.create_json_body(time=None)

    cart_value, delivery_distance, number_of_items, time = extract_the_variables(
        request_json)

    assert cart_value == constants.minimum_cart_value
    assert delivery_distance == constants.minimum_distance
    assert number_of_items == constants.additional_items_threshold
    assert time == None


# test if json request has a missing value


def test_json_request_cart_value_is_missing():
    '''test if the cart value in Json request is missing'''

    requests_time = functions_for_testing.generate_iso_time(rush_hour=False)

    request_json = functions_for_testing.create_json_body(
        cart_value=False, time=requests_time)

    cart_value, delivery_distance, number_of_items, time = extract_the_variables(
        request_json)

    assert cart_value == None
    assert delivery_distance == constants.minimum_distance
    assert number_of_items == constants.additional_items_threshold
    assert time == requests_time


def test_json_request_delivery_distance_is_missing():
    '''test if the delivery distance in Json request is missing'''

    requests_time = functions_for_testing.generate_iso_time(rush_hour=False)

    request_json = functions_for_testing.create_json_body(
        delivery_distance=False, time=requests_time)

    cart_value, delivery_distance, number_of_items, time = extract_the_variables(
        request_json)

    assert cart_value == constants.minimum_cart_value
    assert delivery_distance == None
    assert number_of_items == constants.additional_items_threshold
    assert time == requests_time


def test_json_request_number_of_items_is_missing():
    '''test if the number of items in Json request is missing'''

    requests_time = functions_for_testing.generate_iso_time(rush_hour=False)

    request_json = functions_for_testing.create_json_body(
        number_of_items=False, time=requests_time)

    cart_value, delivery_distance, number_of_items, time = extract_the_variables(
        request_json)

    assert cart_value == constants.minimum_cart_value
    assert delivery_distance == constants.minimum_distance
    assert number_of_items == None
    assert time == requests_time


def test_json_request_time_is_missing():
    '''test if the time in Json request is missing'''

    request_json = functions_for_testing.create_json_body(time=False)

    cart_value, delivery_distance, number_of_items, time = extract_the_variables(
        request_json)

    assert cart_value == constants.minimum_cart_value
    assert delivery_distance == constants.minimum_distance
    assert number_of_items == constants.additional_items_threshold
    assert time == None
