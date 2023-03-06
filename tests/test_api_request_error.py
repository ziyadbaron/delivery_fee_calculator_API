from main import app
import constants

import functions_for_testing

"""
# testing if we send invalid request :

# 1 ### cart value invalid request
# when cart value is 0 or minus:
# ( 1 ) cart value 0€         (must not be 0 cent or less)
# ( 2 ) cart value -2€         (must not be 0 cent or less)
# the result will be :
status_code == 400
response = {'error': 'cart value should not be 0 cent or less.'}

# when cart value is not integer number:
# ( 3 ) cart value = "c"
# the result will be :
status_code == 400
response = {'error': "cart value should be an integer number."}

# when cart value is not exist or None:
# ( 4 ) cart value =  None                     (must not be None)
# ( 5 ) cart value Not exist in the request    (must not be not exist)
# the result will be :
status_code == 400
response = {
    'error': "cart value is missing from the request or it's assigned to None value."}
-----------------------------------------------------

# 2 ### delivery distance invalid request
#  when delivery distance is 0 or minus:
# ( 1 ) delivery distance 0      (must not be 0 meter or less)
# ( 2 ) delivery distance -500   (must not be 0 meter or less)
# the result will be :
status_code == 400
response = {'error': 'delivery distance should not be shorter than 1 meter.'}

# when delivery distance is not integer number:
# ( 3 ) delivery distance = "c"   (must be integer number)
# the result will be :
status_code == 400
response = {'error': "delivery distance should be an integer number."}


# when delivery distance is not exist or None:
# ( 4 ) delivery distance =  None                     (must not be None)
# ( 5 ) delivery distance Not exist in the request    (must not be not exist)
# the result will be :
status_code == 400
response = {
    'error': "delivery distance is missing from the request or it's assigned to None value."}
-----------------------------------------------------

# 3 ### number of items invalid request
#  when number of items is 0 or minus:
# ( 1 ) number of items is 0    (must not be 0 item)
# ( 2 ) number of items is -7   (the items must not be minus)
# the result will be :
status_code == 400
response = {'error': 'number of items should not be less than 1 item.'}

# when number of items is not integer number:
# ( 3 )number of items = "c"      (must be integer number)
# the result will be :
status_code == 400
response = {'error': "number of items should be an integer number."}

# when number of items is not exist or None:
# ( 4 ) number of items =  None                     (must not be None)
# ( 5 ) number of items Not exist in the request    (must not be not exist)
# the result will be :
status_code == 400
response = {
    'error': "number of items is missing from the request or it's assigned to None value."}
-----------------------------------------------------

# 4 ### date invalid request
#  when date format is not ISO format:
# ( 1 ) time     "2021-10-1315:00:00Z"    (time should be in ISO format.)
# ( 2 ) time     "2021-10-13T25:00:00Z"   (time should be in ISO format.)
# ( 3 ) time     "13-10-2021T15:00:00Z"   (time should be in ISO format.)
# ( 4 ) time     "2021-13-10T15:00:00Z"   (time should be in ISO format.)
# ( 5 ) time         4   (number)         (time should be in ISO format.)
# the result will be :
status_code == 400  #(Bad Request)
response = {'error': 'time should be in ISO format.'}

# when time is not exist or None:
# ( 6 ) time =  None                     (must not be None)
# ( 7 ) time Not exist in the request    (must not be not exist))
# the result will be :
status_code == 400
response = {
    'error': "time is missing from the request or it's assigned to None value."}
-----------------------------------------------------

# 5 ### if additional parameters added there is no invalid request
#  when adding additional parameters to the request:
# ( 1 )
# cart_value          10
# delivery distance   1500
# number of items is  4
# latitude            24.678
# longitude           18.9865
# time                2021-10-15T15:00:00Z
# the result will be :
status_code == 200   # (ok)
response = {'delivery_fee': 360}
-----------------------------------------------------

# 6 ### change to another directory invalid request
#  when navigate out of root directory and send request:
# ( 1 )
# directory          '/main'        (must  be the root ='/')

# the result will be :
status_code == 404  #(Not Found)
response = None
"""



################# cart value invalid request #################
# (cart value = 0)
def test_invalid_request_cart_value_1():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, cart_value=0)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {'error': 'cart value should not be 0 cent or less.'}
        assert server_result == true_result


# (cart value = -2)
def test_invalid_request_cart_value_2():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, cart_value=-2)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {'error': 'cart value should not be 0 cent or less.'}
        assert server_result == true_result


# (cart value =  "c")
def test_invalid_request_cart_value_3():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, cart_value="c")

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {'error': 'cart value should be an integer number.'}
        assert server_result == true_result

# (cart value" =  None)
def test_invalid_request_cart_value_4():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, cart_value=None)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "cart value is missing from the request or it's assigned to None value."}
        assert server_result == true_result

# (remove "cart value")
def test_invalid_request_cart_value_5():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, cart_value=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {'error': "cart value is missing from the request or it's assigned to None value."}
        assert server_result == true_result


