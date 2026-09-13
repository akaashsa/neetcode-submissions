class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums :
            count[num] = count.get(num,0)+1

        listMap = []
        for num in count.keys():
            heapq.heappush(listMap, (count[num],num))
            if len(listMap)>k:
                heapq.heappop(listMap)

        res = []
        while listMap:
                res.append(heapq.heappop(listMap)[1])

        return res
