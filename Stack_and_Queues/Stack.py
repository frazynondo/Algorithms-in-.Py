class Stack(object):
    def __init__(self):
        self.stack = []
        self.max = []
        self.count = -1

    def is_empty(self):
        return self.stack == []

    def Push(self, data):
        self.stack.append(data)
        self.count += 1
        temp = self.stack
        temp.sort()
        self.max = temp
        return self

    def pop(self):
        data = self.stack[self.count]
        del self.stack[self.count]
        self.count -= 1
        temp = self.stack
        temp.sort()
        self.max = temp
        return data

    def remove(self, data):
        for ind, temps in enumerate(self.stack):
            if self.stack[ind] == data:
                del self.stack[ind]
                self.count -= 1
                temp = self.stack
                temp.sort()
                self.max = temp
                # return "Found Data's"
                return -1

    def MaxNumber(self):
        return self.max[-1]

    def peek(self):
        return self.stack[self.count]


if __name__ == "__main__":
    stack = Stack()
    stack.Push(1).Push(6).Push(9).Push(7)
    print(stack.MaxNumber())
    # print(stack.remove("Frazy"))
    # print(" - ".join(stack.peek()))
