import queue


class Queue:
    def __init__(self):
        self._queue = queue.Queue()

    def pop(self):
        try:
            return self._queue.get(False)
        except queue.Empty:
            return None

    def push(self, item):
        return self._queue.put(item)


class Queue1(Queue):
    pass


class Queue2(Queue):
    pass


class Queue3(Queue):
    pass


_queue_1 = Queue1()
_queue_2 = Queue2()
_queue_3 = Queue3()

_queues = (_queue_1, _queue_2, _queue_3)


def get_queue(name):
    for queue in _queues:
        if queue.__class__.__name__ == name:
            desired_queue = queue
            break
    else:
        raise ValueError
    return desired_queue

