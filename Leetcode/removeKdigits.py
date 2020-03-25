class Solution:
    def removeKdigits(self, num, k):
        if not num or len(num) == k:
            return "0"
        if k == 0:
            return num
        idx = num.find('0')
        if 0 <= idx <= k:
            return self.removeKdigits(num[idx+1:], k - idx)
        for i in range(1,len(num)):
            if num[i] < num[i-1]:
                return self.removeKdigits(num[:i-1]+num[i:], k-1)
        return num[:-k]