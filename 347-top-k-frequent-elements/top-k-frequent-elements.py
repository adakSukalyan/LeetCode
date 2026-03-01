class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        k_ = list(hash.values())
        k_.sort(reverse=True)
        l = []
        for i in range(k):
            for key in hash:
                if hash[key] == k_[i]:
                    l.append(key)
                    hash[key] = -1
                    break
        return l