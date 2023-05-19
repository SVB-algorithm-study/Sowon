class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        length = len(prices)
        max_price = 0
        while j < length:
            diff = prices[j] - prices[i]
            if diff > max_price:
                max_price = diff
            elif prices[i] > prices[j]:
                    i = j
            j+=1

        return max_price