from main import app

import constants
import functions_for_testing

#
""" 
# testing the number of items fee

# when:
# cart_value 10€           (so there is no charge)
# delivery distance 1000   (so there is 2€ charge)
# not in rush-hour         (so there is no charge)

"""


def test_item_number_one_item():
    '''test if the order has only 
        1 item.

        in this example the result must be equal to
        the minimum distance fee '''

    with app.test_client() as requests:
        # post request to the server
        number_of_items = 1
        server_response = functions_for_testing.post_request(requests,
                                                             number_of_items=number_of_items,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}


def test_item_number_under_extra_fee():
    '''test if the order has  
        the maximum number of items without 
        extra surcharge.

        in this example the result must be equal to
        minimum distance fee '''

    with app.test_client() as requests:
        # post request to the server
        number_of_items = constants.additional_items_threshold
        server_response = functions_for_testing.post_request(requests,
                                                             number_of_items=number_of_items,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}


def test_item_number_extra_item_fee():
    '''test if the order has one item more than
        the maximum number of items without 
        extra surcharge.

        in this example the result must be equal to
        minimum distance fee + additional item fee'''

    with app.test_client() as requests:
        # post request to the server
        number_of_items = constants.additional_items_threshold + 1
        server_response = functions_for_testing.post_request(requests,
                                                             number_of_items=number_of_items,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee + constants.additional_item_fee
        assert server_result == {"delivery_fee": true_result}


def test_item_number_under_bulk_fee_fee():
    '''test if the order has  
        the maximum number of items without bulk_fee fee.

        in this example the result must be equal to
        minimum distance fee +
        the the additional items fee applied according to 
        the number of the additional items'''

    with app.test_client() as requests:
        # post request to the server
        number_of_items = constants.bulk_fee_threshold
        server_response = functions_for_testing.post_request(requests,
                                                             number_of_items=number_of_items,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # calculate the fees
        item_number_fee = (number_of_items - constants.additional_items_threshold) * \
            constants.additional_item_fee

        # check the result from the server
        true_result = constants.minimum_distance_fee + item_number_fee
        server_result = server_response.get_json()
        assert server_result == {"delivery_fee": true_result}


def test_item_number_bulk_fee_fee():
    '''test if the order has  
        one item more than
        the maximum number of items without bulk_fee fee.

        in this example the result must be equal to
        minimum distance fee + item number fee + bulk_fee_fee'''

    with app.test_client() as requests:
        # post request to the server
        number_of_items = constants.bulk_fee_threshold + 1
        server_response = functions_for_testing.post_request(requests,
                                                             number_of_items=number_of_items,
                                                             rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # calculate the fees
        item_number_fee = (number_of_items - constants.additional_items_threshold) * \
            constants.additional_item_fee + constants.bulk_fee

        # check the result from the server
        true_result = constants.minimum_distance_fee + item_number_fee
        server_result = server_response.get_json()
        assert server_result == {"delivery_fee": true_result}
