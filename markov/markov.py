# All of the necessary classes and functions for creating an n-gram, processing text
# and generating our markov text
import redis
import random

BEGIN = '_BEGIN_'
END = '_END_'
N = 3 # start with a 3 gram. This needs to be > 1

class Markov:
    def __init__(self, storage, debug=False):
        # TODO: implement redis as non-debug storage
        self.storage = storage
        self.debug = debug

    def store_ngram(self, prefix, suffix):
         """
         takes a tuple start and the next state,
         stores stat and next state as child of that start along with frequency of next state
         NOTE: I really don't like mutating the 'storage' state like this. might want to refactor to a class
         """
        if not(prefix or suffix):
            raise Exception('Start or next_state are required!')

            # if we're in debug mode, storage is a passed dict
        if prefix not in self.storage:
            self.storage[prefix] = {}
            self.storage[prefix]['total_suffixes'] = 0

        if suffix not in self.storage[prefix]:
            self.storage[prefix][suffix] = 0

            self.storage[prefix][suffix] += 1
            self.storage[prefix]['total_suffixes'] += 1


    def generate_n_gram(self, run):
        # take a string quote and produce an n-gram
        assert type(run) is str, 'quote is not a string %s' % run
        assert run is not '', 'Cannot process empty quote'
        items = run.split(' ')
        assert len(items) > N, 'Cannot process strings less than size N'

        length = len(items)
        for i in range(length - 1):
            right_idx = i + N - 1
            prefix = tuple(items[i:right_idx])

            # we cycle back to the beginning of the quote if the last index overflows
            # this helps prevents prematurely ending the markov stream
            suffix = items[right_idx % length] 
            self.store_ngram(prefix, suffix, True)

        if debug return self.storage

    def get_seed(self):
        if debug:
            starts = self.storage.keys()
            return random.choice(starts)

    def get_storage(self):
        # returns redis client or dict
        pass