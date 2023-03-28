from main import app

import functions_for_testing

#
"""
# test if the request is invalid
"""


################# cart value invalid request #################

def test_invalid_request_cart_value_zero():
    '''test if the cart value is 
        0 cent.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             cart_value=0,
                                                             special_cart_value=True,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {'error': 'cart value should not be 0 cent or less.'}
        assert server_result == true_result


def test_invalid_request_cart_value_minus():
    '''test if the cart value is 
        -2 cent.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             cart_value=-2,
                                                             special_cart_value=True,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {'error': 'cart value should not be 0 cent or less.'}
        assert server_result == true_result


def test_invalid_request_cart_value_string():
    '''test if the cart value is 
        "c" string.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             cart_value="c",
                                                             special_cart_value=True,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {'error': 'cart value should be an integer number.'}
        assert server_result == true_result


def test_invalid_request_cart_value_none():
    '''test if the cart value is 
        None.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             cart_value=None,
                                                             special_cart_value=True,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "cart value is missing from the request or it's assigned to None value."}
        assert server_result == true_result


def test_invalid_request_cart_value_empty():
    '''test if the cart value does 
        not exist in the request.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             cart_value=False,
                                                             special_cart_value=True,
                                                             rush_hour=False,)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "cart value is missing from the request or it's assigned to None value."}
        assert server_result == true_result


################# delivery distance invalid request #################

def test_invalid_request_delivery_distance_zero():
    '''test if the delivery distance is 
        0 meter.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance=0,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'delivery distance should not be shorter than 1 meter.'}
        assert server_result == true_result


def test_invalid_request_delivery_distance_minus():
    '''test if the delivery distance is 
        -500 metres.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance=-500,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'delivery distance should not be shorter than 1 meter.'}
        assert server_result == true_result


def test_invalid_request_delivery_distance_string():
    '''test if the delivery distance is 
        "c" string.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance="c",
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'delivery distance should be an integer number.'}
        assert server_result == true_result


def test_invalid_request_delivery_distance_none():
    '''test if the delivery distance is 
        None.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance=None,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "delivery distance is missing from the request or it's assigned to None value."}
        assert server_result == true_result


def test_invalid_request_delivery_distance_empty():
    '''test if the delivery distance does 
        not exist in the request.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance=False,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "delivery distance is missing from the request or it's assigned to None value."}
        assert server_result == true_result


################# number of items invalid request #################

def test_invalid_request_number_of_items_zero():
    '''test if the number of items is 
        0.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             number_of_items=0,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'number of items should not be less than 1 item.'}
        assert server_result == true_result


def test_invalid_request_number_of_items_minus():
    '''test if the number of items is 
        -7 items.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             number_of_items=-7,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'number of items should not be less than 1 item.'}
        assert server_result == true_result


def test_invalid_request_number_of_items_string():
    '''test if the number of items is 
        "c" string.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             number_of_items="c",
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'number of items should be an integer number.'}
        assert server_result == true_result


def test_invalid_request_number_of_items_none():
    '''test if the number of items is 
        None.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             number_of_items=None,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "number of items is missing from the request or it's assigned to None value."}
        assert server_result == true_result


def test_invalid_request_number_of_items_empty():
    '''test if the number of items does 
        not exist in the request.

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             number_of_items=False,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "number of items is missing from the request or it's assigned to None value."}
        assert server_result == true_result


################# date format invalid request #################

def test_invalid_request_date_format_1():
    '''test if the time is invalid
        "2021-10-1315:00:00Z". the right is("2021-10-13T15:00:00Z")

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             rush_hour=None,
                                                             time="2021-10-1315:00:00Z")

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'time should be in ISO format.'}
        assert server_result == true_result


def test_invalid_request_date_format_2():
    '''test if the time is invalid
        "2021-10-13T25:00:00Z". (the day can not have 25 hours)

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             rush_hour=None,
                                                             time="2021-10-13T25:00:00Z")

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'time should be in ISO format.'}
        assert server_result == true_result


def test_invalid_request_date_format_3():
    '''test if the time is invalid
        "13-10-2021T15:00:00Z". the right is(2021-10-13T15:00:00Z)

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             rush_hour=None,
                                                             time="13-10-2021T15:00:00Z")

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'time should be in ISO format.'}
        assert server_result == true_result


def test_invalid_request_date_format_4():
    '''test if the time is invalid
        "2021-13-10T15:00:00Z". (the year can not have 13 months)

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             rush_hour=None,
                                                             time="2021-13-10T15:00:00Z")

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'time should be in ISO format.'}
        assert server_result == true_result


def test_invalid_request_date_format_5():
    '''test if the time is 
        number 4. 

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             rush_hour=None,
                                                             time=4)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {'error': 'time should be in ISO format.'}
        assert server_result == true_result


def test_invalid_request_date_format_none():
    '''test if the time is 
        None. 

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             rush_hour=None,
                                                             time=None)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "date is missing from the request or it's assigned to None value."}
        assert server_result == true_result


def test_invalid_request_date_format_empty():
    '''test if the time does 
        not exist in the request. 

        in this example the result must be
        error message 
        and status_code == 400
    '''

    with app.test_client() as requests:
        time = False
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             rush_hour=None,
                                                             time=time)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "date is missing from the request or it's assigned to None value."}
        assert server_result == true_result
