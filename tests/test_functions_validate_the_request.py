from functions import validate_the_request_body

'''testing validate_the_request_body function'''

# correct request body
def test_validate_the_request_body_correct():
    '''testing if the request body is correct (normal)'''
    result = validate_the_request_body(5, 111, 4, "2021-10-20T17:17:00Z")
    assert result == (False, "")


# cart value error
def test_validate_the_request_body_cart_value_none():
    '''test if the cart value is None'''
    result = validate_the_request_body(None, 111, 4, "2021-10-20T17:17:00Z")
    assert result == (True, "cart value is missing from the request or it's assigned to None value.")

def test_validate_the_request_body_cart_value_string():
    '''test if the cart value is string'''
    result = validate_the_request_body('cbh', 111, 4, "2021-10-20T17:17:00Z")
    assert result == (True, "cart value should be an integer number.")

def test_validate_the_request_body_cart_value_empty_string():
    '''test if the cart value is empty string'''
    result = validate_the_request_body('', 111, 4, "2021-10-20T17:17:00Z")
    assert result == (True, "cart value should be an integer number.")

def test_validate_the_request_body_cart_value_list():
    '''test if the cart value is a list'''
    result = validate_the_request_body([1, 2, 4], 111, 4, "2021-10-20T17:17:00Z")
    assert result == (True, "cart value should be an integer number.")

def test_validate_the_request_body_cart_value_tuple():
    '''test if the cart value is a tuple'''
    result = validate_the_request_body((1, 2, 4), 111, 4, "2021-10-20T17:17:00Z")
    assert result == (True, "cart value should be an integer number.")

def test_validate_the_request_body_cart_value_zero():
    '''test if the cart value is zero'''
    result = validate_the_request_body(0, 111, 4, "2021-10-20T17:17:00Z")
    assert result == (True, "cart value should not be 0 cent or less.")

def test_validate_the_request_body_cart_value_minus():
    '''test if the cart value is minus number'''
    result = validate_the_request_body(-4, 111, 4, "2021-10-20T17:17:00Z")
    assert result == (True, "cart value should not be 0 cent or less.")


# delivery distance error
def test_validate_the_request_body_delivery_distance_none():
    '''test if the delivery distance is None'''
    result = validate_the_request_body(5, None, 4, "2021-10-20T17:17:00Z")
    assert result == (True, "delivery distance is missing from the request or it's assigned to None value.")

def test_validate_the_request_body_delivery_distance_string():
    '''test if the delivery distance is string'''
    result = validate_the_request_body(5, 'cbh', 4, "2021-10-20T17:17:00Z")
    assert result == (True, "delivery_distance should be an integer number.")

def test_validate_the_request_body_delivery_distance_empty_string():
    '''test if the delivery distance is empty string'''
    result = validate_the_request_body(5, '', 4, "2021-10-20T17:17:00Z")
    assert result == (True, "delivery_distance should be an integer number.")

def test_validate_the_request_body_delivery_distance_list():
    '''test if the delivery distance is a list'''
    result = validate_the_request_body(5, [1, 2, 4], 4, "2021-10-20T17:17:00Z")
    assert result == (True, "delivery_distance should be an integer number.")

def test_validate_the_request_body_delivery_distance_tuple():
    '''test if the delivery distance is a tuple'''
    result = validate_the_request_body(5, (1, 2, 4), 4, "2021-10-20T17:17:00Z")
    assert result == (True, "delivery_distance should be an integer number.")

def test_validate_the_request_body_delivery_distance_zero():
    '''test if the delivery distance is zero'''
    result = validate_the_request_body(5, 0, 4, "2021-10-20T17:17:00Z")
    assert result == (True, "delivery distance should not be shorter than 1 meter.")

def test_validate_the_request_body_delivery_distance_minus():
    '''test if the delivery distance is minus number'''
    result = validate_the_request_body(5, -4, 4, "2021-10-20T17:17:00Z")
    assert result == (True, "delivery distance should not be shorter than 1 meter.")


# number of items error
def test_validate_the_request_body_number_of_items_none():
    '''test if the number of items is None'''
    result = validate_the_request_body(5, 111, None, "2021-10-20T17:17:00Z")
    assert result == (True, "number of items is missing from the request or it's assigned to None value.")

def test_validate_the_request_body_number_of_items_string():
    '''test if the number of items is string'''
    result = validate_the_request_body(5, 111, 'cbh', "2021-10-20T17:17:00Z")
    assert result == (True, "number of items should be an integer number.")

def test_validate_the_request_body_number_of_items_empty_string():
    '''test if the number of items is empty string'''
    result = validate_the_request_body(5, 111, '', "2021-10-20T17:17:00Z")
    assert result == (True, "number of items should be an integer number.")

def test_validate_the_request_body_number_of_items_list():
    '''test if the number of items is a list'''
    result = validate_the_request_body(5, 111, [1, 2, 4], "2021-10-20T17:17:00Z")
    assert result == (True, "number of items should be an integer number.")

def test_validate_the_request_body_number_of_items_tuple():
    '''test if the number of items is a tuple'''
    result = validate_the_request_body(5, 111, (1, 2, 4), "2021-10-20T17:17:00Z")
    assert result == (True, "number of items should be an integer number.")

def test_validate_the_request_body_number_of_items_zero():
    '''test if the number of items is zero'''
    result = validate_the_request_body(5, 111, 0, "2021-10-20T17:17:00Z")
    assert result == (True, "number of items should not be less than 1 item.")

def test_validate_the_request_body_number_of_items_minus():
    '''test if the number of items is minus number'''
    result = validate_the_request_body(5, 111, -4, "2021-10-20T17:17:00Z")
    assert result == (True, "number of items should not be less than 1 item.")


# time error
def test_validate_the_request_body_time_none():
    '''test if the time is None'''
    result = validate_the_request_body(5, 111, 4, None)
    assert result == (True, "date is missing from the request or it's assigned to None value.")

def test_validate_the_request_body_time_random_string():
    '''test if the time is string'''
    result = validate_the_request_body(5, 111, 4, 'cbh')
    assert result == (True, "time should be in ISO format.")

def test_validate_the_request_body_time_empty_string():
    '''test if the time is empty string'''
    result = validate_the_request_body(5, 111, 4, '')
    assert result == (True, "time should be in ISO format.")

def test_validate_the_request_body_time_list():
    '''test if the time is a list'''
    result = validate_the_request_body(5, 111, 4, [1, 2, 4])
    assert result == (True, "time should be in ISO format.")

def test_validate_the_request_body_time_tuple():
    '''test if the time is a tuple'''
    result = validate_the_request_body(5, 111, 4, (1, 2, 4))
    assert result == (True, "time should be in ISO format.")

def test_validate_the_request_body_time_zero():
    '''test if the time is zero'''
    result = validate_the_request_body(5, 111, 4, 0)
    assert result == (True, "time should be in ISO format.")




