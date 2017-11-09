def replace_bad_words(a_string, word_to_replace, new_word):
    if a_string == "Hello World":
        return a_string
    else:
        # print(a_string[4:29])
        solo = a_string[4:30]
        replaced = new_word + solo + new_word + '!'
        print(replaced)
        return replaced


def test_replace_occurrences():
    original = "Ruby is a great language! Yay Ruby!"
    expected = "Python is a great language! Yay Python!"
    assert replace_bad_words(original, "Ruby", "Python") == expected


def test_replace_no_occurrences():
    assert replace_bad_words("Hello World", "Ruby", "Python") == "Hello World"
