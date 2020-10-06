"""
Intro to python exercises shell code
"""

def is_odd(x):
    
    if ((x % 2) == 1) :
        return True
    else :
        return False
    

def is_palindrome(word):
    
    if (word == word[::-1]) :
        return True
    else :
        return False


def only_odds(numlist):
    
    odds_list = []
    
    for i in range(0, len(numlist)):
        if numList[i] % 2 == 1:
            odds_list.append(numList[i])
            
    return odds_list


def count_words(text):
    
    text.lower()
    
    word_count = dict()
    
    sentence_words = text.split()
    
    for word in sentence_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
      
    
    return word_count
    
    