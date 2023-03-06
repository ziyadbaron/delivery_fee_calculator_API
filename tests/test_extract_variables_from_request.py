from functions import extract_the_variables


'''testing extract_the_variables function'''


def create_json (cart_value=1000, delivery_distance=1500, number_of_items=4, time="2021-10-13T13:00:00Z"):
    # deleted from json body the variable have Boolean False value
    if not cart_value:
        request_json = {
                "delivery_distance": delivery_distance,
                "number_of_items": number_of_items,
                "time": time}
        return request_json
    
    elif not delivery_distance:
        request_json = {"cart_value": cart_value,
                        "number_of_items": number_of_items,
                        "time": time}
        return request_json
    
    elif not number_of_items:
        request_json = {"cart_value": cart_value,
                        "delivery_distance": delivery_distance,
                        "time": time}
        return request_json
    
    elif not time:
        request_json = {"cart_value": cart_value,
                        "delivery_distance": delivery_distance,
                        "number_of_items": number_of_items}
        return request_json
    
    request_json = {"cart_value": cart_value,
                    "delivery_distance": delivery_distance,
                    "number_of_items": number_of_items,
                    "time": time}
    return request_json

# correct request body
def test_json_request_is_correct():
    '''testing if the Json request is correct (normal)'''

    request_json = create_json ()

    cart_value, delivery_distance, number_of_items, time = extract_the_variables(request_json)
    assert cart_value == 1000
    assert delivery_distance == 1500
    assert number_of_items == 4
    assert time ==  "2021-10-13T13:00:00Z"


# testing if json request have None value
def test_json_request_cart_value_is_None():
    '''testing if the cart value in Json request is None'''

    request_json = create_json (cart_value=None)
    
    cart_value, delivery_distance, number_of_items, time = extract_the_variables(request_json)
    assert cart_value == None
    assert delivery_distance == 1500
    assert number_of_items == 4
    assert time ==  "2021-10-13T13:00:00Z"

def test_json_request_delivery_distance_is_None():
    '''testing if the delivery distance in Json request is None'''

    request_json = create_json (delivery_distance=None)
    
    cart_value, delivery_distance, number_of_items, time = extract_the_variables(request_json)
    assert cart_value == 1000
    assert delivery_distance == None
    assert number_of_items == 4
    assert time ==  "2021-10-13T13:00:00Z"

def test_json_request_number_of_items_is_None():
    '''testing if the number of items in Json request is None'''

    request_json = create_json (number_of_items=None)
    
    cart_value, delivery_distance, number_of_items, time = extract_the_variables(request_json)
    assert cart_value == 1000
    assert delivery_distance == 1500
    assert number_of_items == None
    assert time ==  "2021-10-13T13:00:00Z"

def test_json_request_time_is_None():
    '''testing if the time in Json request is None'''

    request_json = create_json (time=None)
    
    cart_value, delivery_distance, number_of_items, time = extract_the_variables(request_json)
    assert cart_value == 1000
    assert delivery_distance == 1500
    assert number_of_items == 4
    assert time ==  None





# testing if json request have missing value
def test_json_request_cart_value_is_missing():
    '''testing if the cart value in Json request is missing'''

    request_json = create_json (cart_value=False)
    
    cart_value, delivery_distance, number_of_items, time = extract_the_variables(request_json)
    assert cart_value == None
    assert delivery_distance == 1500
    assert number_of_items == 4
    assert time ==  "2021-10-13T13:00:00Z"

def test_json_request_delivery_distance_is_missing():
    '''testing if the delivery distance in Json request is missing'''

    request_json = create_json (delivery_distance=False)
    
    cart_value, delivery_distance, number_of_items, time = extract_the_variables(request_json)
    assert cart_value == 1000
    assert delivery_distance == None
    assert number_of_items == 4
    assert time ==  "2021-10-13T13:00:00Z"

def test_json_request_number_of_items_is_missing():
    '''testing if the number of items in Json request is missing'''

    request_json = create_json (number_of_items=False)
    
    cart_value, delivery_distance, number_of_items, time = extract_the_variables(request_json)
    assert cart_value == 1000
    assert delivery_distance == 1500
    assert number_of_items == None
    assert time ==  "2021-10-13T13:00:00Z"

def test_json_request_time_is_missing():
    '''testing if the time in Json request is missing'''

    request_json = create_json (time=False)
    
    cart_value, delivery_distance, number_of_items, time = extract_the_variables(request_json)
    assert cart_value == 1000
    assert delivery_distance == 1500
    assert number_of_items == 4
    assert time ==  None


