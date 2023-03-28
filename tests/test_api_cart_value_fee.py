from main import app

import constants
import functions_for_testing

#
""" 
# testing the cart value fee

# when:
# delivery distance 1000   (2€ charge)
# number of items is 4     (no charge)
# not in rush-hour         (no charge)

"""


def test_cart_value_under_threshold():
    '''test if cart value is 
        1 cent less than 
        the minimum cart value limit.

        in this example the result must be equal to
        1 +  minimum distance fee '''

    # make this test if minimum cart value is more
    # than 1 cent
    if constants.minimum_cart_value > 1:
        with app.test_client() as requests:
            # post request to the server
            cart_value = constants.minimum_cart_value - 1
            server_response = functions_for_testing.post_request(requests,
                                                                 cart_value=cart_value,
                                                                 rush_hour=False)

            # check the server response status code
            assert server_response.status_code == 200

            # check the result from the server
            server_result = server_response.get_json()
            true_result = 1 + constants.minimum_distance_fee
            assert server_result == {"delivery_fee": true_result}


def test_cart_value_on_threshold():
    '''test if the cart value is
        exactly the minimum cart value limit.

        in this example the result must be equal
        to the minimum distance fee only'''

    # make this test if minimum cart value is more than 0 cents
    # otherwise disable the cart value fee since
    # there is no need to this test anymore
    if constants.minimum_cart_value > 0:
        with app.test_client() as requests:
            # post request to the server
            cart_value = constants.minimum_cart_value
            server_response = functions_for_testing.post_request(requests,
                                                                 cart_value=cart_value,
                                                                 rush_hour=False)

            # check the server response status code
            assert server_response.status_code == 200

            # check the result from the server
            server_result = server_response.get_json()
            true_result = constants.minimum_distance_fee
            assert server_result == {"delivery_fee": true_result}


def test_cart_value_above_threshold():
    '''test if cart value is 
        1 cent more than 
        minimum cart value limit.

        in this example the result must be equal 
        to the minimum distance fee only'''

    with app.test_client() as requests:
        # post request to the server
        cart_value = constants.minimum_cart_value + 1
        server_response = functions_for_testing.post_request(requests,
                                                             cart_value=cart_value,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}
