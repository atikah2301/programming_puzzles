# Easy difficulty

# Constraints:
# 1. length of "strings" list within [1,200]
# 2. length of each string within [0, 200]
# 3. all chars are lowercase letters

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        # Get the minimum length among all strings in the list
        min_len = len(strs[0])
        for str in strs:
            min_len = len(str) if len(str) < min_len else min_len
        # Check the minimum number of first letters among all strings
        for i in range(min_len):
            current_char = strs[0][i]
            match = True
            # If the ith letter in every string matches the ith letter in first string...
            for str in strs:
                if  len(str) >= len(prefix):
                    return prefix
                if current_char != str[i]:
                    match = False
            # ... then add the ith letter to the common prefix
            if match == True:
                prefix += current_char
            else:
                return prefix
        return prefix


if __name__ == '__main__':
    sol = Solution()
    strings = ["flower", "flow", "flight"] # ["dog", "racecar", "car"]
    ans = sol.longestCommonPrefix(strings)
    print(ans)