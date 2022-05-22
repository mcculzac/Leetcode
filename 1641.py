# https://leetcode.com/problems/count-sorted-vowel-strings/
# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

# Example 1:

# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
# Example 2:

# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.


# TOO SLOW.

class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')
        output_strs = set()
        working_set = {char for char in vowels}
        for i in range(n-1):
            new_set = set()

            for individual_try in working_set:
                for char in vowels:
                    if char >= individual_try[-1]:
                        new_set.add(individual_try + char)
            working_set = new_set
        return len(working_set)
                
class SpoilerSolution:
    def countVowelStrings(self, n: int) -> int:
        vowels = "aeiou"
        dp = {}
        def count(n, c):
            if (n, c) in dp: 
                return dp[(n, c)]
            sum = 0
            index = vowels.find(c)
            if n == 1:
                return 5 - index
            for i in range(index, 5):
                sum += count(n - 1, vowels[i])
            dp[(n, c)] = sum
            return sum
        return count(n, "")

tests = [
    (1, 5),
    (2, 15),
    (33, 66045),
    (50, 316251)
]

s = Solution()
for test in tests:
    print(f'inp: {test[0]}, out: {s.countVowelStrings(test[0])}, expected: {test[1]}')