from main import app
import constants
import functions_for_testing

""" 
# testing free delivery fee 

#when:
# delivery distance   1500  (so there is  3€ charge)
# number of items      13   (so there is   5,70€ charge)
# in rush-hour              (so the total fee will be multiplied by 1.2x)

"""

def test_cart_value_free_delivery_case_1():
    '''test if the user buy with 
        1 cent less than 
        free delivery threshold.

        in this example the result must be equal to 
        (delivery distance fee + number of items fee )* rush-hour fee multiplier '''

    with app.test_client() as client:
        # set the parameters
        cart_value = constants.free_delivery_threshold - 1
        delivery_distance = constants.minimum_distance + \
                            constants.additional_distance_period
        number_of_items   = constants.maximum_items_number + 1
        # client post to the server
        response = functions_for_testing.client_post(client, 
                                            cart_value=cart_value, 
                                            delivery_distance=delivery_distance,
                                            number_of_items=number_of_items,
                                            rush_hour=True)

        # check the server response status code
        assert response.status_code == 200

        # calculating the fees
        delivery_distance_fee = constants.minimum_distance_fee + \
                                constants.additional_distance_period_fee
                                
        number_of_items_fee = (((constants.maximum_items_number + 1) -
                                constants.maximum_number_of_items_without_fee) *
                                constants.additional_item_fee) + constants.bulk
        
        # if there is rush time 
        if constants.rush_times :
            fee_multiplier = constants.rush_times[0]['fee_multiplier']
        else:
            fee_multiplier = 1
        
        # check the result from the server
        
        true_result = (delivery_distance_fee + number_of_items_fee) * \
                        fee_multiplier
        server_result = response.get_json()
        assert server_result == {"delivery_fee": true_result}


def test_cart_value_free_delivery_case_2():
    '''test if the user buy with 
        exactly free delivery threshold.

        in this example the result must be equal to zero '''

    with app.test_client() as client:
        # set the parameters
        cart_value = constants.free_delivery_threshold - 1
        delivery_distance = constants.minimum_distance + \
                            constants.additional_distance_period
        number_of_items   = constants.maximum_items_number + 1
        # client post to the server
        cart_value = constants.free_delivery_threshold
        response = functions_for_testing.client_post(client, 
                                            cart_value=cart_value, 
                                            delivery_distance=delivery_distance,
                                            number_of_items=number_of_items,
                                            rush_hour=True)

        # check the server response status code
        assert response.status_code == 200

        # check the result from the server
        server_result = response.get_json()
        true_result = 0
        assert server_result == {"delivery_fee": true_result}


def test_cart_value_free_delivery_case_3():
    '''test if the user buy with 
        1000 cent more then
        free delivery threshold.

        in this example the result must be equal to zero '''

    with app.test_client() as client:
        # set the parameters
        cart_value = constants.free_delivery_threshold - 1
        delivery_distance = constants.minimum_distance + \
                            constants.additional_distance_period
        number_of_items   = constants.maximum_items_number + 1
        # client post to the server
        cart_value = constants.free_delivery_threshold + 1000
        response = functions_for_testing.client_post(client, 
                                            cart_value=cart_value, 
                                            delivery_distance=delivery_distance,
                                            number_of_items=number_of_items,
                                            rush_hour=True)

        # check the server response status code
        assert response.status_code == 200

        # check the result from the server
        server_result = response.get_json()
        true_result = 0
        assert server_result == {"delivery_fee": true_result}
