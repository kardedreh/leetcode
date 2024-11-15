class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        total = 0
        for i in range(len(s) - 1): #run second to last for comparison
            if conversion[s[i]] < conversion[s[i+1]]: #if s on [i] is smaller than following s:
                total -= conversion[s[i]] #apply subtraction logic
            else:
                total += conversion[s[i]] #else add it to total

        total += conversion[s[-1]] #last roman cannot be compared to anything - always add it

        return total
