from main import app
import constants
import functions_for_testing

""" 
# testing the delivery distance fee

# when:
# cart_value is 10€     (so there is no charge)
# number of items is 4  (so there is no charge)
# not in rush-hour      (so there is no charge)

"""


def client_post(client, delivery_distance, rush_hour):

    # generates time in ISO format automatically in or out rush-hour time
    # depending on rush-hour time constants
    time = functions_for_testing.generate_iso_time(rush_hour)
    print('### delivery_distance ### time #####', time)

    # send post to server and return the response
    server_response = client.post(constants.PATH,
                                  json={"cart_value": constants.minimum_cart_value,
                                        "delivery_distance": delivery_distance,
                                        "number_of_items": constants. maximum_number_of_items_without_fee,
                                        "time": time})
    # "2021-10-13T13:00:00Z"

    return server_response


def test_delivery_distance_first_period_case_1():
    '''test if the delivery distance is 
        only 1 metre.

        in this example the result must be equal to
        the minimum distance fee '''

    with app.test_client() as client:
        # client post to the server
        delivery_distance = 1
        server_response = functions_for_testing.client_post(
            client, delivery_distance=delivery_distance, rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}


def test_delivery_distance_first_period_case_2():
    '''test if the delivery distance is 
        exactly the first fixed distance period.

        in this example the result must be equal to
        the minimum distance fee '''

    with app.test_client() as client:
        # client post to the server
        delivery_distance = constants.minimum_distance
        server_response = functions_for_testing.client_post(
            client, delivery_distance=delivery_distance, rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee
        assert server_result == {"delivery_fee": true_result}


def test_delivery_distance_first_period_case_3():
    '''test if the delivery distance is 
        the first fixed distance period + 1 .

        in this example the result must be equal to
        the minimum distance fee + additional distance period fee'''

    with app.test_client() as client:
        # client post to the server
        delivery_distance = constants.minimum_distance + 1
        server_response = functions_for_testing.client_post(
            client, delivery_distance=delivery_distance, rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee + \
            constants.additional_distance_period_fee
        assert server_result == {"delivery_fee": true_result}


def test_delivery_distance_additional_distance_case_1():
    '''test if the delivery distance is 
        1 metres under 
        the first fixed distance period + 
        the additional distance period.

        in this example the result must be equal to
        the minimum distance fee + additional distance period fee'''

    with app.test_client() as client:
        # client post to the server
        delivery_distance = (constants.minimum_distance +
                             constants.additional_distance_period) - 1
        server_response = functions_for_testing.client_post(
            client, delivery_distance=delivery_distance, rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee + \
            constants.additional_distance_period_fee
        assert server_result == {"delivery_fee": true_result}


def test_delivery_distance_additional_distance_case_2():
    '''test if the delivery distance is
        the first fixed distance period  + 
        the additional distance period.

        in this example the result must be equal to
        the minimum distance fee + additional distance period fee'''

    with app.test_client() as client:
        # client post to the server
        delivery_distance = constants.minimum_distance + \
            constants.additional_distance_period
        server_response = functions_for_testing.client_post(
            client, delivery_distance=delivery_distance, rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee + \
            constants.additional_distance_period_fee
        assert server_result == {"delivery_fee": true_result}


def test_delivery_distance_additional_distance_case_3():
    '''test if the delivery distance is 
        1 metres over 
        the first fixed distance period  + 
        the additional distance period.

        in this example the result must be equal to
        the minimum distance fee + (2*additional distance period fee)'''

    with app.test_client() as client:
        # client post to the server
        delivery_distance = constants.minimum_distance + \
            constants.additional_distance_period + 1
        server_response = functions_for_testing.client_post(
            client, delivery_distance=delivery_distance, rush_hour=False)

        # check the server response status code
        assert server_response.status_code == 200

        # check the result from the server
        server_result = server_response.get_json()
        true_result = constants.minimum_distance_fee + \
            (2*constants.additional_distance_period_fee)
        assert server_result == {"delivery_fee": true_result}
