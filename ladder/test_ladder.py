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
        self.assertRaises(IndexError, self.stack.pop)
        self.stack.push(4)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.pop(), 4)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(3)
        self.stack.push(3)
        self.stack.pop()
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_pass_arr_to_const(self):
        stack = ladder.Stack([1, 2, 3])
        self.assertEqual(len(stack), 3)

    def test_copy_stack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.copy(), [1, 2, 3])


class TestLadder(unittest.TestCase):
    def setUp(self):
        self.ladder = ladder.Ladder(filename="../res/smalldict1.txt")

    def test_words_membership_in_dictionary(self):
        lad = ladder.Ladder(test_dict={"aa", "bb"})
        self.assertTrue(lad.both_words_in_dict("aa", "bb"))
        self.assertTrue(lad.word_in_dict("aa"))
        self.assertFalse(lad.both_words_in_dict("aa", "foo"))
        self.assertFalse(lad.word_in_dict("fdfd"))
        self.assertRaises(ValueError, lad.validate,
                          "fdfdasl", "dlafjkljfdsla")

    def test_find_ladder(self):
        self.assertEqual(self.ladder.find_ladder('code', 'data'), 5)
        self.assertRaisesRegex(
            ValueError, "Both words must be equal.", self.ladder.find_ladder, 'ghost', 'boo')
        self.assertRaises(ValueError, self.ladder.find_ladder,
                          '12345', 'eeeef')
        self.assertEqual(self.ladder.find_ladder('dog', 'cat'), 4)
        self.assertRaisesRegex(
            ValueError, "Words must be different.", self.ladder.find_ladder, 'dog', 'dog')

        biglad = ladder.Ladder(filename="../res/dictionary.txt")
        self.assertEqual(biglad.find_ladder('play', 'Work'), 7)


if __name__ == '__main__':
    unittest.main()
