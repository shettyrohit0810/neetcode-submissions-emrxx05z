
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        h=[]
        for d,f in count.items():
            f=f
            heapq.heappush(h,[f,d])
            while len(h)>k:
                heapq.heappop(h)
        
        return [i for f,i in h]