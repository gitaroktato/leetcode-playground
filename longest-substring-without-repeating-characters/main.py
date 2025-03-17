def main():
    print("Hello from neetcode-sandbox!")


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            result = max(result, len(chars))
        return result


if __name__ == "__main__":
    main()
