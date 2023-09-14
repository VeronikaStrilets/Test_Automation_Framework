import random
import uuid


def get_rand_value():
    value = str(uuid.uuid4()).replace("-", "")[:8]
    print(f"Generated UUID: {value}")
    return value


def get_rand_num():
    value = str(random.randint(1000000, 9999999))
    print(f"Generated number: {value}")
    return value


def get_rand_postcode():
    value = str(random.randint(10000, 99999))
    print(f"Generated postcode: {value}")
    return value
