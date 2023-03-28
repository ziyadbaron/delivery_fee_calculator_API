from main import app

import constants
import functions_for_testing

#
""" 
# testing the maximum delivery fee threshold
"""


def test_maximum_fee_1():
    '''test if the delivery distance is 
        800000 metre.

        in this example the result must be equal to
        The maximum delivery fee threshold '''

    with app.test_client() as requests:
        # set the parameters
        delivery_distance = 800000

        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance=delivery_distance,
                                                             rush_hour=False,)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.maximum_delivery_fee
        assert server_result == {"delivery_fee": true_result}


def test_maximum_fee_2():
    '''test if the number of items is 
        800000 items.

        in this example the result must be equal to
        The maximum delivery fee threshold '''

    with app.test_client() as requests:
        # set the parameters
        number_of_items = 800000

        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             number_of_items=number_of_items,
                                                             rush_hour=False,)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.maximum_delivery_fee
        assert server_result == {"delivery_fee": true_result}