################# delivery distance invalid request #################
# (delivery distance = 0)
def test_invalid_request_delivery_distance_1():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, delivery_distance=0)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {'error': 'delivery distance should not be shorter than 1 meter.'}
        assert server_result == true_result

# (delivery distance = -500)
def test_invalid_request_delivery_distance_2():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, delivery_distance=-500)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'delivery distance should not be shorter than 1 meter.'}
        assert server_result == true_result

# (delivery distance = "c")
def test_invalid_request_delivery_distance_3():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, delivery_distance="c")

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'delivery_distance should be an integer number.'}
        assert server_result == true_result

# (delivery distance = None)
def test_invalid_request_delivery_distance_4():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, delivery_distance=None)

        # check the server response status code
        assert server_response.status_code == 400

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "delivery distance is missing from the request or it's assigned to None value."}
        assert server_result == true_result

# (remove delivery distance)
def test_invalid_request_delivery_distance_5():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, delivery_distance=False)

        # check the server response status code
        assert server_response.status_code == 400

        # check the result from the server
        server_result = server_response.get_json()
        true_result = {'error': "delivery distance is missing from the request or it's assigned to None value."}
        assert server_result == true_result



################# number of items invalid request #################
# (number of items = 0)
def test_invalid_request_number_of_items_1():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, number_of_items=0)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'number of items should not be less than 1 item.'}
        assert server_result == true_result

# (number of items = -7)
def test_invalid_request_number_of_items_2():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, number_of_items=-7)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'number of items should not be less than 1 item.'}
        assert server_result == true_result

# (number of items =  "c")
def test_invalid_request_number_of_items_3():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, number_of_items="c")

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'number of items should be an integer number.'}
        assert server_result == true_result

# (number of items = None)
def test_invalid_request_number_of_items_4():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, number_of_items=None)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "number of items is missing from the request or it's assigned to None value."}
        assert server_result == true_result

# remove "number of items"
def test_invalid_request_number_of_items_5():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, number_of_items=False)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "number of items is missing from the request or it's assigned to None value."}
        assert server_result == true_result



################# date format invalid request #################
# (time = "2021-10-1315:00:00Z")
def test_invalid_request_date_format_1():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, special_time_format=True,
                                        client_time="2021-10-1315:00:00Z")

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'time should be in ISO format.'}
        assert server_result == true_result

# (time = "2021-10-13T25:00:00Z")
def test_invalid_request_date_format_2():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, special_time_format=True, 
                                        client_time="2021-10-13T25:00:00Z")

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'time should be in ISO format.'}
        assert server_result == true_result

# (time = "13-10-2021T15:00:00Z")
def test_invalid_request_date_format_3():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, special_time_format=True, 
                                        client_time="13-10-2021T15:00:00Z")

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'time should be in ISO format.'}
        assert server_result == true_result

# (time = "2021-13-10T15:00:00Z")
def test_invalid_request_date_format_4():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, special_time_format=True,
                                        client_time= "2021-13-10T15:00:00Z")

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': 'time should be in ISO format.'}
        assert server_result == true_result

# (time =  4)
def test_invalid_request_date_format_5():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, special_time_format=True, 
                                        client_time=4)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {'error': 'time should be in ISO format.'}
        assert server_result == true_result

# (time =  None)
def test_invalid_request_date_format_6():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, special_time_format=True, 
                                        client_time=None)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "date is missing from the request or it's assigned to None value."}
        assert server_result == true_result

# remove the time from the request
def test_invalid_request_date_format_7():

    with app.test_client() as client:
        # client post to the server
        server_response = functions_for_testing.client_post(client, time_missing=True)

        # check the server response status code
        assert server_response.status_code == 400  # (Bad Request)
        
        # check the result from the server
        server_result = server_response.get_json()
        true_result = {
            'error': "date is missing from the request or it's assigned to None value."}
        assert server_result == true_result




# add additional parameters ("latitude":24.678,"longitude":18.9865,)
def test_invalid_request_add_parameters():

    with app.test_client() as c:

        time = functions_for_testing.generate_iso_time(rush_hour=False)

        server_response = c.post(constants.PATH, 
                                    json={"cart_value": constants.minimum_cart_value,
                                    "delivery_distance": constants.minimum_distance,
                                    "number_of_items": constants.maximum_number_of_items_without_fee,
                                    "latitude": 24.678,
                                    "longitude": 18.9865,
                                    "time": time})

        # check the server response status code
        assert server_response.status_code == 200  # (ok)

        # check the result from the server
        server_result = server_response.get_json()

        true_result = constants.minimum_distance_fee 
        assert server_result == {'delivery_fee': true_result}


# change root directory =(/mean) invalid request
def test_invalid_request_change_root_directory():

    time = functions_for_testing.generate_iso_time(rush_hour=True)

    with app.test_client() as c:
        server_response = c.post('/main', json={"cart_value": constants.minimum_cart_value,
                                     "delivery_distance": constants.minimum_distance,
                                     "number_of_items": constants.maximum_number_of_items_without_fee,
                                     "time": time})

        server_result = server_response.get_json()
        assert server_response.status_code == 404  # (Not Found)
        assert server_result == None



# 488