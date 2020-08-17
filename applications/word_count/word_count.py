import re


def word_count(s):
    results = {}
    any_whitespace = re.compile(r'\s+')
    non_word_chars = re.compile(r'[":;,\.\-=\+/\|\[\]{}\(\)\*\^&\\]')

    words = any_whitespace.split(s)
    for word in words:
        word = word.lower()
        word = non_word_chars.sub("", word)

        if word in results:
            results[word] += 1
        elif word != "":
            results[word] = 1

    return results


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
