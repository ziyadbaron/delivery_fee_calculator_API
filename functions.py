from math import ceil
from pandas import Timestamp
from datetime import datetime, time

import constants

''' The functions used in the endpoint '''

# Function that returns the values extracted from the request body.


def extract_the_variables(request_json):

    # if any of the variables missing from the request body assign it to None
    try:
        cart_value = request_json['cart_value']
    except:
        cart_value = None
    try:
        delivery_distance = request_json['delivery_distance']
    except:
        delivery_distance = None
    try:
        number_of_items = request_json['number_of_items']
    except:
        number_of_items = None
    try:
        time = request_json['time']
    except:
        time = None

    return cart_value, delivery_distance, number_of_items, time


# Function to check that the cart value is exist (not None) in the
# request body and it's positive integer number.
# returns boolean as error variable and proper error message.
def cart_value_validation(cart_value):

    # Check if the cart value have None value
    if cart_value == None:
        error_message = "cart value is missing from the request or it's assigned to None value."
        return True, error_message

    # Check if the cart value is not integer number
    if type(cart_value) != int:
        error_message = "cart value should be an integer number."
        return True, error_message

    # Check if the cart value is not negative or zero value
    if cart_value < 1:
        error_message = "cart value should not be 0 cent or less."
        return True, error_message

    return False, ""

# Function to check that the delivery distance is exist (not None) in the
# request body and it's positive integer number.
# returns boolean as error variable and proper error message.


def delivery_distance_validation(delivery_distance):

    # Check if the delivery distance have None value
    if delivery_distance == None:
        error_message = "delivery distance is missing from the request or it's assigned to None value."
        return True, error_message

    # Check if the delivery distance is not integer number
    if type(delivery_distance) != int:
        error_message = "delivery_distance should be an integer number."
        return True, error_message

    # Check if the delivery distance is not negative or zero value
    if delivery_distance < 1:
        error_message = "delivery distance should not be shorter than 1 meter."
        return True, error_message

    return False, ""

# Function to check that the number of items is exist (not None) in the
# request body and it's positive integer number.
# returns boolean as error variable and proper error message.


def number_of_items_validation(number_of_items):

    # Check if the number of items have None value
    if number_of_items == None:
        error_message = "number of items is missing from the request or it's assigned to None value."
        return True, error_message

    # Check if the number of items is not integer number
    if type(number_of_items) != int:
        error_message = "number of items should be an integer number."
        return True, error_message

    # Check if the number of items not negative or zero value
    if number_of_items < 1:
        error_message = "number of items should not be less than 1 item."
        return True, error_message

    return False, ""

# Function to check that the time is exist (not None) in the
# request body and it's in ISO format.
# returns boolean as error variable and proper error message.


def time_validation(time):

    # Check if the time variable is None values
    if time == None:
        error_message = "date is missing from the request or it's assigned to None value."
        return True, error_message

    # Check that date is in ISO format
    try:
        datetime.fromisoformat(time.replace('Z', '+00:00'))
    except:
        error_message = "time should be in ISO format."
        return True, error_message

    return False, ""

# Function to check that the values of request body are valid.
# returns boolean as error variable and proper error message.


def validate_the_request_body(cart_value, delivery_distance, number_of_items, time):
    # check that the cart value is exist (not None) in the request body and it's positive integer number
    cart_value_error, error_message = cart_value_validation(
        cart_value)
    if cart_value_error:
        return True, error_message

    # check that the delivery distance is exist (not None) in the request body and it's positive integer number
    delivery_distance_value_error, error_message = delivery_distance_validation(
        delivery_distance)
    if delivery_distance_value_error:
        return True, error_message

    # check that the number of items is exist (not None) in the request body and it's positive integer number
    number_of_items_value_error, error_message = number_of_items_validation(
        number_of_items)
    if number_of_items_value_error:
        return True, error_message

    # check that the time is exist (not None) in the request body and it's in ISO format
    time_value_error, error_message = time_validation(time)
    if time_value_error:
        return True, error_message

    return False, ""




# Function that return delivery fee with surcharge for
# small cart value, if cart value < cart value limit (10€).
def add_cart_value_fee(cart_value, delivery_fee):
    # If the cart value is less than the minimum cart value (10€), a small order
    # surcharge is added to the delivery fee.
    if cart_value < constants.minimum_cart_value:
        delivery_fee += constants.minimum_cart_value - cart_value
    return delivery_fee


