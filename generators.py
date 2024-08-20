import random

from data import Orders


def generate_name():
    return random.choice(Orders.NAME)

def generate_surname():
    return random.choice(Orders.SURNAME)

def generate_address():
    return random.choice(Orders.ADDRESS)

def generate_station():
    return random.choice(Orders.STATION)

def generate_telephone():
    number = random.randint(1000000000, 9999999999)
    return f'7{number}'

def generate_rental_period():
    return random.choice(Orders.RENTAL_PERIOD)

def generate_color():
    return random.choice(Orders.COLOR)

def generate_comment():
    return random.choice(Orders.COMMENT)
