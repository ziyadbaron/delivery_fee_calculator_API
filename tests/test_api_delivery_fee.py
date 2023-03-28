from main import app

import constants
import functions_for_testing

#
""" 
# testing the delivery distance fee

# when:
# cart_value is 10€     (there is no charge)
# number of items is 4  (there is no charge)
# not in rush-hour      (there is no charge)

"""


def test_delivery_distance_without_extra_fee():
    '''test if the delivery distance is under 
        the first fixed distance period.

        in this example the result must be equal to
        the minimum distance fee '''

    with app.test_client() as requests:
        # set delivery distance to be less than minimum distance
        delivery_distance = constants.minimum_distance - 1
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance=delivery_distance,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}


def test_delivery_distance_extra_fee_threshold():
    '''test if the delivery distance is 
        exactly the first fixed distance period.

        in this example the result must be equal to
        the minimum distance fee '''

    with app.test_client() as requests:
        # post request to the server
        delivery_distance = constants.minimum_distance
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance=delivery_distance,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}


def test_delivery_distance_with_extra_fee():
    '''test if the delivery distance is over 
        the first fixed distance period .

        in this example the result must be equal to
        the minimum distance fee + 
        additional distance period fee'''

    with app.test_client() as requests:
        # set the test distance to be 1 meter taller than the minimum distance
        delivery_distance = constants.minimum_distance + 1
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance=delivery_distance,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee + \
            constants.additional_period_fee
        assert server_result == {"delivery_fee": true_result}


def test_delivery_distance_under_additional_period():
    '''test if the delivery distance is 
        1 metres under 
        the first fixed distance period + 
        the additional distance period.

        in this example the result must be equal to
        the minimum distance fee + 
        additional distance period fee'''

    with app.test_client() as requests:
        # Set the test distance to 1 metres under the first fixed distance period +
        # the additional distance period
        delivery_distance = (constants.minimum_distance +
                             constants.additional_distance_period) - 1
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance=delivery_distance,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee + \
            constants.additional_period_fee
        assert server_result == {"delivery_fee": true_result}


def test_delivery_distance_additional_period_threshold():
    '''test if the delivery distance is
        the first fixed distance period  + 
        the additional distance period.

        in this example the result must be equal to
        the minimum distance fee + 
        additional distance period fee'''

    with app.test_client() as requests:
        # Set the test distance to the first fixed distance period +
        # the additional distance period
        delivery_distance = (constants.minimum_distance +
                             constants.additional_distance_period)
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance=delivery_distance,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee + \
            constants.additional_period_fee
        assert server_result == {"delivery_fee": true_result}


def test_delivery_distance_over_additional_period():
    '''test if the delivery distance is 
        1 metres over 
        the first fixed distance period  + 
        the additional distance period.

        in this example the result must be equal to
        the minimum distance fee + 
        (2 * additional distance period fee)'''

    with app.test_client() as requests:
        # Set the test distance to 1 metres over the first fixed distance period +
        # the additional distance period
        delivery_distance = (constants.minimum_distance +
                             constants.additional_distance_period) + 1
        # post request to the server
        server_response = functions_for_testing.post_request(requests,
                                                             delivery_distance=delivery_distance,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee + \
            (2*constants.additional_period_fee)
        assert server_result == {"delivery_fee": true_result}
