import unittest
from unittest.mock import Mock, patch

from .queues import Queue, get_queue


class TestQueue(unittest.TestCase):

    @patch('dataqueue.queues.queue')
    def test_creation(self, mock_queue):
        queue = Queue()
        mock_queue.Queue.assert_called_once_with()

    def test_pop(self):
        queue = Queue()
        queue._queue = Mock()
        queue.pop()
        queue._queue.get.assert_called_once_with(False)

    def test_push(self):
        queue = Queue()
        queue._queue = Mock()
        queue.push("test item")
        queue._queue.put.assert_called_once_with("test item", False)

    @patch('dataqueue.queues._queues')
    def test_get_queue(self, mock_queues):
        class TestQueue1:
            pass

        class TestQueue2:
            pass

        mock_queues_list = [TestQueue1(), TestQueue2()]
        mock_queues.__getitem__.side_effect = mock_queues_list.__getitem__
        mock_queues.__iter__.side_effect = mock_queues_list.__iter__

        for name, exp_queue in [("TestQueue1", mock_queues_list[0]), ("TestQueue2", mock_queues_list[1])]:
            self.assertEquals(get_queue(name), exp_queue)

    @patch('dataqueue.queues._queues')
    def test_get_queue_error_handling(self, mock_queues):
        class TestQueue1:
            pass

        class TestQueue2:
            pass

        mock_queues_list = [TestQueue1(), TestQueue2()]
        mock_queues.__getitem__.side_effect = mock_queues_list.__getitem__
        mock_queues.__iter__.side_effect = mock_queues_list.__iter__

        with self.assertRaises(ValueError):
            get_queue("TestQueue3")
