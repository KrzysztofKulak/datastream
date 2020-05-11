import datetime
import os

from flask import Flask, request

from .queues import get_queue
from .settings import queue_topics_map

app = Flask(__name__)
app.config["INTAKE_API_KEY"] = os.environ["INTAKE_API_KEY"]
app.config["OUTTAKE_API_KEY"] = os.environ["OUTTAKE_API_KEY"]


@app.route('/intake', methods=["POST"])
def intake():
    if request.headers.get("x-api-key") != app.config["INTAKE_API_KEY"]:
        return "api key incorrect", 401
    input_json = request.json
    input_json["TIMESTAMP"] = datetime.datetime.now()
    queues = assign_queues(input_json["topic"])
    for queue in queues:
        queue.push(input_json)
    return input_json, 200


@app.route('/outtake/<string:queue>', methods=["GET"])
def outtake(queue):
    if request.headers.get("x-api-key") != app.config["OUTTAKE_API_KEY"]:
        return "api key incorrect", 401
    try:
        response = get_queue(queue).pop()
    except ValueError:
        return f"queue {queue} not found", 404
    if response:
        return response
    else:
        return f"queue {queue} empty", 404


def assign_queues(topic):
    queues = []
    for queue, topics in queue_topics_map.items():
        if topic in topics:
            queues.append(get_queue(queue))
    return queues
