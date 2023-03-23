"""
You are given a class called Sentence , which takes a string such as 'hello world'.
You need to provide an interface such that the indexer returns a flyweight that can be used to capitalize a
particular word in the sentence.
"""


class Sentence:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.word_formatting = []

    class TextWord:

        def __init__(self, word_position, capitalize=False):
            self.word_position = word_position
            self.capitalize = capitalize

        def is_word_formatted(self, word_position):
            return self.word_position == word_position

    def __getitem__(self, word_position):
        text_word = self.TextWord(word_position)
        self.word_formatting.append(text_word)
        return text_word

    def __str__(self):
        result = []
        for index, word in enumerate(self.plain_text.split(' ')):
            for r in self.word_formatting:
                if r.is_word_formatted(index) and r.capitalize:
                    word = word.upper()
            result.append(word)

        return ' '.join(result)


sentence = Sentence('hello world')
sentence[1].capitalize = True
print(sentence)  # writes "hello WORLD"
