class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if n==m:
            seen = set()
            for i in range(n):
                key=s[i]
                if key in seen:
                    continue
                seen.add(key)
                counts=0
                countt=0
                for j in range(n):
                    if s[j]==key:
                        counts+=1
                for k in range(n):
                    if t[k]==key:
                        countt+=1
                if counts != countt:
                    return False
            return True
        else:
            return False