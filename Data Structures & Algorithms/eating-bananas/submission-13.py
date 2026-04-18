class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=float('inf')
        while l<=r:
            mid=(l+r)//2
            t = 0
            for val in piles:
                t= t+ math.ceil(val/mid)
            if t<=h:
                r = mid - 1
                res=min(res,mid)
            else:
                l = mid + 1
        return res