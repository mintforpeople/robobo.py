import threading
import queue

class AbstractProcessor:
    def __init__(self, state):
        self.state = state
        self.supportedMessages = []
        self.callbacks = {}
        self.callbacklocks = {}
        self._callback_queue = queue.Queue(maxsize=16)
        self._worker_thread = None
        self._worker_lock = threading.Lock()

    def canProcess(self, msg):
        return msg in self.supportedMessages

    def process(self, status):
        name = status["name"]
        value = status["value"]

    def _ensure_worker(self):
        with self._worker_lock:
            if self._worker_thread is None or not self._worker_thread.is_alive():
                self._worker_thread = threading.Thread(
                    target=self._worker_loop,
                    daemon=True,
                    name=f"{self.__class__.__name__}Worker"
                )
                self._worker_thread.start()

    def _worker_loop(self):
        while True:
            try:
                callback, callbackName = self._callback_queue.get(timeout=1.0)
            except queue.Empty:
                continue

            try:
                self.callbacklocks[callbackName] = True
                callback()
            except Exception:
                pass
            finally:
                self.callbacklocks[callbackName] = False
                self._callback_queue.task_done()

    def runCallback(self, callbackName):
        callback = self.callbacks.get(callbackName)
        if callback is not None:
            # Drop duplicate invocation if one is already running
            if self.callbacklocks.get(callbackName, False):
                return

            self._ensure_worker()
            try:
                self._callback_queue.put_nowait((callback, callbackName))
            except queue.Full:
                # Discard stale notification if queue is backed up
                pass
