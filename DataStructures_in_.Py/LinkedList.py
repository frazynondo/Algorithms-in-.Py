class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    # Insert is O(1)
    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_Node = Node(data)

        if self.head is None:
            self.head = new_Node
        else:
            new_Node.nexNode = self.head
            self.head = new_Node

    def insert_end(self, data):
        if self.head is None:
            self.insert_start(data)
            return

        new_n = Node(data)
        tempNode = self.head
        self.numOfNodes = self.numOfNodes + 1
        # Linear running time = O(n)
        while tempNode.nextNode is not None:
            tempNode = tempNode.nextNode
        tempNode.nextNode = new_n

    def size_of_list(self):
        return self.numOfNodes

    def traverse(self):
        tempNode = self.head

        while tempNode is not None:
            print(tempNode.data)
            tempNode = tempNode.nextNode
            # if tempNode.nextNode is not None:
            #     tempNode = tempNode.nextNode

#
# linkedList = LinkedList()
# linkedList.insert_end(4)
# linkedList.insert_end(3)
# linkedList.insert_end(5)
# linkedList.insert_end(6)
# linkedList.traverse()
