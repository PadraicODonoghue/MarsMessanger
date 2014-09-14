from app import models
from time import sleep
from random import randrange

while True:
    sleep(randrange(0, 5))
    models.Message.generate_fake(1)
