import random

start_words = {}
word_store = {}


def store_into(cache, word, next_word):
    if word not in cache:
        cache[word] = [next_word]
    else:
        cache[word].append(next_word)


# Read in all the words in one go
with open("cs-hash-tables/applications/markov/input.txt") as f:
    words = f.read()

    # TODO: analyze which words can follow other words
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
    print(start_words)
    print(word_store)
