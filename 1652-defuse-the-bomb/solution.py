class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n #initialize result list with all 0s

        if k == 0:
            return result #zero case, return 0 list

        for curr_i in range(n):
            sum_for_curr_i = 0

            prev_i = (curr_i - 1) % n
            next_i = (curr_i + 1) % n

            if k < 0:
                for i in range(1, abs(k) + 1):
                    sum_for_curr_i += code[prev_i]
                    prev_i = (prev_i - 1) % n

            else: #k > 0
                for i in range(1, k + 1):
                    sum_for_curr_i += code[next_i]
                    next_i = (next_i + 1) % n
            
            result[curr_i] = sum_for_curr_i

        return result
