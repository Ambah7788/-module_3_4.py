def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:

        if root_word in word:
            same_words.append(word)

    return same_words


result = single_root_words('кот', 'котенок', 'собака', 'котик', 'птица')
print(result)
