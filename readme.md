This code is a solution of a wolt task for summer internship 2023.

It is a HTTP API (single endpoint) to calculate a delivery fee. See more: https://github.com/woltapp/engineering-summer-intern-2023.

The tests of the code include more than 100 different kind of tests to check all the functionality of the code and the validness of the request body with its proper error messages.

The code is designed to

1. be easy to upgrade on future
2. be easy to read and understand
3. have tests covering almost all the functionalities and their possible variation

In order to make the code more future proof, it 

1. won't broke even if some constant values might be deactivated, like cart value fee or rush hour 
2. doesn't return fractions of cents as a result

To run this code, you have to make sure that you have installed in your computer python3 and its libraries pandas, flask and pytest for testing the code.

run pip install -r requirements.txt

To run the code, go to the folder in your terminal and run python3 main.py or just python main.py if you're using Windows. (This command will tell you which http address to use in the next command.)

To call the API, open new terminal and run:

curl -X POST http://127.0.0.1:50100 -d '{"cart_value": 1000,"delivery_distance": 1500,"number_of_items": 4,"time": "2021-10-15T15:00:00Z"}' -H 'Content-Type: application/json'

You will get the delivery fee in cents as:

{
"delivery_fee": 360
}

(If it didn't, check the http address from the previous call in previous terminal.)

You can change the parameters (cart_value, delivery_distance, number_of_items, time) to get the delivery fee.

To run the test (navigate in terminal to the code folder and) run:

python3 -m pytest
