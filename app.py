#! /usr/bin/python

from chalice import Chalice
import datetime
import random, string

app = Chalice(app_name='webapp')

@app.route('/')
def random_world(length=10):
    current_time = datetime.datetime.now().time()
    current_time = str(current_time)
    content = "\nYou queried this at: %s UTC" %current_time

    length = 13
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'

    rnd = random.SystemRandom()
    password = "\nYour random password is:"+''.join(rnd.choice(chars) for i in range(length))

    footer = "\r\r\r\r\t\t\t\tDelivered via Lambda Function; triggered by API Gateway\n"
    
    return (password+content+footer)
