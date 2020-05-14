import os

from datamanager.settings import queues
from datamanager.settings import consumers
from datamanager.settings import consumer_queues_map


def main():
    for queue in queues:
        data = pop_queue(queue)
        for consumer in consumers:
            if queue in consumer_queues_map[consumer.name]:
                send_data(data, consumer.url)


def pop_queue(queue):
    return {"mock": "data"}


def send_data(data, consumer_url):
    print(data, consumer_url)


while True:
    pass
    # main()
