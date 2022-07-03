'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        max_len = curr = 0;
        if len(s) < 2: return len(s);
        
        for i, c in enumerate(s):  
            if c in charDict and curr <= charDict[c]:
                curr = charDict[c] + 1;
            else:
                max_len = max(max_len, i-curr+1)
                
            charDict[c]=i;
        return max_len;
            
