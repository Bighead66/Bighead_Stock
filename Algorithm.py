d = {'1': 2, '2': 7, '3': 8, '4': 9}
indexList = list(d)
print(indexList)
first = int(indexList[0])
print(first)

goal = 9

class Solution(object):
    def twoSum(self, d, target):
        for i in range(0, len(indexList)-1):
            for j in range(i+1, len(indexList)):
                if (d[indexList[i]] + d[indexList[j]] == target):
                    return [indexList[i], indexList[j]]


class SolutionDict(object):
    def twoSum()


mySol = Solution()
print(mySol.twoSum(d,goal))