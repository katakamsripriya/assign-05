'''
User regular expressions 
to find out the occurances of the words 
typed by a stuttering keyboard.

Reference to understand:
https://towardsdatascience.com/regular-expressions-in-python-a212b1c73d7f
'''

import re
import unittest

def stuttering_words(text, word):
    """ 
    Return the number of occurances of the given word in string s.
    Where the starting character of the word must have been typed many number of times.
    """
    special_words = []
    # Write your implementation here

    return special_words

class Stuttering_words(unittest.TestCase):
    def test_code(self):
        text = "ccccccode code cede ccode ode"
        code_words = stuttering_words(text, 'code')
        self.assertEqual(code_words, ['ccccccode', 'code', 'ccode'])

        text = "code is cccode written in file where ccccccode iiiis pppresent jjjust as code"
        code_words = stuttering_words(text, 'code')
        self.assertEqual(code_words, ['code', 'cccode', 'ccccccode', 'code'])

    def test_oops(self):
        text = "OOOOOPs is OOObjected OOOOriented PPPPProgramming. OOOOPs, OOOPs, OOPs"
        oops_words = stuttering_words(text, 'OOPs')
        self.assertEqual(oops_words, ['OOOOOPs', 'OOOOPs', 'OOOPs', 'OOPs'])
        

    def test_ooh(self):
        text = "oooh tttthis kkkkkeyboard iiis dddddifficult tttto ttttype, ooooh, oooh, ooh"
        ooh_words = stuttering_words(text, 'ooh')
        self.assertEqual(ooh_words, ['oooh', 'ooooh', 'oooh', 'ooh'])

if __name__ == '__main__':
  unittest.main(verbosity=2)