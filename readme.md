To run this code, you have to make sure that you have installed in your computer python3 and its libraries pandas, flask and pytest for testing the code. 

run pip install -r requirements.txt

To run the code, go to the folder in your terminal and run python3 main.py or just python main.py if you're using Windows.


To call the API open new terminal and run:

curl -X POST http://192.168.3.48:50100 -d '{"cart_value": 1000,"delivery_distance": 1500,"number_of_items": 4,"time": "2021-10-15T15:00:00Z"}' -H 'Content-Type: application/json'

You will get the delivery fee as:

{
  "delivery_fee": 360
}

You can change (cart_value, delivery_distance, number_of_items, time) to get the delivery fee.


To run the test navigate in terminal to the code folder and run:

 python3 -m pytest


The tests of the code include 53 different kind of tests to check all the functionality of the code and the validness of the request body with its proper error message.





To install pytest, run: pip3 install pytest
To run the test: python3 -m pytest

to install the requirements tool : pip install pipreqs
                                   pip install -r requirements.txt
to made the requirements file:    pipreqs .
to overwrite the requirements file:    pipreqs --force 