import numpy as np


# sys.getsize gives us the size occupied by a specific object

# Find all duplicates in a list O(n) without using extra memory
def find_duplicates(arr):
    dup = []
    # for i in range(len(arr)):
    for i, c in enumerate(arr):
        print(" I = {} and C == {}".format(i, c))
        # eg array = [1, 1, 2, 3, 3, 4, 5]
        # assign value at index i to j --> at 0 --> j = abs(1) = 1
        j = abs(arr[i])
        # check if index of j = 1 which is arr[1] < than 0
        if arr[j] < 0:
            dup.append(abs(arr[j]))
        # convert j or  arr[arr[i]] to negative
        arr[j] = -arr[j]
    return dup


# Write a function that takes in an array of Int and return the longest Peak
def longestPeak(array):
    # Write your code here.
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] > array[leftIdx + 1]:
            leftIdx -= 1
            rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx
    return longestPeakLength


# Reverse an array space - O(n)
def reverse(num):
    num = list(num)
    start_index = 0
    end_index = len(num) - 1
    while start_index < end_index:
        num[start_index], num[end_index] = num[end_index], num[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
    return ''.join(num)


# Anagram check function Space O(n) memory O(1)
def anagrams(string):
    revers = reverse(string)
    sizes = len(string)
    start1 = 0
    start2 = 0
    while start1 < sizes and start2 < sizes:
        if not (string[start1] == revers[start2]):
            return False
        return True


# Palindrome check function O(n)
def is_palindrome(string):
    reverse_st = reverse(string)
    if string == reverse_st:
        return True
    return False


# Reverse an Int number function O(n)
def reverses(T):
    C = ''
    while T > 0:
        S = T % 10
        T = int(T / 10)
        C = C + str(S)
    return int(C)


# if __name__ == "__main__":
#     a = [1, 3, 4, 5, 6, 9]
# print(reverses(Tech))
# print("This string is Anagram? ", anagrams("fluster"))

# print(20 // 2)
# student = {"name": "Frazy", "age": 25, "courses": ["Math", "CompSci"]}
# print("Student 1 -->", student)
# student.update({"name": "Zhiqi", "age": 26, "phone": "514-6687"})
# print("Student 2 -->", student)
# print("Courses -->", student["courses"][0])
#
# for key, values in student.items():
#     print("{} : {}".format(key, values))

# z = "restful"
# R = "fulrest"


def is_Anagram(R, z):
    for i in z:
        if not (i in R):
            return False
    return True


if __name__ == "__main__":
    Rest = "restful"
    Full = "fulrest"
    print(is_Anagram(Rest, Full))
