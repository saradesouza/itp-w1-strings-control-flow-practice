def first_half(a_string):
    stringlength = len(a_string)
    if stringlength % 2 == 0:
        #print(stringlength)
        halfstring = stringlength / 2
        #print(halfstring)
        #print(a_string[:halfstring])
        return(a_string[:halfstring])
    else:
        #print(stringlength)
        halfstring = stringlength / 2
        #print(halfstring)
        #print(a_string[:halfstring])
        return(a_string[:halfstring + 1])
        
def test_first_half_with_even_length_string():
    assert first_half('abcdef') == 'abc'


def test_first_half_with_odd_length_string():
    assert first_half('abcXdef') == 'abcX'
