def single_root_words(root_word: str, *other_words) -> list:
    """Returns a list of words with the same root

    Args:
        root_word: rule to check
        *other_words: words to check

    Returns:
        same_words

    """
    same_words = []
    root_word_l = root_word.lower()
    for i in other_words:
        word_l = i.lower()
        if root_word_l in word_l or word_l in root_word_l:
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
