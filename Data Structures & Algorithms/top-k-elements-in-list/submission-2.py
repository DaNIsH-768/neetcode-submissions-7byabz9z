class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        sorted_map = [(k, v) for k, v in sorted(count_map.items(), key=lambda item: item[1])]
        print(sorted_map)
        
        result = []
        n = len(sorted_map) - 1

        while k > 0:
            result.append(sorted_map[n][0])
            k -= 1
            n -= 1
        
        return result
        

        