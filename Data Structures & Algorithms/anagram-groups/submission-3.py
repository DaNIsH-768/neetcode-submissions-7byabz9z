class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """str_map = defaultdict(list)

        for char in strs:
            sorted_char = "".join(sorted(char))
            str_map[sorted_char].append(char)
        
        return list(str_map.values())"""

        group = defaultdict(list)

        for word in strs:
            word_list = [0] * 26
            for c in word:
                word_list[ord(c) - ord("a")] += 1
            
            group[tuple(word_list)].append(word)
        
        return list(group.values())





