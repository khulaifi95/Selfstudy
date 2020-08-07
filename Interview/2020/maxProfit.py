from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = int(1e9)
        maxprofit = 0

        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)

        return maxprofit
