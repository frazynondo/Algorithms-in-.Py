class Node:
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.rootHelper(data, self.root)

    def rootHelper(self, data, roots):
        if data < roots.data:
            if roots.leftChild is not None:
                self.rootHelper(data, roots.leftChild)
            else:
                roots.leftChild = Node(data, roots)

        else:
            if roots.rightChild is not None:
                self.rootHelper(data, roots.rightChild)
            else:
                roots.rightChild = Node(data, roots)

    def preOrderTraverse(self):
        if self.root:
            self.preOrderHelp(self.root)
        else:
            print("Root is Null")

    def preOrderHelp(self, roots):

        if roots is None:
            return
        else:

            print("--> Current Node = {} ".format(str(roots.data)))
            self.preOrderHelp(roots.leftChild)
            self.preOrderHelp(roots.rightChild)

    def MAX(self):
        if self.root:
            self.maxValHelp(self.root)
        else:
            print("Root is empty")

    def maxValHelp(self, roots):
        if roots.rightChild is not None:
            self.maxValHelp(roots.rightChild)
        else:
            print(roots.data)

    def MIM(self):
        if self.root:
            self.minValHelp(self.root)
        else:
            print("Root is empty")

    def minValHelp(self, roots):
        if roots.leftChild is not None:
            self.minValHelp(roots.leftChild)
        else:
            print(roots.data)


class Compare(object):
    def compareTwoTrees(self, node1: Node, node2: Node):
        if node1 is None and node2 is None:
            return True
        if node1 is None and node2:
            return False
        if node2 is None and node1:
            return False
        return node1.data == node2.data and \
               self.compareTwoTrees(node1.leftChild, node2.leftChild) \
               and self.compareTwoTrees(node1.rightChild, node2.rightChild)

    def BFS_Traverse(self, nodes: Node) -> []:
        if nodes is None:
            return None
        Queue = [nodes]
        Traverse = []
        while Queue:
            temp = Queue.pop(0)
            Traverse.append(temp.data)
            if temp.leftChild:
                Queue.append(temp.leftChild)
            if temp.rightChild:
                Queue.append(temp.rightChild)
        return Traverse

    def DFS_Iterate(self, nodes: Node) -> []:
        if nodes is None:
            return None
        Queue = [nodes]
        Traverse = []
        while Queue:
            temp = Queue.pop()
            Traverse.append(temp.data)
            if temp.rightChild:
                Queue.append(temp.rightChild)
            if temp.leftChild:
                Queue.append(temp.leftChild)
        return Traverse


def StringReverse(peeps: []):
    start = 0
    end = peeps.__len__() - 1
    while start < end:
        peeps[start], peeps[end] = peeps[end], peeps[start]
        # temp = peeps[start]
        # peeps[start] = peeps[end]
        # peeps[end] = temp
        start += 1
        end -= 1
    return peeps


def can_be_constructed(Inp, allow):
    # allowed = 'ab'
    # IN = ['abba', 'bacd', 'baa', 'ghst']
    Allowed = sorted(set(allow))
    results = []
    for x in Inp:
        temps = sorted(set(x))
        start_A = 0
        start_B = 0
        end_A = len(Allowed) - 1
        end_B = len(Inp) - 1
        counts = 0
        while start_A < end_A and start_B < end_B:
            if Allowed[start_A] == temps[start_B]:
                counts += 1
                start_A += 1
            start_B += 1
        if counts == end_A:
            results.append(x)
    print(" ".join(results))


if __name__ == "__main__":


    BST = BinarySearchTree()
    BST.insert(10)
    BST.insert(20)
    BST.insert(5)
    BST.insert(7)
    BST.insert(27)
    # BST.insert(10)
    # BST.insert(20)
    # BST.insert(22)
    # BST.insert(11)
    # BST.insert(12)
    # BST.insert(7)
    # BST.insert(9)
    # BST.insert(2)

    Check = Compare().DFS_Iterate(BST.root)
    print("DFS Stack Results = " + str(Check))
    Checks = Compare().BFS_Traverse(BST.root)
    print("BFS Queue Results = " + str(Checks))
    Frazy = "STREET MUSIC"
    print(str.lower(Frazy))

    # BST1 = BinarySearchTree()
    # BST1.insert(10)
    # BST1.insert(20)
    # BST1.insert(22)
    # BST1.insert(11)
    # BST1.insert(12)
    # BST1.insert(7)
    # BST1.insert(9)
    # BST1.insert(2)
    #
    # Comp = Compare().compareTwoTrees(BST.root, BST1.root)
    # print(Comp)
