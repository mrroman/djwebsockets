
class WebSocket:
    loop = None

    def __init__(self, socket, close, send_queue):
        self.socket = socket
        self.close_handler = close
        self.send_queue = send_queue
        self.id = id(socket)
        self.closed = False

    def send(self, Message):
        self.loop.call_soon_threadsafe(self._send, Message)

    def _send(self, Message):
        self.send_queue.put_nowait(Message)

    def close(self):
        self.closed = True
        self.loop.call_soon_threadsafe(self._close)

    def _close(self):
        self.close_handler.set_result(-1)
