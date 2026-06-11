class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)

        for char in strs:
            sorted_char = "".join(sorted(char))
            str_map[sorted_char].append(char)
        
        return list(str_map.values())


