from main import app

import constants
import functions_for_testing

#
""" 
# testing free delivery fee 

#when:
# delivery distance 1000   (so there is jut 2€ charge)
# number of items      13   (so there is   5,70€ charge)
# not in rush-hour         (so there is no charge)

"""


def test_cart_value_under_free_delivery_threshold():
    '''test if the cart value is 
        1 cent less than 
        free delivery threshold.

        in this example the result must be equal to 
        delivery distance fee + 
        number of items fee '''

    with app.test_client() as requests:
        # set the parameters
        cart_value = constants.free_delivery_threshold - 1
        number_of_items = constants.bulk_fee_threshold + 1

        # post request to the server
        response = functions_for_testing.post_request(requests,
                                                      cart_value=cart_value,
                                                      number_of_items=number_of_items,
                                                      rush_hour=False)

        # check the server response status code
        assert response.status_code == 200

        # calculating the fees
        delivery_distance_fee = constants.minimum_distance_fee

        number_of_items_fee = (((constants.bulk_fee_threshold + 1) -
                                constants.additional_items_threshold) *
                               constants.additional_item_fee) + constants.bulk_fee

        # check the result from the server
        true_result = delivery_distance_fee + number_of_items_fee
        server_result = response.get_json()
        assert server_result == {"delivery_fee": true_result}


def test_cart_value_on_free_delivery_threshold():
    '''test if the cart value is 
        exactly free delivery threshold.

        in this example the result must be equal to zero '''

    with app.test_client() as requests:
        # set the parameters
        cart_value = constants.free_delivery_threshold
        number_of_items = constants.bulk_fee_threshold + 1

        # post request to the server
        response = functions_for_testing.post_request(requests,
                                                      cart_value=cart_value,
                                                      special_cart_value=True,
                                                      number_of_items=number_of_items,
                                                      rush_hour=False)

        # check the server response status code
        assert response.status_code == 200

        # check the result from the server
        server_result = response.get_json()
        true_result = 0
        assert server_result == {"delivery_fee": true_result}


def test_cart_value_over_free_delivery_threshold():
    '''test if the cart value is 
        1000 cent more then
        free delivery threshold.

        in this example the result must be equal to zero '''

    with app.test_client() as requests:
        # set the parameters
        cart_value = constants.free_delivery_threshold + 1000
        number_of_items = constants.bulk_fee_threshold + 1

        # post request to the server
        response = functions_for_testing.post_request(requests,
                                                      cart_value=cart_value,
                                                      special_cart_value=True,
                                                      number_of_items=number_of_items,
                                                      rush_hour=False)

        # check the server response status code
        assert response.status_code == 200

        # check the result from the server
        server_result = response.get_json()
        true_result = 0
        assert server_result == {"delivery_fee": true_result}
