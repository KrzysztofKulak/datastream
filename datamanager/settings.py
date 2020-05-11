from collections import namedtuple

Consumer = namedtuple('Consumer', 'name url')

queues = ["Queue1", "Queue2", "Queue3"]
consumers = [Consumer("Consumer1", ""), Consumer("Consumer2", "")]
consumer_queues_map = {
    "Consumer1": ["Queue1", "Queue2"],
    "Consumer2": ["Queue3"]
}
