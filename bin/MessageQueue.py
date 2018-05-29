#https://gamedevelopment.tutsplus.com/tutorials/how-to-implement-and-use-a-message-queue-in-your-game--cms-25407

from Entity import Entity

class Message:
    def __init__(self, msgTo, msgFrom, msgType, msgData):
        self.msgTo = msgTo
        self.msgFrom = msgFrom
        self.msgType = msgType
        self.msgData = msgData 
    def __str__(self):
        return "msgTo: %s msgFrom: %s msgType: %s msgData: %s" % (self.msgTo, self.msgFrom, self.msgType, self.msgData)

class MessageQueue:
    def __init__(self):
        self.messages = []
    def add(self, message):
        self.messages.append(message)
    def showAll(self):
        print(self.messages.items())
    def dispatch(self):
        for i in range(len(self.messages)):
            msg = self.messages[i]
            if msg:
                entity = msg.msgTo
                if entity:
                    entity.onMessage(msg)
                self.messages.pop(i)
                i -= 1