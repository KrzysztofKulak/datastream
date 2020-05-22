import os
import atexit

from apscheduler.scheduler import Scheduler
from flask import Flask
import requests

from ..settings import queues
from ..settings import consumers
from ..settings import consumer_queues_map

app = Flask(__name__)
app.config["DATAQUEUE_URL"] = os.environ["DATAQUEUE_URL"]
app.config["DATAQUEUE_API_KEY"] = os.environ["INTAKE_API_KEY"]
app.config["POLLING_INTERVAL"] = int(os.environ["POLLING_INTERVAL"])

cron = Scheduler(daemon=True)
cron.start()


@cron.interval_schedule(seconds=app.config["POLLING_INTERVAL"])
def go_over_queues():
    for queue in queues:
        data = pop_queue(queue)
        if not data:
            continue
        for consumer in consumers:
            if queue in consumer_queues_map[consumer.name]:
                send_data(data, consumer.url)


def pop_queue(queue):
    response = requests.get(
        f"{app.config['DATAQUEUE_URL']}/outtake/{queue}",
        headers={"x-api-key": app.config["DATAQUEUE_API_KEY"]})
    if response.status_code == 200:
        return response.json()
    else:
        return False


def send_data(data, consumer_url):
    print(data)


atexit.register(lambda: cron.shutdown(wait=False))
