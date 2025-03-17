def main():
    print("Hello from neetcode-sandbox!")


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left_index = 0
        right_index = 1
        max_len = 1
        i = right_index
        while i < len(s):
            # Exact place where it is on last occurence and jump to that position
            substring = s[left_index:right_index]
            last_index = substring.rfind(s[i])
            if last_index != -1:
                # Adjust last_index
                last_index += left_index
                # Add maximum selection
                new_max = right_index - left_index
                if new_max > max_len:
                    max_len = new_max
                left_index = last_index + 1
                right_index = last_index + 2
                if i != len(s) - 1:
                    i = right_index
                else:
                    i += 1
            else:
                right_index += 1
                i += 1
                new_max = right_index - left_index
                if new_max > max_len:
                    max_len = new_max
            # TODO: jump with i accordingly
        return max_len


if __name__ == "__main__":
    main()
