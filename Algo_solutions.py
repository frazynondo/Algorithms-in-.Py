import numpy as np


# sys.getsize gives us the size occupied by a specific object

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



if __name__ == "__main__":
    Rest = "restful"
    Full = "fulrest"
    maps = {"{": "}", "(": ")", "[": "]"}
    print(maps.get("("))
    stack = []
    string = "(){}[]"
    for i in string:
        if i in maps:
            stack.append(i)
            # print("Found: {} with Value: {}".format(i, maps.get(i)))
        elif len(stack) != 0 and maps.get(i) == maps.get(stack[-1]):
            print("maps print ", maps.get(stack[-1]))
            stack.pop()
        else:
            print("Frazy")

