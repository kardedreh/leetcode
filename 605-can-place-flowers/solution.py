class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True

        return False