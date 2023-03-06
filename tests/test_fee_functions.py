import constants
import functions
import functions_for_testing


'''testing all the fees functions'''

# testing cart value fee
def test_add_cart_value_fee_under_the_limit():
    '''testing if the cart value is under the limit '''
    delivery_fee = 0
    cart_value =  0
    result = functions.add_cart_value_fee(cart_value, delivery_fee)
    assert result == constants.minimum_cart_value

def test_add_cart_value_fee_on_the_limit():
    '''testing if the cart value is exactly on the limit (1000 cents)'''
    delivery_fee = 0
    cart_value = constants.minimum_cart_value
    result = functions.add_cart_value_fee(cart_value, delivery_fee)
    assert result == 0

def test_add_cart_value_fee_over_the_limit():
    '''testing if the cart value is over the limit (1000 cents)'''
    delivery_fee = 0
    cart_value = constants.minimum_cart_value + 100
    result = functions.add_cart_value_fee(cart_value, delivery_fee)
    assert result == 0



# testing delivery distance fee
def test_add_delivery_distance_fee_under_the_limit():
    '''testing if the delivery distance is under the limit
    
        the result must be the minimum delivery distance fee'''
    delivery_fee = 0
    delivery_distance = constants.minimum_distance - 1
    result = functions.add_delivery_distance_fee(delivery_distance, delivery_fee)
    
    # the result must be the minimum delivery distance fee
    true_result = constants.minimum_distance_fee
    assert result == true_result

def test_add_delivery_distance_fee_on_the_limit():
    '''testing if the delivery distance is on the limit 
    
        the result must be the minimum delivery distance fee'''
    delivery_fee = 0
    delivery_distance = constants.minimum_distance
    result = functions.add_delivery_distance_fee(delivery_distance, delivery_fee)
    
    # the result must be the minimum delivery distance fee
    true_result = constants.minimum_distance_fee
    assert result == true_result

def test_add_delivery_distance_fee_over_the_limit_1():
    '''testing if the delivery distance is 1 meter over the limit
    
    the result must be 
    the minimum delivery distance fee + one period additional fee'''
    delivery_fee = 0
    delivery_distance = constants.minimum_distance + 1
    result = functions.add_delivery_distance_fee(delivery_distance, delivery_fee)
    
    # the result must be the minimum delivery distance fee plus one period additional fee
    true_result = constants.minimum_distance_fee + constants.additional_distance_period_fee
    assert result == true_result

def test_add_delivery_distance_fee_over_the_limit_2():
    '''testing if the delivery distance is one period over the limit 
    
    the result must be :
    the minimum delivery distance fee + one period additional fee'''
    delivery_fee = 0
    delivery_distance = constants.minimum_distance + constants.additional_distance_period
    result = functions.add_delivery_distance_fee(delivery_distance, delivery_fee)
    
    # the result must be the minimum delivery distance fee plus one period additional fee
    true_result = constants.minimum_distance_fee + constants.additional_distance_period_fee
    assert result == true_result

def test_add_delivery_distance_fee_over_the_limit_3():
    '''testing if the delivery distance is one period plus 1 over the limit 
    
    the result must be :
    the minimum delivery distance fee + (2* periods additional fee)'''
    delivery_fee = 0
    delivery_distance = constants.minimum_distance + constants.additional_distance_period + 1
    result = functions.add_delivery_distance_fee(delivery_distance, delivery_fee)
    
    # the result must be the minimum delivery distance fee plus two periods additional fee
    true_result = constants.minimum_distance_fee + (2 * constants.additional_distance_period_fee)
    assert result == true_result


# testing additional items fee
def test_add_additional_items_fee_under_the_limit():
    '''testing if the additional items is under the limit 
    
    the result must be zero'''
    delivery_fee = 0
    number_of_items = constants.maximum_number_of_items_without_fee
    result = functions.add_additional_items_fee(number_of_items, delivery_fee)
    assert result == 0

def test_add_additional_items_fee_over_the_limit_1():
    '''testing if one items is over the limit 
    
    the result must be :
    additional item fee applied one time'''
    delivery_fee = 0
    number_of_items = constants.maximum_number_of_items_without_fee + 1
    result = functions.add_additional_items_fee(number_of_items, delivery_fee)
    
    # the result must be additional item fee applied one time
    true_result = constants.additional_item_fee
    assert result == true_result

def test_add_additional_items_fee_over_the_limit_2():
    '''testing if 3 items is over the limit 
    
    the result must be :
    additional item fee applied 3 times'''
    delivery_fee = 0
    number_of_items = constants.maximum_number_of_items_without_fee + 3
    result = functions.add_additional_items_fee(number_of_items, delivery_fee)
    
    # the result must be additional item fee applied 3 times
    true_result = constants.additional_item_fee * 3
    assert result == true_result

