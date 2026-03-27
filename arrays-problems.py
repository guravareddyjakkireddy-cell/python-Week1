1)	Two Sum
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i
2)	Contains Duplicate
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
3)	Move Zeroes
def move_zeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums
4)	Merge Sorted Arrays
def merge_sorted(nums1, nums2):
    return sorted(nums1 + nums2)
5)	Reverse String
def reverse_string(s):
    return s[::-1]
6)	Valid Palindrome
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
7)	Valid Anagram
def is_anagram(s, t):
    return sorted(s) == sorted(t)
8)	First Unique Character
def first_unique_char(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1
9)	Longest Substring Without Repeating Characters
def longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_ set:
            char_ set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
 return max_len
10)	Intersection of Two Arrays
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
