import unittest
import markov


class TestNGrams(unittest.TestCase):
    """
    Test n-grams function with various quotes and strings
    """

    def test_store_ngram(self):
        test_start = ('to', 'be')
        self.assertEqual(markov.store_ngram({}, test_start, 'or', True), {
            test_start: {'or': 1, 'total_suffixes': 1}
        })

    def test_n_gram_quote(self):
        self.maxDiff = None
        print(markov.n_gram('to be or not to be just be who you want to be or not ok you want okay', True))
        self.assertEqual(markov.n_gram(
            'to be or not to be just be who you want to be or not ok you want okay', True),  {
                ('to', 'be'): {'or': 2, 'just': 1, 'total_suffixes': 3},
                ('be',  'or'): {'not': 2, 'total_suffixes': 2 },
                ('or',  'not'): {'to': 1, 'ok': 1, 'total_suffixes': 2},
                ('not',  'to'): {'be': 1, 'total_suffixes': 1},
                ('be', 'just'): {'be': 1, 'total_suffixes': 1},
                ('just',  'be'): {'who': 1, 'total_suffixes': 1},
                ('be', 'who'): {'you': 1, 'total_suffixes': 1},
                ('who', 'you'): {'want': 1, 'total_suffixes': 1},
                ('you', 'want'): {'to': 1, 'okay': 1, 'total_suffixes': 2},
                ('want', 'to'): {'be': 1, 'total_suffixes': 1},
                ('not', 'ok'): {'you': 1, 'total_suffixes': 1},
                ('ok', 'you'): {'want': 1, 'total_suffixes': 1},
                ('want', 'okay'): {'_END_': 1, 'total_suffixes': 1},
        })

if __name__ == '__main__':
    unittest.main()
