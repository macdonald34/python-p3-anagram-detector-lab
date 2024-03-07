# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        return [anagram for anagram in possible_anagrams if self.is_anagram(anagram)]

    def is_anagram(self, candidate):
        return sorted(candidate.lower()) == sorted(self.word.lower())