class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = 0

        mapFreq = {}
        for i in nums:
            if i in mapFreq.keys():
                mapFreq[i] -= 1
            
            else :
                mapFreq[i] = -1

        mapHeap = [(v, k) for k, v in mapFreq.items()]
        heapq.heapify(mapHeap)
        res = []
        while k:
            res.append(mapHeap[0][1])
            heapq.heappop(mapHeap)
            k -=1
        return res

