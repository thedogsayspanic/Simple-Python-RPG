from MessageQueue import MessageQueue

class PlayState:
    def __init__(self):
        self.messageQueue = MessageQueue()
    def update(self):
        self.messageQueue.dispatch()