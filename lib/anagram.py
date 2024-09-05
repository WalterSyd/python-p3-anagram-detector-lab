# your code goes here!

class Anagram:
    def __init__(self, word):
        #handle case sensitivity
        self.word = word.lower()

    def match(self, words):
        #sort letters of original word
        sorted_word = sorted(self.word)
        #loop through words and return anagrams if they exist else return empty list
        matches = [word for word in words if sorted(word.lower()) == sorted_word]
        return matches

result = Anagram("listen")
answer = result.match(["enlists", "google", "banana"])
print(answer)
