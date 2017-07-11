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
import string
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

    def __init__(self, arr=None):
        self.__array = []
        if arr:
            self.__array = arr
        self.__len = len(self.__array)
        self.__last_index = self.__len - 1
        self.__size = self.__len

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
        if self.is_empty():
            raise IndexError("Can't pop from an empty stack")

        if self.__last_index <= math.floor(self.__len / 4):
            # halve the size
            self.resize(math.ceil(self.__len / 2))

        val = self.__array[self.__last_index]
        self.__last_index -= 1
        self.__len -= 1
        return val

    def __str__(self):
        return ' -> '.join([str(e) for e in self.__array if e != None])

    def __len__(self):
        return self.__len

    def size(self):
        # actual size of internal container
        return self.__size

    def is_empty(self):
        return self.__len == 0

    def copy(self):
        return [e for e in self.__array if e != None]


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

    def validate(self, word1, word2):
        if not self.both_words_in_dict(word1, word2):
            raise ValueError("Neither words were found in the dictionary!")

        if not self.word_in_dict(word1):
            raise ValueError("Word1 not in dictionary.")

        if not self.word_in_dict(word2):
            raise ValueError("Word2 not in dictionary!")

        if len(word1) != len(word2):
            raise ValueError("Both words must be equal.")

        if word1 == word2:
            raise ValueError("Words must be different.")

    def find_ladder(self, word1, word2):
        """
        BFS implementation. 
        Find all valid neighbors between word1 and word2 by examining every 
        permutation of words from the word at the top of the first stack in the queue. 
        Returns the shortest path if the path is found or -1.
        """
        self.validate(
            word1, word2)  # check that these words are actually in dict
        if self.both_words_in_dict(word1, word2):
            # create a queue of word ladder stack
            stack = Stack([word1])
            queue = deque([stack])
            seen = set([word1])
            while len(queue) > 0:
                stack = queue.popleft()
                # examine neighbors from the current word at the top of the stack
                curr_word = stack.pop()
                for i, c in enumerate(curr_word):
                    for s in string.printable:
                        neighbor = curr_word[0:i] + s + \
                            curr_word[i + 1::]
                        if self.word_in_dict(neighbor) and neighbor not in seen:
                            # if the neighbor not seen and neighbor is word2
                            if neighbor == word2:
                                print("ladder from {0} to {1} is: ".format(
                                    word2, word1))
                                # account for the current popped word and first word, hence 2
                                l = len(stack) + 2
                                print("{0}, {1}".format(
                                    word2, curr_word), end="")
                                while not stack.is_empty():
                                    print(
                                        ", {0}".format(stack.pop()), end="")
                                print("\nlength: ", l)
                                return l
                            else:
                                copy = Stack(stack.copy())
                                # add this neighbor to the stack's copy
                                copy.push(neighbor)
                                seen.add(neighbor)
                                queue.appendleft(copy)
            return -1


if __name__ == '__main__':
    args = parser.parse_args()
    if not args.dict:
        raise ValueError("No dictionary file provided")
    else:
        if len(args.w1) != len(args.w2):
            raise ValueError("Words must be of the same length")
        ladder = Ladder(filename=args.dict)
        print(ladder.find_ladder(args.w1, args.w2))
