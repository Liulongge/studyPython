


def make_pizza(size, *toppings): 
    """概述要制作的比萨""" 
    print("Making a " + str(size) + 
    "-inch pizza with the following toppings:") 
    for topping in toppings: 
        print("+ " + topping)