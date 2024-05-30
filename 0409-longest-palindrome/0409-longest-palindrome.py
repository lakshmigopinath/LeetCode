class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        longest_palindrome_length = 0
        
        for count in char_count.values():
            longest_palindrome_length += count // 2 * 2
            if count % 2 == 1 and longest_palindrome_length % 2 == 0:
                longest_palindrome_length += 1
        
        return longest_palindrome_length
