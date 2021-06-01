import re

class QueenProblem:

    def __init__(self, n):
        self.n = n
        self.chess_table = [[None for i in range(n)] for j in range(n)]

    def Print(self):
        print(self.chess_table)


if __name__ == '__main__':
    xml = "<data>\n<items>" \
          "\n<item name='item1''>item1abc</item>" \
          "\n<item name='item2'>item2abc</item>\n</items>\n</data>"
    print(xml)
    # for i in xml.split(" "):
    #     print(i)
    temp = re.split('[\s\n</>]', xml)
    print(temp)
