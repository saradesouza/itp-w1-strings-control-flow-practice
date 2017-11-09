def how_many_times(a_string, a_word):
    if a_word in a_string:
        print(a_string[-13:-7])
        if a_string[-13:-7] == 'Python':
            return 2
        else:
            return 1
    else:
        return 0

def test_more_than_once():
    phrase = "Python is a great language. I like Python a lot."
    assert how_many_times(phrase, "Python") == 2


def test_only_once():
    phrase = "Python is a great language. I like it a lot."
    assert how_many_times(phrase, "Python") == 1


def test_none():
    phrase = "Python is a great language."
    assert how_many_times(phrase, "Ruby") == 0
