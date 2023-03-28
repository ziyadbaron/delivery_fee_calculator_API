'''Constant parameters that will be easy to change 
in case the fees or policies in the company change'''


# the server IP
host = '0.0.0.0'

# the server port
port = 50100

# the base URL for the web page which has the API
base_url = ""

# set the path of the api in the main web page URL
api_path = '/'

# the URL for the API
api_url = base_url + api_path

# the minimum price for the order to not to add
# surcharge to the delivery price.
''' notice: if minimum_cart_value set to 0, it will deactivate 
    the cart_value_fee and its test'''
minimum_cart_value = 1000  # 10 € = 1000cent

# the minimum delivery distance and its fee
minimum_distance = 1000  # meters
minimum_distance_fee = 200  # 2€ = 200cent

# the periodic additional distance over the minimum delivery
# distance and its fee
additional_distance_period = 500  # meter
additional_period_fee = 100  # 1€ = 100cent

# the maximum amount of items in the cart to not to add
# surcharge to the delivery price.
additional_items_threshold = 4

# Additional fee for every additional item on the cart
additional_item_fee = 50  # 0.5€ = 50cent

# the maximum amount of items in the cart before applying
# extra fee (bulk_fee) for the delivery price
bulk_fee_threshold = 12  # amount of items
bulk_fee = 120  # 1.20€ = 120cent

# the minimum price for the order so the delivery is free
free_delivery_threshold = 10000  # 100€ = 10000cent

# the maximum delivery fee could apply for one order
maximum_delivery_fee = 1500  # 15€ = 1500cent

# Set rush hour parameters as a dictionary in a list so that
# in future more rush times can be added to the list easily
rush_times = [
    {
        "rush_day": "Friday",
        "begin": (15, 00),   # (hours, minutes)
        "end": (19, 00),   # (hours, minutes)
        "fee_multiplier": 1.2
    }
]
