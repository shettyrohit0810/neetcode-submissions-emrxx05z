class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        dist=0
        for i,j in points:
            dist=(i**2)+(j**2)
            heapq.heappush(h,[-dist,i,j])
        while len(h)>k:
            heapq.heappop(h)

        return [[i,j] for dist,i,j in h]