from pandas import Timestamp
from pandas import Timedelta

import constants

''' The functions used for testing the API and its functions'''


def create_fake_date(day_name):
    '''function for creating fake dates for week days'''

    if day_name == 'Friday':
        return "2021-10-15T"
    if day_name == 'Saturday':
        return "2021-10-16T"
    if day_name == 'Sunday':
        return "2021-10-17T"
    if day_name == 'Monday':
        return "2021-10-18T"
    if day_name == 'Tuesday':
        return "2021-10-19T"
    if day_name == 'Wednesday':
        return "2021-10-20T"
    if day_name == 'Thursday':
        return "2021-10-21T"


def set_iso_time(day_name, hours, minutes, time_shift):
    '''function for making a date in ISO format'''

    # create fake date depending on day name
    date = create_fake_date(day_name)

    # Create a Pandas Timestamp object and shift the minutes
    date_object = Timestamp(f"{date}{str(hours)}:{str(minutes)}")
    time_shifted = date_object + Timedelta(minutes=time_shift)

    return time_shifted.isoformat()


def set_time_parameters(rush_hour):
    '''function to set the time parameters 
        in/out rush-hour time '''

    # take first day have rush hour
    day_name = constants.rush_times[0]["rush_day"]

    # if we are generating a date in rush hour
    if rush_hour:
        # take the beginning of the rush hour for the first day
        hours, minutes = constants.rush_times[0]["begin"]

        # do not make shift to the time
        time_shift = 0

    # if we are generating a date out of rush hour
    else:
        # take the ending of the rush hour for the first day
        hours, minutes = constants.rush_times[0]["end"]

        # shift the date 10 minutes after the
        # end of rush time (out of rush hour)
        time_shift = 10

    return day_name, hours, minutes, time_shift


def generate_iso_time(rush_hour):
    '''function for generating date in/out rush-hour time 
        and make it in ISO format'''

    # if the company has defined any rush_time during the week
    if constants.rush_times:
        # set the time parameters in/out rush-hour time
        day_name, hours, minutes, time_shift = set_time_parameters(rush_hour)

        # generating a date in ISO format
        rush_hour_date = set_iso_time(
            day_name, hours, minutes, time_shift=time_shift)
        return rush_hour_date

    # if the company has not defined any rush_time during the week
    else:
        # generating random date in ISO format
        random_date = set_iso_time(
            day_name="Friday", hours=10, minutes=10, time_shift=0)
        return random_date


def create_json_body(cart_value=constants.minimum_cart_value,
                     delivery_distance=constants.minimum_distance,
                     number_of_items=constants.additional_items_threshold,
                     time=False
                     ):
    ''' function to create json body for the request '''

    # ignore from json body the variable that has Boolean False value (but not number 0)
    if not cart_value and type(cart_value) != int:
        json_body = {
            "delivery_distance": delivery_distance,
            "number_of_items": number_of_items,
            "time": time}
        return json_body

    elif not delivery_distance and type(delivery_distance) != int:
        json_body = {"cart_value": cart_value,
                     "number_of_items": number_of_items,
                     "time": time}
        return json_body

    elif not number_of_items and type(number_of_items) != int:
        json_body = {"cart_value": cart_value,
                     "delivery_distance": delivery_distance,
                     "time": time}
        return json_body

    elif not time:
        json_body = {"cart_value": cart_value,
                     "delivery_distance": delivery_distance,
                     "number_of_items": number_of_items}
        return json_body

    # create json body without ignoring any variable
    json_body = {"cart_value": cart_value,
                 "delivery_distance": delivery_distance,
                 "number_of_items": number_of_items,
                 "time": time}
    return json_body


def post_request(requests,
                 cart_value=constants.minimum_cart_value,
                 special_cart_value=False,
                 delivery_distance=constants.minimum_distance,
                 number_of_items=constants.additional_items_threshold,
                 time=None,
                 rush_hour=False
                 ):
    '''function to create json request and post it to server. 
        it returns the server response'''

    # if we want to test special time format(not ISO format)
    if rush_hour == None:
        request_time = time

    else:
        # generates time in ISO format automatically in/out rush-hour time
        request_time = generate_iso_time(rush_hour)

    # avoid minimum cart value set to 0
    if constants.minimum_cart_value == 0 and not special_cart_value:
        cart_value = 1

    # create json body for the request
    json_body = create_json_body(cart_value=cart_value,
                                 delivery_distance=delivery_distance,
                                 number_of_items=number_of_items,
                                 time=request_time
                                 )

    # post to server and return the response
    server_response = requests.post(constants.api_url,
                                    json=json_body)

    return server_response
