from sense_hat import sense_hat
from datetime import datetime


sense = SenseHat()


def get_sense_data():
    sense_data = []
    sense_data.append(sense.get_temperature())
    return sense_data

    while True:
        print(get_sense_data())
