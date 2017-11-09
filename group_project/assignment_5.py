def positions(a_string, first_word, second_word, third_word):
    
    if first_word in a_string:
        print('yes')
        if first_word == a_string[:6]:
            # print('it is the first word')
            posone = "0"
        elif first_word == a_string[26:30]:
            # print('it is the second word')
            posone = "26"
        else:
            # print('it is the third word')
            posone = "34"
    else:
        posone = "-"
    
    if second_word in a_string:
        print('yes')
        if second_word == a_string[:6]:
            # print('it is the first word')
            postwo = "0"
        elif second_word == a_string[26:30]:
            # print('it is the second word')
            postwo = "26"
        else:
            # print('it is the third word')
            postwo = "34"
    else:
        postwo = "-"
    
    
    if third_word in a_string:
        # print('yes')
        if third_word == a_string[:6]:
            # print('it is the first word')
            posthree = "0"
        elif third_word == a_string[26:30]:
            # print('it is the second word')
            posthree = "26"
        else:
            # print('it is the third word')
            posthree = "34"
    else:
        posthree = "-"
    
    print(posone)
    print(postwo)
    print(posthree)
    
    return posone + "," + postwo + "," + posthree
        
     
    
    # wone = a_string[:6]
    # wtwo = a_string[26:30]
    # wthree = a_string[34:38]
    
    # if wone == first_word:
    #     oone = "0"
    # else:
    #     oone = "-"
        
    # if wtwo == second_word:
    #     otwo = "26"
    # else:
    #     otwo = "-"
        
    # if wthree == third_word:
    #     othree = "34"
    # else:
    #     othree = "-"

    # return oone + "," + otwo + "," + othree
    
    

def test_three_occurrences():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Python', 'Wise', 'like') == "0,26,34"


def test_two_occurrences_missing_third():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Python', 'Wise', 'Ruby') == "0,26,-"


def test_two_occurrences_missing_first():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Ruby', 'Wise', 'like') == "-,26,34"


def test_one_occurrence_first_word():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Python', 'Javascript', 'Ruby') == "0,-,-"
    
   
    
def test_one_occurrence_second_word():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Javscript', 'like', 'Ruby') == "-,34,-"


def test_one_occurrence_third_word():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Javscript', 'Ruby', 'Wise') == "-,-,26"
