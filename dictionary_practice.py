dict_food = {"chicken": 1.59, "beef": 1.99, "cheese": 1.00, "milk": 2.00}

dict_food = {"chicken": "$1.59", "beef": "$1.99", "cheese": "$1.00", "milk": "$2.00"}
print(dict_food)

chicken_price = dict_food["chicken"]
print(chicken_price)

beef_price = dict_food["beef"]
print(beef_price)

cheese_price = dict_food["cheese"]
print(cheese_price)

milk_price = dict_food["milk"]
print(milk_price)

my_bucket_list = {"learn python": 1, "hang out": 2, "visit friends": 3, "watch movies": 4}
print(my_bucket_list)

number_learn_python = my_bucket_list["learn python"]
print(number_learn_python)

number_hangout = my_bucket_list["hang out"]
print(number_hangout)

number_visit_friends = my_bucket_list["visit friends"]
print(number_visit_friends)

number_watch_movies = my_bucket_list["watch movies"]
print(number_watch_movies)

update_value = my_bucket_list["learn python"] = 10
print(update_value)
print(my_bucket_list["learn python"] == 10)

my_bucket_list = {"learn python": 1, "hang out": 2, "visit friends": 3, "watch movies": 4}
my_bucket_list["learn python"] = 10
print(my_bucket_list)

number_of_shoes = {"Jordan": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
number_of_shoes["SB Dunk"] -= 2
number_of_shoes["Yeezy"] += 1

number_of_shoes["Jordan"] += 7
number_of_shoes["Yeezy"] += 7
number_of_shoes["Foamposite"] += 7
number_of_shoes["Air Max"] += 7
number_of_shoes["SB Dunk"] += 7
print(number_of_shoes)

number_of_shoes["NMD"] = 10
number_of_shoes["Superstar"] = 15
number_of_shoes["Ultraboost"] = 20
print(number_of_shoes)

del number_of_shoes["Ultraboost"]
print(number_of_shoes)

del number_of_shoes["Yeezy"]
number_of_shoes["SB Dunk"]
print(number_of_shoes)



