import threading

from messaging_service.service.routes import flask_app
from messaging_service.utils.single_queue import WorkQueue


def work():
    q = WorkQueue().queue()
    while True:
        if not q.empty():
            q.get().call()


def main():
    # turn on the worker thread
    work_thread = threading.Thread(target=work)
    work_thread.setDaemon(True)
    work_thread.start()

    # turn on the flask rest service in the main thread
    flask_app.run(debug=True)


if __name__ == '__main__':
    main()