def first_half(a_string):
    string_length = len(a_string)
    half_length = int(string_length / 2)
    if string_length % 2 == 0:
        return a_string[:half_length]
    else:
        return a_string[:half_length + 1]


def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'
