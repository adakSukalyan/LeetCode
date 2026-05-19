1class Solution:
2    def removeOccurrences(self, s: str, part: str) -> str:
3        while (part in s):
4            s=s.replace(part,"",1)
5        return s