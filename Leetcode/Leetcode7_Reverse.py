
class Solution(object):
    def reverse(self, x): 
        """
        :type x: int
        :rtype: int
        :给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
        :示例 1:
        输入: 123
        输出: 321
        :示例 2:
        输入: -123
        输出: -321
        示例 3:
        输入: 120
        输出: 21
        注意:
        假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/reverse-integer
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """   
        if -10 < x < 10:
            return x 
        strN = list(str(x))
        strNnew = []
        tempF = strN[0]
        tempL = strN[len(strN)-1]
        for i in range (len(strN)):  
            if tempF == '-': 
                if i == 0:
                    strNnew.append(tempF) 
                    continue
                if tempL == '0':                   
                    if  i != 1:
                        temp = strN[len(strN)-i]
                        strNnew.append(temp) 
                else:
                    temp = strN[len(strN)-i]
                    strNnew.append(temp)                   
            else: 
                if tempL == '0':
                    if i != 0:                     
                        temp = strN[len(strN)-i-1]
                        strNnew.append(temp)
                else:
                    temp = strN[len(strN)-i-1]
                    strNnew.append(temp)
        result =  int("".join(strNnew))     
        if -2147483648 < result < 2147483647:
            return result    
        else:
            return 0

inputN1 = 123
inputN2 = 120
inputN3 = -123
inputN4 = -120
inputN5 = 2**31
inputN6 = -2**31-1
inputN7 = 1534236469
         
mySol = Solution()
print(mySol.reverse(inputN1))
print(mySol.reverse(inputN2))
print(mySol.reverse(inputN3))
print(mySol.reverse(inputN4))
print(mySol.reverse(inputN5))
print(mySol.reverse(inputN6))
print(mySol.reverse(inputN7))

