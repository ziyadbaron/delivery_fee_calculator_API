from main import app
import constants
import functions_for_testing

""" 
# testing the number of items fee

# when:
# cart_value 10€           (so there is no charge)
# delivery distance 1000   (so there is jut 2€ charge)
# not in rush-hour         (so there is no charge)

"""

def test_item_number_is_1():
    '''test if the user buy only 
        1 item.

        in this example the result must be equal to
        the minimum distance fee '''

    with app.test_client() as client:
        # client post to the server
        number_of_items = 1
        server_response = functions_for_testing.client_post(client, 
                                        number_of_items=number_of_items, 
                                        rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}


def test_item_number_threshold_case_1():
    '''test if the user buy with  
        the maximum number of items without 
        extra surcharge.

        in this example the result must be equal to
        minimum distance fee '''

    with app.test_client() as client:
        # client post to the server
        number_of_items = constants.maximum_number_of_items_without_fee
        server_response = functions_for_testing.client_post(client, 
                                        number_of_items=number_of_items, 
                                        rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}


def test_item_number_threshold_case_2():
    '''test if the user buy with  
        one item more than
        the maximum number of items without 
        extra surcharge.

        in this example the result must be equal to
        minimum distance fee + additional item fee'''

    with app.test_client() as client:
        # client post to the server
        number_of_items = constants.maximum_number_of_items_without_fee + 1
        server_response = functions_for_testing.client_post(client, 
                                        number_of_items=number_of_items, 
                                        rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee + constants.additional_item_fee
        assert server_result == {"delivery_fee": true_result}


def test_item_number_bulk_threshold_case_1():
    '''test if the user buy with  
        the maximum number of items without bulk fee.

        in this example the result must be equal to
        minimum distance fee + item number fee'''

    with app.test_client() as client:
        # client post to the server
        number_of_items = constants.maximum_items_number
        server_response = functions_for_testing.client_post(client, 
                                        number_of_items=number_of_items, 
                                        rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200
        
        # calculating the fees
        item_number_fee = (number_of_items - constants.maximum_number_of_items_without_fee) * \
                                constants.additional_item_fee
        
        # check the result from the server
        true_result = constants.minimum_distance_fee + item_number_fee
        server_result = server_response.get_json()
        assert server_result == {"delivery_fee": true_result}


def test_item_number_bulk_threshold_case_2():
    '''test if the user buy with  
        one item more than
        the maximum number of items without bulk fee.

        in this example the result must be equal to
        minimum distance fee + item number fee + bulk_fee'''

    with app.test_client() as client:
        # client post to the server
        number_of_items = constants.maximum_items_number + 1
        server_response = functions_for_testing.client_post(client, 
                                        number_of_items=number_of_items, 
                                        rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # calculating the fees
        item_number_fee = (number_of_items - constants.maximum_number_of_items_without_fee) * \
                                constants.additional_item_fee + constants.bulk
        
        # check the result from the server
        true_result = constants.minimum_distance_fee + item_number_fee
        server_result = server_response.get_json()
        assert server_result == {"delivery_fee": true_result}
