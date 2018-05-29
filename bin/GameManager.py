from MessageQueue import MessageQueue

class GameManager:
    def __init__(self):
        self.messageQueue = MessageQueue()
    def update(self):
        self.messageQueue.dispatch()