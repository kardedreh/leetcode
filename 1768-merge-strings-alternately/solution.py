class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        collector = []
        i = j = 0

        while i < len(word1) and j < len(word2):
            collector.append(word1[i] + word2[j])
            i, j = i + 1, j + 1

        if i < len(word1):
            collector.append(word1[i:])

        if j < len(word2):
            collector.append(word2[j:])

        return ''.join(collector)
