# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        sorted_word = sorted(self.word)

        result = []
        for candidate in word_list:
            if sorted(candidate) == sorted_word and candidate.lower() != self.word.lower():
                result.append(candidate)

        return result


