class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def find(rate):
            res = 0
            for val in piles:
                res += math.ceil(val/rate)

            return res
        l=1
        r=max(piles)
        res=float('inf')
        while l<=r:
            mid=(l+r)//2
            t = find(mid)
            print(t)
            if t<=h:
                r = mid - 1
                res=min(res,mid)
            else:
                l = mid + 1
        return res