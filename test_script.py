import random
import time

from dataproducer.dataproducer import enqueue_data

while True:
    time.sleep(5)
    data = {"topic": f"topic_{random.choice(['a', 'b', 'c'])}", "value": random.randint(1, 100)}
    print(enqueue_data(data))
