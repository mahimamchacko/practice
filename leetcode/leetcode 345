# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        word = list(s)

        first = 0
        firVowel = False
        last = len(s) - 1
        lasVowel = False

        while first < last:
            if not(firVowel) and word[first] in vowels:
                firVowel = True
            elif not(firVowel):
                first += 1
            
            if not(lasVowel) and word[last] in vowels:
                lasVowel = True
            elif not(lasVowel):
                last -= 1
            
            if firVowel and lasVowel:
                temp = word[last]
                word[last] = word[first]
                word[first] = temp
                firVowel = lasVowel = False
                first += 1
                last -= 1
        
        return "".join(word)