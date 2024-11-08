# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation:

# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]

# Explanation:

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

# Constraints:

# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_dict = {}
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        
        result = []
        for i in range(len(s) - total_len + 1):
            seen = {}
            for j in range(word_count):
                start = i + j * word_len
                end = i + (j + 1) * word_len
                word = s[start:end]
                if word in word_dict:
                    if word in seen:
                        seen[word] += 1
                    else:
                        seen[word] = 1
                    if seen[word] > word_dict[word]:
                        break
                else:
                    break
            if seen == word_dict:
                result.append(i)
        return result
    
# Time complexity: O(n*m) where n is the length of s and m is the length of words
# Space complexity: O(m) where m is the length of words

# Let's test the solution
sol = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo","bar"])) # [0,9]
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])) # []
print(sol.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])) # [6,9,12]
# The solution works as expected
