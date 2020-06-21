class Solution:
    def romanToInt(self, s: str) -> int:
        dictRoman = {'I':'1', 'V':'5', 'X':'10', 'L':'50', 'C':'100', 'D':'500', 'M':'1000'}
        #strL = list(s)
        #print(strL)
        tempSum = 0
        temp = 0
        for i in range(len(s)):
            key = s[i]
            lenN = len(s)
            if key == 'I' and i < (len(s)-1):
                if (s[i+1] == 'V' or s[i+1] == 'X'):
                    temp = -1*int(dictRoman[key])
                    tempSum = tempSum + temp
                    continue
                else:
                    temp = int(dictRoman[key]) 
            elif key == 'X'and i < (len(s)-1):
                if (s[i+1] == 'L' or s[i+1] == 'C'):
                    temp = -1*int(dictRoman[key])
                    tempSum = tempSum + temp
                    #if i == (len(s) -2):
                    continue
                else:
                    temp = int(dictRoman[key]) 
            elif key == 'C'and i < (len(s)-1):
                if (s[i+1] == 'D' or s[i+1] == 'M'):
                    temp = -1*int(dictRoman[key])
                    tempSum = tempSum + temp
                    continue
                else:
                    temp = int(dictRoman[key]) 
            else:
                temp = int(dictRoman[key]) 
            tempSum = tempSum + temp
        if (1<= tempSum <= 3999):
            return tempSum


inputN1 = 'II' # 2
inputN2 = 'III' #3
inputN3 = 'XX'  #20'
inputN4 = 'CC' #200
inputN5 = 'VI' #6
inputN6 = 'IV' #4
inputN7 = 'IX' #9
inputN8 = 'XL'#40
inputN9 = 'XC' #90
inputN10 = 'CD' #400
inputN11 = 'CM' #900
inputN12 = "MIX" #1009
inputN13 = "MCMXCIV" #2216->1994


mySol = Solution()
print(mySol.romanToInt(inputN1))
print(mySol.romanToInt(inputN2))
print(mySol.romanToInt(inputN3))
print(mySol.romanToInt(inputN4))
print(mySol.romanToInt(inputN5))
print(mySol.romanToInt(inputN6))
print(mySol.romanToInt(inputN7))
print(mySol.romanToInt(inputN8))
print(mySol.romanToInt(inputN9))
print(mySol.romanToInt(inputN10))
print(mySol.romanToInt(inputN11))
print(mySol.romanToInt(inputN12))
print(mySol.romanToInt(inputN13))