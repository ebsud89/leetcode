from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        idx, i, wlen = 0, 0, 0
        words.sort()
        for n in words:
            wl = list(n)
            if wl[0] > list(words[idx])[0]:
                continue
            if (wlen < len(wl)):
                wlen = len(list(n))
                idx = i
            i += 1

        return words[idx]

s = Solution()
words = ["w","wo","wor", "world123","worl", "world"]
print(s.longestWord(words))
words = ["a","banana","app","appl","ap","apply","apple"]
print(s.longestWord(words))