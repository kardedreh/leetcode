class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""

        while columnNumber > 0: 
            columnNumber -= 1 #adjust to start from 1
            answer = chr(ord("A") + columnNumber % 26) + answer
            columnNumber //= 26 #reduce num for next conversion

        return answer
