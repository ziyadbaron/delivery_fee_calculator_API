from main import app
import constants


""" 
# testing The delivery fee can never be more than 15€ :


## ( 1 ) when:
# cart_value 0.01€        (9.99€ fee)
# delivery distance 1500  (3€ fee)
# number of items is 4    (0€ fee)
# in rush-hour            (1.2x)
# the Total fee           (15.588)
-----------------------------------------------------

## ( 2 ) when:
# cart_value 10€           (0€ fee)
# delivery distance 8000   (16€ fee)
# number of items is 4     (0€ fee)
# not in rush-hour         (0€ fee)
# the Total fee            (16€) 
-----------------------------------------------------

## ( 3 ) when:
# cart_value 10€          (0€ fee)
# delivery distance 1000  (2€ fee)
# number of items is 28   (13.2€ fee)
#  not rush-hour 
# the Total fee           (15.2€)
"""



def test_maximum_fee_1():

    with app.test_client() as c:
        response = c.post('/', json={"cart_value": 1,
                                     "delivery_distance": 3500,
                                     "number_of_items": 4,
                                     "time": "2021-10-15T15:00:00Z"})

        # check the server response status code
        assert response.status_code == 200
        
        # check the result from the server
        server_result = response.get_json()
        true_result = constants.maximum_delivery_fee
        assert server_result == {"delivery_fee": true_result}


def test_maximum_fee_2():

    with app.test_client() as c:
        response = c.post('/', json={"cart_value": 1000,
                                     "delivery_distance": 8000,
                                     "number_of_items": 4,
                                     "time": "2021-10-13T15:00:00Z"})

        # check the server response status code
        assert response.status_code == 200
        
        # check the result from the server
        server_result = response.get_json()
        true_result = constants.maximum_delivery_fee
        assert server_result == {"delivery_fee": true_result}


def test_maximum_fee_3():

    with app.test_client() as c:
        response = c.post('/', json={"cart_value": 1000,
                                     "delivery_distance": 1000,
                                     "number_of_items": 28,
                                     "time": "2021-10-13T15:00:00Z"})

        # check the server response status code
        assert response.status_code == 200
        
        # check the result from the server
        server_result = response.get_json()
        true_result = constants.maximum_delivery_fee
        assert server_result == {"delivery_fee": true_result}