def test_add_additional_items_fee_over_the_limit_bulk():
    '''testing if the additional items is over the maximum number 
    of items so it must add the bulk(1,20€)
    
    the result must be :
    the fee applied as the number of the additional items + the bulk fee'''
    delivery_fee = 0
    number_of_items = constants.maximum_items_number + 1
    result = functions.add_additional_items_fee(number_of_items, delivery_fee)
    
    # the result must be the fee applied as the number of the additional items plus the bulk fee
    additional_item_number = number_of_items - constants.maximum_number_of_items_without_fee 
    true_result = (constants.additional_item_fee * additional_item_number) + constants.bulk
    assert result == true_result


# testing rush hour fee
def test_add_rush_hour_fee_last_minint_before_rush_hour_time():
    '''testing if the time is a minint before rush hour:
    friday 2:59'''
    delivery_fee = 100
    
    # Make the test for every day have a rush hour
    for rush_time in constants.rush_times :
        day_name = rush_time["rush_day"]
        
        # bring the beginning time for rush-hour
        beginning_hours, beginning_minutes = rush_time['begin']
        
        # shift the time by one minutes earlier and make it in ISO format
        time = functions_for_testing.set_iso_time(day_name, beginning_hours, beginning_minutes, time_shift=-1)
        result = functions.add_rush_hour_fee(time, delivery_fee)
        
        # the results must be the same delivery fee without adding rush-hour fee
        true_result = delivery_fee
        assert result == true_result

def test_add_rush_hour_fee_on_firs_minint_rush_hour_time():
    '''testing if the time is on first minint rush hour:
    friday 3:00'''
    
    delivery_fee = 100
    
    # Make the test for every day have a rush hour
    for rush_time in constants.rush_times :
        #day_name = constants.rush_times[rush_time]["rush_day"]
        day_name = rush_time["rush_day"]
        
        # bring the beginning time for rush-hour
        beginning_hours, beginning_minutes = rush_time['begin']
        
        # make the time in ISO format without shifting the time
        time = functions_for_testing.set_iso_time(day_name, beginning_hours, beginning_minutes, time_shift=0)
        
        result = functions.add_rush_hour_fee(time, delivery_fee)
        
        # the results must be the delivery fee multiplied bye rush-hour fee in integer
        true_result =  int(delivery_fee * rush_time['fee_multiplier'])
        assert result == true_result

def test_add_rush_hour_fee_in_rush_hour_time_rounding():
    '''testing if the time is on rush hour and the 
    delivery fee odd number so we make rounding to 
    avoid fractions of cents in it.
    
    for example if the delivery_fee is 99 cents and the rush hour fee multiplier is 1,2
    so the result is 118.8 cents
    but after rounding it become 119 cents'''
    
    delivery_fee = 99
    
    # Make the test for every day have a rush hour
    for rush_time in constants.rush_times :
        day_name = rush_time["rush_day"]
        
        # bring the beginning time for rush-hour
        beginning_hours, beginning_minutes = rush_time['begin']
        
        # make the time in ISO format without shifting the time
        time = functions_for_testing.set_iso_time(day_name, beginning_hours, beginning_minutes, time_shift=0)
        
        result = functions.add_rush_hour_fee(time, delivery_fee)
        
        # the results must be the delivery fee multiplied bye 
        # rush-hour fee rounded to the nearest integer number
        true_result = delivery_fee * rush_time['fee_multiplier']
        true_result = round(true_result)
        assert result == true_result
    
def test_add_rush_hour_fee_on_last_minint_rush_hour_time():
    '''testing if the time is on last minint rush hour:
    friday 6:59'''
    
    delivery_fee = 100
    
    # Make the test for every day have a rush hour
    for rush_time in constants.rush_times :
        day_name = rush_time["rush_day"]
        
        # bring the ending time for rush-hour
        end_hours, end_minutes = rush_time['end']
        
        # shift the time by one minutes earlier and make it in ISO format
        time = functions_for_testing.set_iso_time(day_name, end_hours, end_minutes, time_shift=-1)
        
        result = functions.add_rush_hour_fee(time, delivery_fee)
        
        # the results must be the delivery fee multiplied bye rush-hour fee in integer
        true_result = int(delivery_fee * rush_time['fee_multiplier'])
        assert result == true_result

def test_add_rush_hour_fee_on_firs_minint_after_rush_hour_time():
    '''testing if the time is on first minint after rush hour :
    friday 7:00'''
    
    delivery_fee = 100
    
    # Make the test for every day have a rush hour
    for rush_time in constants.rush_times :
        day_name = rush_time["rush_day"]
        
        # bring the ending time for rush-hour
        end_hours, end_minutes = rush_time['end']
        
        # make the time in ISO format without shifting the time
        time = functions_for_testing.set_iso_time(day_name, end_hours, end_minutes, time_shift=0)
        
        result = functions.add_rush_hour_fee(time, delivery_fee)
        
        # the results must be the same delivery fee without adding rush-hour fee
        true_result = delivery_fee
        assert result == true_result







