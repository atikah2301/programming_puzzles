# Easy difficulty

# Constraints:
# 1. Assume input string has length within [1,15]
# 2. Assume input sting only contains valid chars
# 3. Assume output integer is within [1,3999]


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                      "C": 100, "D": 500, "M": 1000,}
        int_val = 0
        length = len(s)
        if length == 1:
            return roman_dict[s]
        for i in range(length):
            if i < length - 1:
                if roman_dict[s[i+1]] > roman_dict[s[i]]:
                    int_val -= roman_dict[s[i]]
                    continue
            int_val += roman_dict[s[i]]
        return int_val

if __name__ == '__main__':
    sol = Solution()
    s = "MCMXCIV"
    ans = sol.romanToInt(s)
    print(ans)
