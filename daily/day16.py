"""Day 16 circle buffers!  :)"""

def get_next(n):
    """Yield a continuing index based on size n."""
    yield 0
    c = 1
    while True:
        yield c % n
        c += 1

class Logger:
    def __init__(self, buff_size):
        self._idx = get_next(buff_size)
        self.buff = [None] * buff_size

    @property
    def idx(self):
        return next(self._idx)

    def append_msg(self, msg):
        """Append a message to the buffer."""
        self.buff[self.idx] = msg

    def __str__(self):
        return str(self.buff)

if __name__ == "__main__":
    logger = Logger(10)
    for i in range(20):
        logger.append_msg(f"Message number {i}")
        print(logger)
