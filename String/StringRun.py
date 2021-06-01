from typing import List


class Solutions(object):
    # Find all duplicates in a list O(n) without using extra memory

    # Write a function that takes in an array of Int and return the longest Peak

    # Reverse an array space - O(n)
    def reverse(self, num):
        num = list(num)
        start_index = 0
        end_index = len(num) - 1
        while start_index < end_index:
            num[start_index], num[end_index] = num[end_index], num[start_index]
            start_index = start_index + 1
            end_index = end_index - 1
        return ''.join(num)

    # Anagram check function Space O(n) memory O(1)
    def anagrams(self, string):
        revers = self.reverse(string)
        sizes = len(string)
        start1 = 0
        start2 = 0
        while start1 < sizes and start2 < sizes:
            if not (string[start1] == revers[start2]):
                return False
            return True

    # Palindrome check function O(n)
    def is_palindrome(self, string):
        reverse_st = self.reverse(string)
        if string == reverse_st:
            return True
        return False

    # Reverse an Int number function O(n)
    def reverses(self, T):
        C = ''
        while T > 0:
            S = T % 10
            T = int(T / 10)
            C = C + str(S)
        return int(C)

    def is_Anagram(self, R, z):
        for i in z:
            if not (i in R):
                return False
        return True

    def reverseInt(self, num):
        Temp = str(self, num)
        Res = ""
        for i in range(len(Temp) - 1, 0, -1):
            Res += Temp[i]
        Res += Temp[0]

    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return False
        stack = []
        maps = {"{": "}", "(": ")", "[": "]"}
        for i in s:
            if i in maps:
                stack.append(i)
                # print("Found: {} with Value: {}".format(i, maps.get(i)))
            elif len(stack) > 0 and i == maps.get(stack[-1]):
                stack.pop()
            else:
                return False
        return len(stack) == 0

    def longestValidParentheses(self, s: str) -> int:
        pass

    def numberofSteps(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        temp = [1, 2, 3]
        i = 3
        right = number + 1
        while i < right:
            temp.append(temp[i - 1] + temp[i - 2])
            i += 1
        return temp[number - 1]

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        target = {}
        count = 2
        high = 0
        for i in range(2, len(arr)):
            if arr[i] in target:
                count += 1 + target.get(arr[i])
            if arr[i - 2] + arr[i - 1] == arr[i]:
                count += 1
            else:
                target[arr[i - 2] + arr[i - 1]] = count
                high = max(high, count)
                count = 0
        if count > high:
            high = count
        return high

    def reverseVowels(self, s: str) -> str:
        temp = list(s)
        left = 0
        right = len(s) - 1
        V = {'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u'}
        if len(s) <= 0:
            return s
        if len(s) == 1 and temp[0].lower() in V and temp[1].lower() in V:
            S = temp[0]
            temp[0] = temp[1]
            temp[1] = S
            return temp
        while left <= right:
            if temp[left].lower() in V:
                T = left
                while right >= T:
                    if temp[right].lower() in V:
                        break
                    else:
                        right -= 1
            if temp[right].lower() in V:
                T = right
                while left <= T:
                    if temp[left].lower() in V:
                        break
                    else:
                        left += 1
            if temp[left].lower() in V and temp[right].lower() in V:
                S = temp[left]
                temp[left] = temp[right]
                temp[right] = S
            left += 1
            right -= 1
        return "".join(temp)


if __name__ == '__main__':
    # arr = [1, 2, 3, 4, 5, 6, 7, 8]
    arr = [1, 3, 7, 11, 12, 14, 18]
    # arr = [1, 2, 3, 5, 8]
    # target = {}
    # count = 2
    # high = 0



