class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}

        for char in strs:
            sorted_char = "".join(sorted(char))
            if sorted_char in str_map:
                str_map[sorted_char].append(char)
            else:
                str_map[sorted_char] = [char]
        
        return list(str_map.values())


