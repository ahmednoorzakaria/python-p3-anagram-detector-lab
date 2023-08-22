# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagrams = []
        sorted_word = sorted(self.word.lower())  # Convert to lowercase for case-insensitive comparison

        for candidate in word_list:
            candidate_lower = candidate.lower()
            if candidate_lower != self.word.lower() and sorted(candidate_lower) == sorted_word:
                anagrams.append(candidate)

        return anagrams