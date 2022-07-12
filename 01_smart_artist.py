# concept: Regular Expressions
'''
User regular expressions 
to find out the occurances of the words 
in the given text.

Reference to understand:
https://towardsdatascience.com/regular-expressions-in-python-a212b1c73d7f
'''
import re

import unittest


def count_word_occurances(sentense, word):
    """ 
    Return the number of occurances of the given word in string s.
    The matches must not be substring of another word.

    e.g:
    input: 
    sentense = "Smart is not art. Art is not smart. Only Art is Art."
    word = 'Art'

    output:
    count = 3

    The 'Art' matches exactly 3 words in the sentense.

    Note:
    In regular expressions, when you pass patterns like these be carefull
    r'\b' is equal to '\\b'
    r"\b" is equal to "\\b"
    So when you are constructing the pattern, make note of the above.
    """
    count = 0
    # write you implementation here
    l=[]
    x=re.sub('\W',' ',sentense)
    y=re.split(' ',x)
    for i in y:
        s=re.findall('^'+word,i)
        if s:
            l.append(s)
    count=len(l)

    return count


def word_occurances_ignore_case(sentense, word):
    """ 
    Return the number of occurances of the given word in string s.
    Ignoring the case.
    The matches must not be substring of another word.

    e.g:
    input: 
    sentense = "Smart is not art. Art is not smart. Only Art is Art."
    word = 'ART'

    output:
    all_words = ['art', 'Art', 'Art', 'Art']

    """
    all_words = []
    # write you implementation here

    return all_words

class Smart_artist(unittest.TestCase):
    def smart_string(self):
        return "Smart is not art. Art is not smart. Only Art is Art. Smart must not match for art. So this string about art contains 7 complete art words."

    def test_smart(self):
        smart_count = count_word_occurances(self.smart_string(), 'smart')
        self.assertEqual(smart_count, 1)    
        capital_smart_count = count_word_occurances(self.smart_string(), 'Smart')
        self.assertEqual(capital_smart_count, 2)
        smart_words = word_occurances_ignore_case(self.smart_string(), 'smart')
        self.assertEqual(smart_words, ['Smart', 'smart', 'Smart'])
        smart_words = word_occurances_ignore_case(self.smart_string(), 'Smart')
        self.assertEqual(smart_words, ['Smart', 'smart', 'Smart'])


    def test_art(self):
        art_count = count_word_occurances(self.smart_string(), 'art')
        self.assertEqual(art_count, 4)    
        capital_art_count = count_word_occurances(self.smart_string(), 'Art')
        self.assertEqual(capital_art_count, 3)
        art_words = word_occurances_ignore_case(self.smart_string(), 'art')
        self.assertEqual(art_words, ['art', 'Art', 'Art', 'Art', 'art', 'art', 'art'])
        art_words = word_occurances_ignore_case(self.smart_string(), 'ART')
        self.assertEqual(art_words, ['art', 'Art', 'Art', 'Art', 'art', 'art', 'art'])

    def test_artist(self):
        software_artifact = """
Art is practiced by artist. 
Artist create different artworks.
Software developer is a smart artist,
who create software artifacts."""
        art_words = word_occurances_ignore_case(software_artifact, 'art')
        self.assertEqual(art_words, ['Art'])
        artist_words = word_occurances_ignore_case(software_artifact, 'artist')
        self.assertEqual(artist_words, ['artist', 'Artist', 'artist'])
        artist_words = word_occurances_ignore_case(software_artifact, 'ARTist')
        self.assertEqual(artist_words, ['artist', 'Artist', 'artist'])



if __name__ == '__main__':
  unittest.main(verbosity=2)




