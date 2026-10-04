class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cm_pre = []
        i = 0

        while True:
            if i >= len(strs[0]):
                break

            ch = strs[0][i]

            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return ''.join(cm_pre)

            cm_pre.append(ch)
            i += 1

        return ''.join(cm_pre)