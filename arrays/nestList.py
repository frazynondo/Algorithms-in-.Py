

class Solutions(object):

    @classmethod
    def twoNumberSum(arr, target):
        arr.sort()
        lefts, rights = 0, arr.__len__() - 1
        temp = []
        # O(N) space because we use extra list and O(N) time complexity
        while lefts <= rights:
            if arr[lefts] + arr[rights] == target:
                temp.append("{} and {} at index {} and {}".format(arr[lefts], arr[rights], lefts, rights))
                lefts += 1
                rights -= 1
            elif arr[lefts] + arr[rights] > target:
                rights -= 1
            else:
                lefts += 1
        return "\n".join(temp)

    def numOfIslands(self, IslandArr):
        count = 0
        for i in range(len(IslandArr)):
            for j in range(len(IslandArr[0])):
                if IslandArr[i][j] == '1':
                    count += self.islandHelper(IslandArr, i, j)
        return count

    def islandHelper(self, ar, i, j):
        if i < 0 or i >= len(ar) or j < 0 or j >= len(ar[0]) or ar[i][j] == '0':
            return 0
        else:
            ar[i][j] = '0'
            self.islandHelper(ar, i + 1, j)
            self.islandHelper(ar, i - 1, j)
            self.islandHelper(ar, i, j + 1)
            self.islandHelper(ar, i, j - 1)
        return 1

    def SpiralTraverse(self, array):
        left, right = 0, len(li[0]) - 1
        top, bottom = 0, li.__len__() - 1
        inc = 0
        results = []
        while left <= right and top <= bottom:
            inc = left
            for i in range(inc, right):
                results.append(array[top][i])

            inc = top
            for i in range(inc, bottom):
                results.append(array[i][right])

            inc = right
            for i in range(inc, left, -1):
                results.append(array[bottom][i])

            inc = bottom
            for i in range(inc, top, -1):
                results.append(array[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return "".join(str(results))

    def nextPermutation(self, num):
        res = [int(x) for x in str(num)]
        I = len(res) - 2
        print(" RES is ", res)

        for i in range(len(res) - 1, 0, -1):
            print("Loop R = ", i)
            if res[I] < res[i]:
                break
            else:
                I -= 1
        print(" I is ", I)
        if I <= 0:
            left, right = 0, len(res) - 1
            while left < right:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
            return res
        for i in range(len(res) - 1, I + 1, -1):
            if res[i] > res[I]:
                res[i], res[I] = res[I], res[i]
                break
        left, right = I + 1, len(res) - 1

        while left <= right:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
        res = [str(x) for x in res]
        res = "".join(res)
        return int(res)

    def runLengthEncode(self, string):
        dicts = {}
        results = ""
        for i in string:
            if i in dicts.keys():
                t = dicts.get(i) + 1
                dicts.update({i: t})
            else:
                dicts[i] = 1
        for k, v in dicts.items():
            if v > 9:
                while v > 9:
                    v = v - 9
                    results += str(9)+k
            results += str(v)+k
        return results

    def useOfCapital(self, string):
        pass



if __name__ == "__main__":
    island = [['0', '0', '1', '1'],
              ['1', '0', '0', '1'],
              ['0', '0', '1', '0'],
              ['1', '1', '0', '0']]
    li = [[1, 5, 9, 13],
          [2, 6, 10, 14],
          [3, 7, 11, 15],
          [4, 8, 12, 16]]
    check = [2, 3, 4, 5, 6]
    checks = "AAAAAAAAAAAAABBCCCCDD"
    String = "aAaAaaaaaAaaaAAAABbbbBBBB"

    # print(chr(65) < chr(90))
    # for i in range(65, 90):
    #     print(chr(i))
    # print("Two number sum found are:\n {}".format(Solutions.twoNumberSum(check, 7)))
    temp = Solutions()
    numbs = 1349532
    N = 4321
    array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    index = 0
    result = []


    # for i in range(len(check) - 1, 0, -1):
    #     print("i is ", check[i])
    # print(temp.nextPermutation(numbs))

    # print(res[0])
    # print(temp.nextPermutation(numbs))

    # for j in range(len(li[0])):
    #     print(li[j][end])
    #     end -= 1

# print(X)
# for i in range(len(li)):
#     for j in range(len(li[0])):
# temp = li[i - 1][j] + li[i][j - 1]
# print(li[i - 1][j], "and", li[i][j - 1], "==", temp, "at", li[i][j], "\n")
