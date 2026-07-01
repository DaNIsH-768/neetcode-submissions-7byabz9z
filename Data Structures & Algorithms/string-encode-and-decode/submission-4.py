class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "e"
        
        return ",ss,".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "e":
            return []

        return s.split(",ss,")