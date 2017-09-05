import unittest
import markov


class TestNGrams(unittest.TestCase):
    """
    Test n-grams function with various quotes and strings
    """

    def test_store_ngram(self):
        test_start = ('to', 'be')
        self.assertEqual(markov.store_ngram({}, test_start, 'or', True), {
            test_start: {'or': 1}
        })

    def test_n_gram_quote(self):
        self.assertEqual(markov.n_gram(
            'to be or not to be just be who you want to be or not ok you want okay', 3, True),  {
                ('to', 'be'): {'or': 2, 'just': 1},
                ('be',  'or'): {'not': 1},
                ('or',  'not'): {'to': 1, 'okay': 1},
                ('not',  'to'): {'be': 1},
                ('be', 'just'): {'be': 1},
                ('just',  'be'): {'who': 1},
                ('be', 'who'): {'you': 1},
                ('who', 'you'): {'want': 1},
                ('you', 'want'): {'to': 1, 'okay': 1},
                ('want', 'to'): {'be': 1},
                ('not', 'okay'): {'you': 1},
                ('okay', 'you'): {'want': 1},
                ('want', 'okay'): {'to': 1},
                ('okay', 'to'): {'be': 1}
        })


if __name__ == '__main__':
    unittest.main()
