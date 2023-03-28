from flask import Flask, request

import constants
import functions


'''
When the request body is valid, the endpoint returns:
status_code == 200  #(ok Request)
{"delivery_fee": The fee in cents} 
___________________________________________________________

If the request body is invalid, the endpoint returns:
status_code == 400  #(Bad Request)
{'error': proper error message}

the request body is invalid (Bad Request):
(1) if any of (cart value, delivery distance, number of items) is Zero, minus or not number.
(2) if any of (cart value, delivery distance, number of items, time ) does not exist in the request or 
    is assigned as None.
(3) if (time) is not in ISO format.
'''

# create a flask server
app = Flask(__name__)


@app.route(constants.api_url, methods=['POST'])
def delivery_fee_calculator():
    # fetch the request body (Json)
    request_json = request.get_json()
    # extract the variables from request body
    cart_value, delivery_distance, number_of_items, time = functions.extract_the_variables(
        request_json)

    # Validate the request body inputs and send proper error messages
    error, error_message = functions.validate_the_request_body(
        cart_value, delivery_distance, number_of_items, time)
    # in case of problems in request body, send error message
    if error:
        return {"error": error_message}, 400

    # Set initial delivery fee
    delivery_fee = 0

    # If the cart value does not qualify for free delivery, count the delivery fee
    if cart_value < constants.free_delivery_threshold:

        # apply surcharge of small cart value
        delivery_fee = functions.add_cart_value_fee(cart_value, delivery_fee)
        
        # apply all the fees if delivery fee didn't pass the maximum 
        # delivery fee threshold
        if delivery_fee < constants.maximum_delivery_fee:
            delivery_fee = functions.add_delivery_distance_fee(
                delivery_distance, delivery_fee)

        if delivery_fee < constants.maximum_delivery_fee:
            delivery_fee = functions.add_additional_items_fee(
                number_of_items, delivery_fee)

        if delivery_fee < constants.maximum_delivery_fee:
            delivery_fee = functions.add_rush_hour_fee(time, delivery_fee)

        # if delivery fee passed the maximum delivery fee threshold 
        # return the maximum delivery fee 
        if delivery_fee > constants.maximum_delivery_fee:
            return {"delivery_fee": constants.maximum_delivery_fee}

    return {"delivery_fee": delivery_fee}


# __name__ will be __main__ only if this file is the entry point
if __name__ == '__main__':
    # run the server on this ip and port 
    app.run(host=constants.host, port=constants.port, debug=True)
