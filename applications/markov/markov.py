import random
import re

start_words = []
word_store = {}


def buildCache(words_list):
    for (index, cur_word) in enumerate(words_list):
        # get next word
        next_word = words_list[index+1] if index < len(words_list)-1 else ""

        # check for start word
        if cur_word[0].isupper() or (cur_word[0] == "\"" and cur_word[1].isupper()):
            start_words.append(cur_word)

        # store the word
        if cur_word not in word_store:
            word_store[cur_word] = [next_word]
        else:
            word_store[cur_word].append(next_word)


def getWord(words_list=start_words) -> tuple:
    key = random.choice(words_list)
    return (key, word_store[key])


def isEndWord(word) -> bool:
    end_words = re.compile(r".*[.?!\"]$")
    return end_words.match(word)


def getSentence():
    output = ""
    cur_word, other_words = getWord()
    while not isEndWord(cur_word):
        output += cur_word + " "
        cur_word, other_words = getWord(other_words)

    # concatinate the last word to output and return
    print(f"({cur_word}, {other_words})")
    return output + cur_word


# Read in all the words in one go
# with open("applications/markov/input.txt") as f:
with open("cs-hash-tables/applications/markov/input.txt") as f:
    words = f.read()
    buildCache(words.split())

    # TODO: construct 5 random sentences
    print(getSentence())
