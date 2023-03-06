'''Constant parameters that will be easy to change 
in case the fees or policies in the company change'''

# the minimum price for the order to not to add
# surcharge to the delivery price.
minimum_cart_value = 1000  # 10 € = 100cent

# the minimum delivery distance and its fee
minimum_distance = 1000  # M
minimum_distance_fee = 200  # 2€ = 200cent

# the periodic additional distance over the minimum delivery
# distance and it's fee
additional_distance_period = 500  # M
additional_distance_period_fee = 100  # 1€ = 100cent

# the maximum amount of items in the cart to not to add
# surcharge to the delivery price.
maximum_number_of_items_without_fee = 4
maximum_items_free_charge = 4
items_free_charge_threshold = 4
items_free_charge_limit = 4




# Additional fee for every additional item on the cart
additional_item_fee = 50  # 0.5€ = 50cent

# the maximum amount of items in the cart before apply
# extra fee (bulk) for the delivery price
maximum_items_number = 12
bulk_threshold = 12
bulk_fee_threshold = 12
bulk_item_threshold = 12
bulk = 120  # 1.20€ = 120cent






# the minimum price for the order so the delivery is free
free_delivery_threshold = 10000  # 100€ = 10000cent

# the maximum delivery fee could apply for one order
maximum_delivery_fee = 1500  # 15€ = 1500cent

# Set rush hour parameters as a dictionary in a list so that
# in future more rush times can be added to the list easily
rush_times =[
    {
        "rush_day"      :"Friday",
        "begin"         :(15, 00),
        "end"           :(19, 00),
        "fee_multiplier": 1.2
    }
]

#rush_times =[]

# set the path for the rout of the api
PATH = '/'