# Function that returns the amount of delivery fee when the customer's
# delivery distance is more than the minimum delivery distance.
def additional_distance_fee(delivery_distance):
    # Get the amount of additional distance periods (every 500 meters is one period)
    additional_distance = delivery_distance - constants.minimum_distance
    periods = additional_distance / constants.additional_distance_period

    # Even if the distance would be shorter than 500 meters,
    # the minimum fee is always 1€
    # Round up the periods
    periods = ceil(periods)

    # Calculate the additional distance fee
    distance_fee = periods * constants.additional_distance_period_fee
    return distance_fee

# Function that returns the delivery fee with the distance based fee.
# it add 1€ for every additional 500 meters if the delivery distance is
# longer than 1000 meters.


def add_delivery_distance_fee(delivery_distance, delivery_fee):

    # If the delivery distance is longer than 1000 meters,
    # 1€ is added for every additional 500 meters
    if delivery_distance > constants.minimum_distance:
        delivery_fee += additional_distance_fee(
            delivery_distance)

    # add the delivery distance for first 1000 meters
    # (=1km), delivery fee for the distance is 2€.
    delivery_fee += constants.minimum_distance_fee
    return delivery_fee


# Function that returns the surcharge of orders with multiple items (5 or more)
def additional_items_fee(number_of_items):
    # Add fee for every item above the maximum number of free items
    num_of_additional_items = number_of_items - \
        constants.maximum_number_of_items_without_fee
    additional_items_fee = num_of_additional_items * constants.additional_item_fee

    # An extra "bulk" fee applies for more than 12 items of 1,20€
    if number_of_items > constants.maximum_items_number:
        # Add bulk fee only once
        additional_items_fee += constants.bulk
    return additional_items_fee

# Function that returns the delivery fee with the fee of additional
# items, if there is additional items.


def add_additional_items_fee(number_of_items, delivery_fee):

    # an additional (50 cent) surcharge is added for each item above five
    if number_of_items > constants.maximum_number_of_items_without_fee:
        delivery_fee += additional_items_fee(
            number_of_items)
    return delivery_fee


# Function that returns the delivery fee multiplier
# if the order was sent during rush hour.
def check_rush_hour_time(customer_time):
    # split customer time string to date and time
    # "2021-10-12", "13:00:00Z" = "2021-10-12T13:00:00Z"
    order_date, order_time = customer_time.split('T')

    # split the order time string to hours and minutes
    # "13",  "00"  ,    = "13:00:00Z"
    hours, minutes, _ = order_time.split(':')

    # Create a Pandas Timestamp object to get the weekday
    date_object = Timestamp(order_date)

    # if there is rush time 
    if constants.rush_times :
        # go through the rush times and check if the order was sent in rush hour
        for rush_time in constants.rush_times:
            # if customer order day is in rush day
            #if date_object.day_name() == constants.rush_times[rush_time]["rush_day"]:
            if date_object.day_name() == rush_time["rush_day"]:

                # get the order time
                order_time = time(int(hours), int(minutes))

                # get the rush hour beginning and end times
                #beginning_hours, beginning_minutes = constants.rush_times[rush_time]['begin']
                beginning_hours, beginning_minutes = rush_time['begin']
                rush_hour_begin = time(beginning_hours, beginning_minutes)

                #end_hours, end_minutes = constants.rush_times[rush_time]['end']
                end_hours, end_minutes = rush_time['end']
                rush_hour_end = time(end_hours, end_minutes)

                # if customer order time is in rush hour time, return the rush hour fee multiplier
                if rush_hour_begin <= order_time < rush_hour_end:
                    #return True, constants.rush_times[rush_time]['fee_multiplier']
                    return True, rush_time['fee_multiplier']

    return False, 1

# Function that returns delivery fee with
# rush hour multiplication, if it's rush hour.


def add_rush_hour_fee(time, delivery_fee):

    # if it's rush-hour time, apply rush-hour fee
    rush_hour, rush_hour_fee_multiplier = check_rush_hour_time(
        time)
    if rush_hour:
        delivery_fee *= rush_hour_fee_multiplier
        # The multiplier is 1.2 so let's round the fee so that
        # there is no fractions of cents in it
        delivery_fee = round(delivery_fee)
    return delivery_fee
