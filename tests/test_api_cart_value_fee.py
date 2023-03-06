from main import app
import constants
import functions_for_testing

""" 
# testing the cart value fee

# when:
# delivery distance 1000   (so there is jut 2€ charge)
# number of items is 4     (so there is no charge)
# not in rush-hour         (so there is no charge)

"""



def test_cart_value_under_threshold_case_1():
    '''test if the user buy with 
        300 cent less than 
        the minimum cart value limit.
        
        in this example the result must be equal to
        300 +  minimum distance fee '''

    with app.test_client() as client:
        # client post to the server
        cart_value = constants.minimum_cart_value - 300
        server_response = functions_for_testing.client_post(client, cart_value=cart_value, rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = 300 + constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}


def test_cart_value_under_threshold_case_2():
    '''test if the user buy with 
        1 cent less than 
        the minimum cart value limit.
        
        in this example the result must be equal to
        1 +  minimum distance fee '''

    with app.test_client() as client:
        # client post to the server
        cart_value = constants.minimum_cart_value - 1
        server_response = functions_for_testing.client_post(client, cart_value=cart_value, rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = 1 + constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}


def test_cart_value_free_charge_threshold():
    '''test if the user buy with the minimum 
        cart value limit.
        
        in this example the result must be equal
        to the minimum distance fee only'''

    with app.test_client() as client:
        # client post to the server
        cart_value = constants.minimum_cart_value
        server_response = functions_for_testing.client_post(client, cart_value=cart_value, rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}


def test_cart_value_above_threshold_case_1():
    '''test if the user buy with 
        1 cent more than 
        minimum cart value limit.
        
        in this example the result must be equal 
        to the minimum distance fee only'''

    with app.test_client() as client:
        # client post to the server
        cart_value = constants.minimum_cart_value + 1
        server_response = functions_for_testing.client_post(client, cart_value=cart_value, rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}
