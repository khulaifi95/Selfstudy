# Problem for creating own iterators

# Iterator


class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        # loop through all the values
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


# Generator
# Simple and very low cost


def sentence(sentence):
    for word in sentence.split():
        yield word


my_sentence = Sentence('This is a test')    # iterator class
my_sentence_2 = sentence('This is a test')    # generator

for word in my_sentence:
    print(word)

for word in my_sentence_2:
    print(word)
