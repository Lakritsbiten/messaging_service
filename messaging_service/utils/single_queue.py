from messaging_service.utils.singleton import Singleton
import queue


class WorkQueue(metaclass=Singleton):
    # Implemented as a singleton. In the future this module might handle a pool of queues
    def __init__(self):
        self.__queue = queue.Queue()

    def __str__(self):
        return str(id(self))

    def queue(self):
        return self.__queue
