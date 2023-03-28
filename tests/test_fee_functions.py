import constants
import functions
import functions_for_testing

#
'''test all the fees functions'''


# test cart value fee


def test_cart_value_fee_under_threshold():
    '''test if cart value is 
        1 cent less than 
        the minimum cart value limit.

        in this example the result must be equal to 1 '''

    # make this test if minimum cart value is more than 0 cents
    # if minimum cart value is 0 so disable the cart value fee since
    # there is no need to this test
    if constants.minimum_cart_value > 0:
        # Assign the delivery fee to 0 so we will get
        # just the result of the (add_cart_value_fee) function
        delivery_fee = 0

        cart_value = constants.minimum_cart_value - 1
        function_result = functions.add_cart_value_fee(
            cart_value, delivery_fee)
        true_result = 1
        assert function_result == true_result


def test_cart_value_fee_on_threshold():
    '''test if cart value is 
        exactly the minimum cart value limit.

        in this example the result must be equal to 0 '''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_cart_value_fee) function
    delivery_fee = 0

    cart_value = constants.minimum_cart_value
    function_result = functions.add_cart_value_fee(cart_value, delivery_fee)
    true_result = 0
    assert function_result == true_result


def test_cart_value_fee_over_threshold():
    '''test if cart value is 
        1 cent more than 
        the minimum cart value limit.

        in this example the result must be equal to 0 '''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_cart_value_fee) function
    delivery_fee = 0

    cart_value = constants.minimum_cart_value + 1
    function_result = functions.add_cart_value_fee(cart_value, delivery_fee)
    true_result = 0
    assert function_result == true_result


# test delivery distance fee


def test_delivery_distance_fee_without_extra_fee():
    '''test if the delivery distance is 
        1 metres under 
        the first fixed distance period.

        in this example the result must be equal to
        the minimum distance fee '''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_delivery_distance_fee) function
    delivery_fee = 0

    delivery_distance = constants.minimum_distance - 1
    function_result = functions.add_delivery_distance_fee(
        delivery_distance, delivery_fee)

    # the result must be the minimum delivery distance fee
    true_result = constants.minimum_distance_fee
    assert function_result == true_result


def test_delivery_distance_fee_extra_fee_threshold():
    '''test if the delivery distance is 
        exactly the first fixed distance period.

        in this example the result must be equal to
        the minimum distance fee '''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_delivery_distance_fee) function
    delivery_fee = 0

    delivery_distance = constants.minimum_distance
    function_result = functions.add_delivery_distance_fee(
        delivery_distance, delivery_fee)

    # the result must be the minimum delivery distance fee
    true_result = constants.minimum_distance_fee
    assert function_result == true_result


def test_delivery_distance_fee_with_extra_fee():
    '''test if the delivery distance is 
        1 meter over 
        the first fixed distance period .

        in this example the result must be equal to
        the minimum distance fee + 
        additional distance period fee'''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_delivery_distance_fee) function
    delivery_fee = 0

    delivery_distance = constants.minimum_distance + 1
    function_result = functions.add_delivery_distance_fee(
        delivery_distance, delivery_fee)

    # the result must be the minimum delivery distance fee plus one period additional fee
    true_result = constants.minimum_distance_fee + \
        constants.additional_period_fee
    assert function_result == true_result


def test_delivery_distance_fee_under_additional_period():
    '''test if the delivery distance is 
        1 metres under 
        the first fixed distance period + 
        the additional distance period.

        in this example the result must be equal to
        the minimum distance fee + 
        additional distance period fee'''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_delivery_distance_fee) function
    delivery_fee = 0

    delivery_distance = (constants.minimum_distance +
                         constants.additional_distance_period) - 1
    function_result = functions.add_delivery_distance_fee(
        delivery_distance, delivery_fee)

    # the result must be the minimum delivery distance fee plus one period additional fee
    true_result = constants.minimum_distance_fee + \
        constants.additional_period_fee
    assert function_result == true_result


def test_delivery_distance_fee_additional_period_threshold():
    '''test if the delivery distance is
        the first fixed distance period  + 
        the additional distance period.

        in this example the result must be equal to
        the minimum distance fee + 
        additional distance period fee'''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_delivery_distance_fee) function
    delivery_fee = 0

    delivery_distance = (constants.minimum_distance +
                         constants.additional_distance_period)
    function_result = functions.add_delivery_distance_fee(
        delivery_distance, delivery_fee)

    # the result must be the minimum delivery distance fee plus one period additional fee
    true_result = constants.minimum_distance_fee + \
        constants.additional_period_fee
    assert function_result == true_result


