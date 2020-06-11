#d = {'1': 2, '2': 7, '3': 8, '4': 9}
#indexList = list(d)
#print(indexList)
#first = int(indexList[0])
#print(first)

myList = [2, 7, 8, 9]
goal = 9

#class Solution(object):
#    def twoSum(self, d, target):
#        for i in range(0, len(indexList)-1):
#            for j in range(i+1, len(indexList)):
#                if (d[indexList[i]] + d[indexList[j]] == target):
#                    return [indexList[i], indexList[j]]
"""use the dict structure to give back the information for index and value
if found the correct the combination of index, then give it back as list
"""


class SolutionDict(object):
    def twoSum(self, nums, target):
        dic = dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in dic:
                return [dic[sub], index]
            else:
                dic[value] = index


mySol = SolutionDict()
print(mySol.twoSum(myList,goal))