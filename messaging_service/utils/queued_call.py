import functools
import threading
from messaging_service.utils.single_queue import WorkQueue


class QueuedCall(object):

    def __init__(self, function):
        self.__function = function                  # function (with aruments) to be executed
        self.__event_signal = threading.Event()     # semaphore to signal when result is ready
        self.__result = object()                    # None could be a valid result

    def call(self):
        self.__result = self.__function()
        self.__event_signal.set()                   # signal that the results is done

    def wait(self):
        self.__event_signal.wait()                  # wait for result done signal

    def get_result(self):
        return self.__result


def redirect(function_impl, *args):
    q = WorkQueue().queue()

    # create a partial object that behaves like a function with arguments passed on
    f = functools.partial(function_impl, *args)

    # queue up the function and with for event to signal work thread is done
    queued_call = QueuedCall(f)
    q.put(queued_call)
    queued_call.wait()
    return queued_call.get_result()

