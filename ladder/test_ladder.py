import unittest
import ladder


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = ladder.Stack()

    def test_push(self):
        # self.assertEqual(len(stack), 0)
        self.stack.push(1)
        # self.assertEqual(len(stack), 1)
        self.stack.push(32)
        self.stack.push(3)
        self.stack.push(33)
        self.assertEqual(len(self.stack), 4)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(3)
        self.stack.push(8)
        self.assertEqual(self.stack.pop(), 8)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 1)
        self.assertRaises(IndexError, self.stack.pop())


class TestLadder(unittest.TestCase):
    def test_words_membership_in_dictionary(self):
        lad = ladder.Ladder(test_dict={"aa", "bb"})
        self.assertTrue(lad.both_words_in_dict("aa", "bb"))
        self.assertTrue(lad.word_in_dict("aa"))
        self.assertFalse(lad.both_words_in_dict("aa", "foo"))
        self.assertFalse(lad.word_in_dict("fdfd"))


if __name__ == '__main__':
    unittest.main()
