class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array = list(range(1, n + 1))
        result = []

        for i in array:
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
