from main import app

import constants
import functions_for_testing
#
""" 
# testing the rush-hour threshold :

# when:
# delivery distance 1000   (there is 2€ charge)
# number of items is 4     (there is no charge)
# not in rush-hour         (there is no charge)
"""


def test_rush_hours_minute_before_rush_hour():
    '''test if the order was sent 
        1 minute before rush-hour time

        in this example the result must be equal to
        minimum distance fee '''

    with app.test_client() as requests:
        # Make the test for every day have a rush hour
        for rush_time in constants.rush_times:
            day_name = rush_time["rush_day"]

            # bring the beginning time for rush-hour
            beginning_hours, beginning_minutes = rush_time['begin']

            # shift the time by one minute to earlier and make it in ISO format
            time = functions_for_testing.set_iso_time(day_name,
                                                      beginning_hours,
                                                      beginning_minutes,
                                                      time_shift=-1)

            # post request to the server
            server_response = functions_for_testing.post_request(requests,
                                                                 rush_hour=None,
                                                                 time=time,)

            # check the server response status code
            assert server_response.status_code == 200

            # check the result from the server
            server_result = server_response.get_json()
            true_result = constants.minimum_distance_fee
            assert server_result == {"delivery_fee": true_result}


def test_rush_hours_first_minute_rush_hour():
    '''test if the order was sent 
        on first minute of rush-hour time

        in this example the result must be equal to
        minimum distance fee * rush-hour fee multiplier'''

    with app.test_client() as requests:
        # Make the test for every day have a rush hour
        for rush_time in constants.rush_times:
            day_name = rush_time["rush_day"]

            # bring the beginning time for rush-hour
            beginning_hours, beginning_minutes = rush_time['begin']

            # make the time in ISO format without shifting the time
            time = functions_for_testing.set_iso_time(day_name,
                                                      beginning_hours,
                                                      beginning_minutes,
                                                      time_shift=0)

            # post request to the server
            server_response = functions_for_testing.post_request(requests,
                                                                 rush_hour=None,
                                                                 time=time,)

            # check the server response status code
            assert server_response.status_code == 200

            # check the result from the server
            server_result = server_response.get_json()
            true_result = constants.minimum_distance_fee * \
                rush_time["fee_multiplier"]
            assert server_result == {"delivery_fee": true_result}


def test_rush_hours_last_minute_rush_hour():
    '''test if the order was sent 
        on last minute rush-hour time

        in this example the result must be equal to
        minimum distance fee * rush-hour fee multiplier'''

    with app.test_client() as requests:
        # Make the test for every day that has a rush hour
        for rush_time in constants.rush_times:
            day_name = rush_time["rush_day"]

            # bring the ending time for rush-hour
            end_hours, end_minutes = rush_time['end']

            # shift the time by one minutes earlier and make it in ISO format
            time = functions_for_testing.set_iso_time(day_name,
                                                      end_hours,
                                                      end_minutes,
                                                      time_shift=-1)

            # post request to the server
            server_response = functions_for_testing.post_request(requests,
                                                                 rush_hour=None,
                                                                 time=time,)

            # check the server response status code
            assert server_response.status_code == 200

            # check the result from the server
            server_result = server_response.get_json()
            true_result = constants.minimum_distance_fee * \
                rush_time["fee_multiplier"]
            assert server_result == {"delivery_fee": true_result}


def test_rush_hours_minute_after_rush_hour():
    '''test if the order was sent 
        on first minute after rush-hour time

        in this example the result must be equal to
        minimum distance fee '''

    with app.test_client() as requests:
        # Make the test for every day that has a rush hour
        for rush_time in constants.rush_times:
            day_name = rush_time["rush_day"]

            # bring the ending time for rush-hour
            end_hours, end_minutes = rush_time['end']

            # make the time in ISO format without shifting the time
            time = functions_for_testing.set_iso_time(day_name,
                                                      end_hours,
                                                      end_minutes,
                                                      time_shift=0)

            # post request to the server
            server_response = functions_for_testing.post_request(requests,
                                                                 rush_hour=None,
                                                                 time=time)

            # check the server response status code
            assert server_response.status_code == 200

            # check the result from the server
            server_result = server_response.get_json()
            true_result = constants.minimum_distance_fee
            assert server_result == {"delivery_fee": true_result}
