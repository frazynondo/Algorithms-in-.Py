class Queue(object):
    def __init__(self):
        self.queue = []

    # O(1) running time
    def is_empty(self):
        return self.queue == []

    def Enqueue(self, data):
        self.queue.append(data)

    def Dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def QueueSize(self):
        return self.queue.__len__()

    def peek(self):
        return self.queue[0]


if __name__ == "__main__":
    test = ["Apple", "Onions", "Peach"]
    print("==> " + " - ".join(test))
    del test[0]
    print("==>Del --> " + " - ".join(test))
    test.append("Moon")
    print("==>Append --> " + " - ".join(test))
    del test[0]
    print("==>Del --> " + " - ".join(test))
    del test[0]
    print("==>Del --> " + " - ".join(test))
