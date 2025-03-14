class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            if len(sentence[i]) >= len(searchWord):
                if sentence[i][:len(searchWord)] == searchWord:
                    return i+1
                    break
        return -1