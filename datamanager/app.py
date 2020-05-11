import os

from flask import Flask, request

from .settings import queues
from .settings import consumers
from .settings import consumer_queues_map

app = Flask(__name__)
app.config["INTAKE_API_KEY"] = os.environ["INTAKE_API_KEY"]


@app.route("/")
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
    main()
