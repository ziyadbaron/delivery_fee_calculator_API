from datetime import time
from pandas import Timestamp
from pandas import Timedelta

import constants



def create_fake_date(day_name):
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
    # create fake date depending on day name
    date = create_fake_date(day_name)
    
    # Create a Pandas Timestamp object and shift the minutes
    leap = Timestamp(f"{date}{str(hours)}:{str(minutes)}")
    time_shifted = leap + Timedelta(minutes=time_shift)
    
    return time_shifted.isoformat()


def generate_iso_time(rush_hour):
    # if there is rush time 
    if constants.rush_times :
        # if we are generating a date in the rush hour time
        if rush_hour:
            # take first day have rush hour and it's beginning rush time 
            day_name = constants.rush_times[0]["rush_day"]
            begin_hours, begin_minutes = constants.rush_times[0]["begin"]
            
            # generating a date in ISO format
            rush_hour_date = set_iso_time(day_name, begin_hours, begin_minutes, time_shift=0)
            return rush_hour_date

        # if we are generating a date not in the rush hour time
        else:
            # take first day have rush hour and it's ending rush time 
            day_name = constants.rush_times[0]["rush_day"]
            end_hours, end_minutes = constants.rush_times[0]["end"]
            
            # generating a date in ISO format 10 minutes after 
            # the end of rush time 
            not_rush_hour_date = set_iso_time(day_name, end_hours, end_minutes, time_shift=10)
            return not_rush_hour_date
    else:
        # generating random date in ISO format
        random_date = set_iso_time(day_name="Friday", hours=10, minutes=10, time_shift=0)
        return random_date



def create_json_request(cart_value=constants.minimum_cart_value,
                delivery_distance=constants.minimum_distance,
                number_of_items=constants.maximum_number_of_items_without_fee,
                time=False
                ):
    # deleted from json body the variable have Boolean False value  and type(var) == int
    if not cart_value and type(cart_value) != int:
        request_json = {
                "delivery_distance": delivery_distance,
                "number_of_items": number_of_items,
                "time": time}
        return request_json

    elif not delivery_distance and type(delivery_distance) != int:
        request_json = {"cart_value": cart_value,
                        "number_of_items": number_of_items,
                        "time": time}
        return request_json

    elif not number_of_items and type(number_of_items) != int:
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




def client_post(client,
                cart_value=constants.minimum_cart_value,
                delivery_distance=constants.minimum_distance,
                number_of_items=constants.maximum_number_of_items_without_fee,
                time_missing=False,
                special_time_format=False,
                client_time=None,
                rush_hour=False
                ):

    # if we want to test the request body missing the time variable
    if time_missing:
        time = False
    # if we want to test special time format(not ISO format)
    elif special_time_format:
        time = client_time
    else:
        # generates time in ISO format automatically in or out rush-hour time
        # depending on rush-hour time constants
        time = generate_iso_time(rush_hour)

    # 
    json_request = create_json_request(cart_value=cart_value,
                            delivery_distance=delivery_distance,
                            number_of_items=number_of_items,
                            time=time
                            )

    # send post to server and return the response
    server_response = client.post(constants.PATH,
                                json=json_request)

    return server_response









# WEEK_DAYS = ['Sunday', 'Monday', 'Tuesday',
#              'Wednesday', 'Thursday', 'Friday', 'Saturday']

    
    
# def date_generator_in_iso_format1(rush_hour):

#     # if we are generating a date in the rush hour time
#     if rush_hour:

#         day_name = constants.rush_times[0]["rush_day"]
#         date = create_fake_date(day_name)
#         begin_hours, begin_minutes = constants.rush_times[0]["begin"]
        
#         order_time = time(int(begin_hours), int(begin_minutes))
#         return date + str(order_time)  #+ ":00Z"
#         #return date + str(begin_hours) + ":" + str(begin_minutes) + ":00Z"

#     # if we are generating a date not in the rush hour time
#     else:
#         for day in WEEK_DAYS:

#             exist = []

#             exist = list(filter(
#                 lambda rush_time: rush_time['rush_day'] == day,
#                 constants.rush_times))

#             # if this day is not rush day(have not rush hour) so generate 
#             # an iso format date in this day with random hours and minutes
#             if not exist:
#                 date = create_fake_date(day)
#                 return date + "10:00:00Z"
            
#             # if this day is rush day So try to generate an iso format date 
#             # And choose the time after a few minutes from the rush hour ending
#             else:
#                 date = create_fake_date(day)

#                 #beginning_hours, beginning_minutes = exist[0]["begin"]
#                 #rush_hour_begin = time(beginning_hours, beginning_minutes)

#                 end_hours, end_minutes = exist[0]["end"]
#                 #rush_hour_end = time(end_hours, end_minutes)

#                 after_end_minutes = end_minutes + 10
#                 #order_time = time(int(end_hours), int(after_end_minutes))

#                 #if rush_hour_begin <= order_time < rush_hour_end:
#                 #    continue
#                 #else:
#                 order_time = time(int(end_hours), int(after_end_minutes))
#                 return date + str(order_time) + ":00Z"
#                 #return date + str(end_hours) + ":" + str(after_end_minutes) + ":00Z"


# def date_generator_in_iso_format(rush_hour):

#     # if we are generating a date in the rush hour time
#     if rush_hour:
#         # find the first rush time in rush day dictionary
#         #
#         # for rush_time in constants.rush_times:
#         #     day_name = rush_time["rush_day"]
#         #     date = create_fake_date(day_name)
#         #     begin_hours, begin_minutes = rush_time["begin"]
#         #     return date + str(begin_hours) + ":"+ str(begin_minutes) + ":00Z"

#         day_name = constants.rush_times[0]["rush_day"]
#         date = create_fake_date(day_name)
#         begin_hours, begin_minutes = constants.rush_times[0]["begin"]
#         return date + str(begin_hours) + ":" + str(begin_minutes) + ":00Z"

#     # if we are generating a date not in the rush hour time
#     else:
#         for week_day in WEEK_DAYS:
#             #exist = None
#             exist = []

#             # rush_day_key = -1
#             # for rush_time in constants.rush_times:
#             #     rush_day_key += 1
#             #     if week_day == rush_time["rush_day"] :
#             #         exist = True

#             #         break

#             # if week_day in constants.rush_times.values():
#             exist = list(filter(
#                 lambda rush_time: rush_time['rush_day'] == week_day, constants.rush_times))

#             if not exist:
#             #if exist == None:
#             #if len(exist) == 0:

#                 date = create_fake_date(week_day)
#                 return date + str(10) + ":" + str(00) + ":00Z"
#             else:
#                 date = create_fake_date(week_day)
#                 #beginning_hours, beginning_minutes = constants.rush_times[rush_day_key]["begin"]
#                 beginning_hours, beginning_minutes = exist[0]["begin"]
#                 rush_hour_begin = time(beginning_hours, beginning_minutes)

#                 #end_hours, end_minutes = constants.rush_times[rush_day_key]["end"]
#                 end_hours, end_minutes = exist[0]["end"]
#                 rush_hour_end = time(end_hours, end_minutes)

#                 after_end_minutes = end_minutes + 10
#                 order_time = time(int(end_hours), int(after_end_minutes))

#                 if rush_hour_begin <= order_time < rush_hour_end:
#                     continue
#                 else:
#                     return date + str(end_hours) + ":" + str(after_end_minutes) + ":00Z"
