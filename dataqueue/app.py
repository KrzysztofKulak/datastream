import datetime
from json import dumps

from flask import Flask, jsonify, request

from .queues import get_queue

app = Flask(__name__)

queue_topics_map = {
    "Queue1": ["topic_a", "topic_b"],
    "Queue2": ["topic_c", "topic_d"],
    "Queue3": ["topic_c"]
}


@app.route('/intake', methods=["POST"])
def intake():
    input_json = request.json
    input_json["TIMESTAMP"] = datetime.datetime.now()
    queues = assign_queues(input_json["topic"])
    for queue in queues:
        queue.push(input_json)
    return input_json, 200


@app.route('/outtake/<string:queue>', methods=["GET"])
def outtake(queue):
    try:
        response = get_queue(queue).pop()
    except ValueError:
        return f"Queue {queue} not found", 404
    if response:
        return response
    else:
        return f"Queue {queue} empty", 404


def assign_queues(topic):
    queues = []
    for queue, topics in queue_topics_map.items():
        if topic in topics:
            queues.append(get_queue(queue))
    return queues
