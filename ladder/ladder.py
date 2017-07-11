"""
    cli tool to determine distance between two words of equal length and verifies
    that the words exist in the user-provided dictionary.
    I understand that the hamming distance provides the minimum substitutions to change from word a
    to word b but this implementation uses BFS as a learning exercise in pythong.

    Usage:
    python ladder.py -d/--dict <dictfile> <word1> <word2>  

    find_distance(word1, word2) can be exported to be use in other modules
"""
import argparse
import math
from collections import deque

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", help="runs unittests", action="store_true")
parser.add_argument("-d", "--dict", help="line separated list of words")
parser.add_argument("w1", help="first word")
parser.add_argument("w2", help="second word")


class Stack:
    """
    I know we can use the list as a stack but this is for learning!
    Dynamically sized stack.
    Doubles array if not enough room in stack.
    Halves the array if stack is too large.
    """

    def __init__(self):
        self.__array = []
        self.__len = len(self.__array)
        self.__last_index = -1
        self.__size = 0

    def resize(self, capacity):
        copy = [None] * capacity
        for i in range(self.__len):
            copy[i] = self.__array[i]
        self.__array = copy
        self.__size = capacity

    def push(self, value):
        self.__last_index += 1
        if self.__last_index == 0:
            self.__array = [value]

        if self.__last_index >= self.__len and self.__len >= 1:
            # double the size of the array
            new_size = self.__len
            self.resize(new_size * 2)
            self.__array[self.__last_index] = value

        self.__len += 1

    def pop(self):
        # halve the array if array is too large
        if self.__last_index < 0:
            raise IndexError("Can't pop from an empty stack")

        if self.__last_index <= math.floor(self.__len / 4):
            # halve the size
            self.resize(math.ceil(self.__len / 2))

        val = self.__array[self.__last_index]
        self.__last_index -= 1
        self.__len -= 1
        return val

    def __str__(self):
        for e in self.__array:
            print("{0}\n".format(e))

    def __len__(self):
        return self.__len

    def size(self):
        # actual size of internal container
        return self.__size


class Ladder:
    def __init__(self, filename="", test_dict=None):
        self.filename = filename
        self.__dictionary = None

        if test_dict and isinstance(test_dict, set):
            self.__dictionary = test_dict
        else:
            with open(filename) as f:
                self.__dictionary = {line.strip() for line in f}

    def word_in_dict(self, word):
        return word in self.__dictionary

    def both_words_in_dict(self, word1, word2):
        return self.word_in_dict(word1) and self.word_in_dict(word2)

    def find_ladder(self, word1, word2):
        """
        BFS implementation. 
        Find all valid neighbors between word1 and word2 by examining every 
        permutation of words from the word at the top of the first stack in the queue. 

        """
        if self.both_words_in_dict(word1, word2):
            # create a queue of word ladder stack
            stack = [word1]
            queue = deque([stack])
            seen = set(stack)
            while len(queue) > 0:
                stack = queue.popleft()
                # examine neighbors from the current word at the top of the stack
                curr_word = stack.pop()
            # if the neighbor not seen and neighbor is word2


if __name__ == '__main__':
    args = parser.parse_args()
    if not args.dict:
        raise ValueError("No dictionary file provided")
    else:
        if len(args.w1) != len(args.w2):
            raise ValueError("Words must be of the same length")
        ladder = Ladder(filename=args.dict)