def test_delivery_distance_fee_over_additional_period():
    '''test if the delivery distance is 
        1 metres over 
        the first fixed distance period  + 
        the additional distance period.

        in this example the result must be equal to
        the minimum distance fee + 
        (2*additional distance period fee)'''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_delivery_distance_fee) function
    delivery_fee = 0

    delivery_distance = (constants.minimum_distance +
                         constants.additional_distance_period) + 1
    function_result = functions.add_delivery_distance_fee(
        delivery_distance, delivery_fee)

    # the result must be the minimum delivery distance fee plus two periods additional fee
    true_result = constants.minimum_distance_fee + \
        (2 * constants.additional_period_fee)
    assert function_result == true_result


# testing additional items fee


def test_additional_items_fee_one_item():
    '''test if the order has only 
        1 item.

        in this example the result must be 0'''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_additional_items_fee) function
    delivery_fee = 0

    number_of_items = 1
    function_result = functions.add_additional_items_fee(
        number_of_items, delivery_fee)
    true_result = 0
    assert function_result == true_result


def test_additional_items_fee_under_extra_fee():
    '''test if the order has 
        the maximum number of items without 
        extra surcharge.

        in this example the result must 0'''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_additional_items_fee) function
    delivery_fee = 0

    number_of_items = constants.additional_items_threshold
    function_result = functions.add_additional_items_fee(
        number_of_items, delivery_fee)
    true_result = 0
    assert function_result == true_result


def test_additional_items_fee_extra_item_fee():
    '''test if the order has
        one item more than
        the maximum number of items without 
        extra surcharge.

        in this example the result must be equal to
        additional item fee applied one time'''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_additional_items_fee) function
    delivery_fee = 0

    number_of_items = constants.additional_items_threshold + 1
    function_result = functions.add_additional_items_fee(
        number_of_items, delivery_fee)

    # the result must be additional item fee applied one time
    true_result = constants.additional_item_fee
    assert function_result == true_result


def test_additional_items_fee_under_bulk_fee_fee():
    '''test if the order has
        the maximum number of items without bulk_fee fee.


        in this example the result must be equal to
        the the additional items fee applied as 
        the number of the additional items '''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_additional_items_fee) function
    delivery_fee = 0

    number_of_items = constants.bulk_fee_threshold
    function_result = functions.add_additional_items_fee(
        number_of_items, delivery_fee)

    # the result must be the fee applied as the number of the additional items
    additional_item_number = number_of_items - \
        constants.additional_items_threshold
    true_result = (constants.additional_item_fee *
                   additional_item_number)
    assert function_result == true_result


def test_additional_items_fee_bulk_fee_fee():
    '''test if the order has
        one item more than
        the maximum number of items without bulk_fee fee.

        in this example the result must be equal to
        the the additional items fee applied as 
        the number of the additional items  + 
        the bulk_fee fee'''

    # Assign the delivery fee to 0 so we will get
    # just the result of the (add_additional_items_fee) function
    delivery_fee = 0

    number_of_items = constants.bulk_fee_threshold + 1
    function_result = functions.add_additional_items_fee(
        number_of_items, delivery_fee)

    # the result must be the fee applied as the number of the additional items plus the bulk_fee fee
    additional_item_number = number_of_items - \
        constants.additional_items_threshold
    true_result = (constants.additional_item_fee *
                   additional_item_number) + constants.bulk_fee
    assert function_result == true_result


# testing rush hour fee

def test_rush_hour_fee_minute_before_rush_hour():
    '''test if the order is sent  
        1 minute before rush-hour time

        in this example the result must be equal to
        delivery fee '''

    # Assign the delivery fee to 100 so we will
    # check if rush-hour fee multiplier is applied
    delivery_fee = 100

    # Make the test for every day have a rush hour
    for rush_time in constants.rush_times:
        day_name = rush_time["rush_day"]

        # bring the beginning time for rush-hour
        beginning_hours, beginning_minutes = rush_time['begin']

        # shift the time by one minutes earlier and make it in ISO format
        time = functions_for_testing.set_iso_time(
            day_name, beginning_hours, beginning_minutes, time_shift=-1)
        function_result = functions.add_rush_hour_fee(time, delivery_fee)

        # the results must be the same delivery fee without adding rush-hour fee
        true_result = delivery_fee
        assert function_result == true_result


