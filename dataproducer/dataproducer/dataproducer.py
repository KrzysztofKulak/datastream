import os
import requests

dataqueue_url = os.environ["DATAQUEUE_URL"]
api_key = os.environ["API_KEY"]


def enqueue_data(data):
    return requests.post(
        f"{dataqueue_url}/intake", json=data, headers={"x-api_key": api_key}
    ).json()
