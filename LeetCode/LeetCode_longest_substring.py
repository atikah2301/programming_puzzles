# Medium difficulty

# For a given string, the function should return the length of the longest continuous substring
# which has no repeating characters
# e.g. abccbb has substrings a, b, c, ab, bc, cb, abc and the longest is abc

class Solution:
    ## Naive solution with time complexity O(n^3),
    ## since nested loop has time complexity O(n^2) and "if .. in .." has time complexity O(n)
    ## Space complexity is O(n) since we are storing the substring with at most length n

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     longest = 1 if s else 0
    #     repeats = False
    #     for i in range(len(s)):
    #         print(f"i = {i}: {s[i]}")
    #         sub = s[i]
    #
    #         for j in range(i+1,len(s)):
    #             print(f"\tj = {j}: {s[j]}, {sub}")
    #             if s[j] in sub:
    #                 repeats = True
    #                 break
    #             sub += s[j]
    #
    #         longest = len(sub) if len(sub) > longest else longest
    #
    #     longest = longest if repeats else len(s)
    #     return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        result = 0
        char_dict = {}
        while end != len(s)+1:
            result = end - start + 1 if end - start + 1 > result else result
            if s[end] not in char_dict:
                char_dict[s[end]] = 1
                end += 1
            elif char_dict[s[end]] == 0:
                char_dict[s[end]] = 1
                end += 1
            else:
                char_dict[s[start]] -= 1
                start += 1

            print(f"start={start}, end={end}")
        return result




if __name__ == '__main__':
    sol = Solution()
    s = "pwwkew"
    ans = sol.lengthOfLongestSubstring(s)
    print(ans)

0,0
0,1
0,2 !
1,2 !
2,2
2,3
2,4
2,5 !
3,5
5-3+1=3 
