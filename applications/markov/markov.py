import random
import re

start_words = {}
word_store = {}


def store_into(cache, word, next_word):
    if word not in cache:
        cache[word] = [next_word]
    else:
        cache[word].append(next_word)


def getWord(cache) -> str:
    return random.choice(list(cache.keys()))


def isEndWord(word) -> bool:
    end_words = re.compile(r".*[.?!\"]$")
    return end_words.match(word)


def getSentence():
    output = ""
    next_word = getWord(start_words)
    while not isEndWord(next_word):
        output += next_word + " "
        next_word = getWord(word_store)

    # concatinate the last word to output and return
    return output + next_word


# Read in all the words in one go
# with open("applications/markov/input.txt") as f:
with open("cs-hash-tables/applications/markov/input.txt") as f:
    words = f.read()

    words_list = words.split()
    for (index, cur_word) in enumerate(words_list):
        # get next word
        next_word = words_list[index+1] if index < len(words_list)-1 else ""

        # check for start word
        if cur_word[0].isupper() or (cur_word[0] == "\"" and cur_word[1].isupper()):
            store_into(start_words, cur_word, next_word)
        else:
            store_into(word_store, cur_word, next_word)

    # TODO: construct 5 random sentences
    print(getSentence())

if __name__ == "__main__":
    pass
    # print(start_words)
    # print(word_store)
