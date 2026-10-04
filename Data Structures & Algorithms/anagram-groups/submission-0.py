class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            cnt = [0] * 26

            for j in range(len(s)):
                cnt[ord(s[j]) - ord('a')] += 1

            key = tuple(cnt)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())