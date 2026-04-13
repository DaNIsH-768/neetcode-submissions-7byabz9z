class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for char in s:
            if s_map.get(char, 0) != 0:
                s_map[char] = s_map[char] + 1
            else:
                s_map[char] = 1
        
        for char in t:
            if t_map.get(char, 0) != 0:
                t_map[char] = t_map[char] + 1
            else:
                t_map[char] = 1

        return s_map == t_map
        