def test_rush_hour_fee_first_minute_rush_hour():
    '''test if the order is sent
        on first minute of rush-hour time

        in this example the result must be equal to
        delivery fee * rush-hour fee multiplier'''

    # Assign the delivery fee to 100 so we will
    # check if rush-hour fee multiplier is applied
    delivery_fee = 100

    # Make the test for every day have a rush hour
    for rush_time in constants.rush_times:
        day_name = rush_time["rush_day"]

        # bring the beginning time for rush-hour
        beginning_hours, beginning_minutes = rush_time['begin']

        # make the time in ISO format without shifting the time
        time = functions_for_testing.set_iso_time(
            day_name, beginning_hours, beginning_minutes, time_shift=0)

        function_result = functions.add_rush_hour_fee(time, delivery_fee)

        # the results must be the delivery fee multiplied bye rush-hour fee in integer
        true_result = int(delivery_fee * rush_time['fee_multiplier'])
        assert function_result == true_result


def test_rush_hour_fee_rounding():
    '''test if the time is on rush hour and 
        the delivery fee is an odd number 
        in order to make rounding to avoid fractions 
        of cents in the fee.

        for example if the delivery fee is 99 cents and
        the rush hour fee multiplier is 1,2
        the result is 118.8 cents
        but after rounding it becomes 119 cents'''

    # Assign the delivery fee to 99 so we will check
    # if the function apply rounding to the result of this function
    delivery_fee = 99

    # Make the test for every day have a rush hour
    for rush_time in constants.rush_times:
        day_name = rush_time["rush_day"]

        # bring the beginning time for rush-hour
        beginning_hours, beginning_minutes = rush_time['begin']

        # make the time in ISO format without shifting the time
        time = functions_for_testing.set_iso_time(
            day_name, beginning_hours, beginning_minutes, time_shift=0)

        function_result = functions.add_rush_hour_fee(time, delivery_fee)

        # the results must be the delivery fee multiplied bye
        # rush-hour fee rounded to the nearest integer number
        true_result = delivery_fee * rush_time['fee_multiplier']
        true_result = round(true_result)
        assert function_result == true_result


def test_rush_hour_fee_last_minute_rush_hour():
    '''test if the order is sent 
        on last minute of rush-hour time

        in this example the result must be equal to
        delivery fee * rush-hour fee multiplier'''

    # Assign the delivery fee to 100 so we will
    # check if rush-hour fee multiplier is applied
    delivery_fee = 100

    # Make the test for every day have a rush hour
    for rush_time in constants.rush_times:
        day_name = rush_time["rush_day"]

        # bring the ending time for rush-hour
        end_hours, end_minutes = rush_time['end']

        # shift the time by one minutes earlier and make it in ISO format
        time = functions_for_testing.set_iso_time(
            day_name, end_hours, end_minutes, time_shift=-1)

        function_result = functions.add_rush_hour_fee(time, delivery_fee)

        # the results must be the delivery fee multiplied bye rush-hour fee in integer
        true_result = int(delivery_fee * rush_time['fee_multiplier'])
        assert function_result == true_result


def test_rush_hour_fee_minute_after_rush_hour():
    '''test if the order is sent 
        on first minute after rush-hour time

        in this example the result must be equal to
        delivery fee'''

    # Assign the delivery fee to 100 so we will
    # check if rush-hour fee multiplier is applied
    delivery_fee = 100

    # Make the test for every day have a rush hour
    for rush_time in constants.rush_times:
        day_name = rush_time["rush_day"]

        # bring the ending time for rush-hour
        end_hours, end_minutes = rush_time['end']

        # make the time in ISO format without shifting the time
        time = functions_for_testing.set_iso_time(
            day_name, end_hours, end_minutes, time_shift=0)

        function_result = functions.add_rush_hour_fee(time, delivery_fee)

        # the results must be the same delivery fee without adding rush-hour fee
        true_result = delivery_fee
        assert function_result == true_result
