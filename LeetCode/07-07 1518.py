def numWaterBottles(numBottles: int, numExchange: int) -> int:
    total = 0
    empty = 0
    while numBottles>0:
        total+=numBottles
        empty+=numBottles
        numBottles=empty//numExchange
        empty = empty%numExchange
    return total

numBottles = 9
numExchange = 3
print(numWaterBottles(numBottles, numExchange))

# O(1)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)
