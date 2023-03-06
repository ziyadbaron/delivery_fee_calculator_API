from main import app
import constants


""" 
# testing if the User buy in rush-hour :


## ( 1 ) when:
# cart_value 9€          
# delivery distance 2000   
# number of items is 4 
# time friday at 2:59pm (not in rush-hour)
-----------------------------------------------------m

## ( 2 ) when:
# cart_value 9€          
# delivery distance 2000   
# number of items is 4  
# time friday at 3:00pm (in rush-hour)
-----------------------------------------------------m

## ( 3 ) when:
# cart_value 7€          
# delivery distance 1000   
# number of items is 10
# time friday at 5:20pm  (in rush-hour)
-----------------------------------------------------

## ( 4 ) when:
# cart_value 7€          
# delivery distance 1000   
# number of items is 10
# time friday at 6:59pm  (in rush-hour)
-----------------------------------------------------m

## ( 5 ) when:
# cart_value 7€          
# delivery distance 1000   
# number of items is 10 
# time friday at 7:00pm  (not in rush-hour)
-----------------------------------------------------m

## ( 6 ) when:
# cart_value 7€          
# delivery distance 1000   
# number of items is 10 
# time sunday at 3:00pm  (not in rush-hour)
-----------------------------------------------------

## ( 7 ) when:
# cart_value 8€          
# delivery distance 2000   
# number of items is 5 
# time monday at 3:30pm  (not in rush-hour)
-----------------------------------------------------

## ( 8 ) when:
# cart_value 6€          
# delivery distance 3500   
# number of items is 6 
# time wednesday at 5:17pm  (not in rush-hour)
-----------------------------------------------------

"""


def test_User_buying_in_rush_hour_1():

    with app.test_client() as c:
        response = c.post('/', json={"cart_value": 900,
                                     "delivery_distance": 2000,
                                     "number_of_items": 4,
                                     "time": "2021-10-15T14:59:00Z"})

        json_response = response.get_json()
        assert response.status_code == 200
        assert json_response == {"delivery_fee": 500}


def test_User_buying_in_rush_hour_2():

    with app.test_client() as c:
        response = c.post('/', json={"cart_value": 900,
                                     "delivery_distance": 2000,
                                     "number_of_items": 4,
                                     "time": "2021-10-15T15:00:00Z"})

        # check the server response status code
        assert response.status_code == 200
        
        # check the result from the server
        json_response = response.get_json()
        
        if constants.rush_times : 
            fee_multiplier = constants.rush_times[0]["fee_multiplier"]
        else:
            fee_multiplier = 1
        
        true_result = 500 * fee_multiplier
        assert json_response == {"delivery_fee": true_result}


def test_User_buying_in_rush_hour_3():

    with app.test_client() as c:
        response = c.post('/', json={"cart_value": 700,
                                     "delivery_distance": 1000,
                                     "number_of_items": 10,
                                     "time": "2021-10-15T17:20:00Z"})

        # check the server response status code
        assert response.status_code == 200
        
        # check the result from the server
        json_response = response.get_json()
        
        if constants.rush_times : 
            fee_multiplier = constants.rush_times[0]["fee_multiplier"]
        else:
            fee_multiplier = 1
        
        true_result = (500 + 300)* fee_multiplier
        
        assert json_response == {"delivery_fee": true_result}


def test_User_buying_in_rush_hour_4():

    with app.test_client() as c:
        response = c.post('/', json={"cart_value": 700,
                                     "delivery_distance": 1000,
                                     "number_of_items": 10,
                                     "time": "2021-10-15T18:59:00Z"})

        # check the server response status code
        assert response.status_code == 200
        
        # check the result from the server
        json_response = response.get_json()
        
        if constants.rush_times : 
            fee_multiplier = constants.rush_times[0]["fee_multiplier"]
        else:
            fee_multiplier = 1
        
        true_result = (300 + 200 + 300)* fee_multiplier
        
        assert json_response == {"delivery_fee": true_result}


def test_User_buying_in_rush_hour_5():

    with app.test_client() as c:
        response = c.post('/', json={"cart_value": 700,
                                     "delivery_distance": 1000,
                                     "number_of_items": 10,
                                     "time": "2021-10-15T19:00:00Z"})

        # check the server response status code
        assert response.status_code == 200
        
        # check the result from the server
        json_response = response.get_json()
        
        
        if constants.rush_times : 
            fee_multiplier = constants.rush_times[0]["fee_multiplier"]
        else:
            fee_multiplier = 1
        
        true_result = (300 + 200 + 300)
        assert json_response == {"delivery_fee": true_result}


def test_User_buying_in_rush_hour_6():

    with app.test_client() as c:
        response = c.post('/', json={"cart_value": 700,
                                     "delivery_distance": 1000,
                                     "number_of_items": 10,
                                     "time": "2021-10-17T15:00:00Z"})

        json_response = response.get_json()
        assert response.status_code == 200
        assert json_response == {"delivery_fee": 800}


def test_User_buying_in_rush_hour_7():

    with app.test_client() as c:
        response = c.post('/', json={"cart_value": 800,
                                     "delivery_distance": 2000,
                                     "number_of_items": 5,
                                     "time": "2021-10-18T15:30:00Z"})

        json_response = response.get_json()
        assert response.status_code == 200
        assert json_response == {"delivery_fee": 650}


def test_User_buying_in_rush_hour_8():

    with app.test_client() as c:
        response = c.post('/', json={"cart_value": 600,
                                     "delivery_distance": 3500,
                                     "number_of_items": 6,
                                     "time": "2021-10-20T17:17:00Z"})

        json_response = response.get_json()
        assert response.status_code == 200
        assert json_response == {"delivery_fee": 1200}
