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
        return self._queue.put(item, False)


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


def _get_class_name(queue):
    return queue.__class__.__name__


def get_queue(name):
    if name in map(lambda n: _get_class_name(n), _queues):
        return [queue for queue in _queues if _get_class_name(queue) == name][0]
    raise ValueError

