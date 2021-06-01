import math
from collections import defaultdict


def dictionarySearch():
    tests = ['abba', 'bacd', 'baa', 'ghst', 'baa', 'bacd', 'bacd']
    keys = [12, 14, 15, 16]
    # result = dict(zip(tests, keys))
    result = {}
    for J in tests:
        if J in result.keys():
            temp = result.get(J) + 1
            result.update({J: temp})
        else:
            result[J] = 1
            # result.update({i: 1})

    for k, v in result.items():
        print("key: {} --> Value: {}".format(k, v))
    print("Items : ", result.items())
    # val = {}
    # for i in temps:
    #     if temps.count(i) > 1:
    #         num = temps.count(i)
    #         print("Key: {} and Value: {}".format(i, num))
    #     else:
    #         val[i] = 1
    # print(val)


if __name__ == "__main__":
    tem = "frazy nondo is the best"
    temp = [1,9, 2, 5, 7, 10, 13, 14, 15, 22]
    temp.sort()
    T = temp
    se = set()
    se.add(2)
    se.add(5)
    se.add(6)
    se.add(2)
    print(se)
    # D = {}
    # for count, i in enumerate(temp):
    #     D[count] = i
    # D.get()
    # for k, v in D.items():
    #     print("Key {} Value {}".format(k,v))


    # t = int(len(temp)/2)
    # print(temp[t])
    # P = len(temp) - t
    # t = P/2
    # T = [3]
    # simps = (1, "B")
    # stack = [temp]
    # print("Stach is : " + str(stack[-1]))
    # team, people = stack.pop()
    # print("team: {} and people: {}".format(team, people))


    # print(temp[int(t)])
    # P = len(temp) - t
    # t = P // 2
    # print(temp[int(t)])
    # temps = defaultdict(int)
    # for i in tem:
    #     if i != " ":
    #         temps[i] += 1
    # for k, v in temps.items():
    #     print("{} : {}".format(k, v))
    # event = list(map(lambda x: x + str("++-"), list(temps)))
    # event = list(map(lambda x: x * 2, list(temp)))
    # print(event)
    # tem = list(temps)

    # val[i - 'a'] += 1
    # print(temps.split())
    # print(tem)
