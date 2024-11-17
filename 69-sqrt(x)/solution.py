class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: #case for 0 and 1
            return x

        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid**2 == x:
                return mid #exact square case
            elif mid**2 < x:
                low = mid + 1
            else:
                high = mid - 1

        return high
