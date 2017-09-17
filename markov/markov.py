# All of the necessary classes and functions for creating an n-gram, processing text
# and generating our markov text
import redis


BEGIN = '_BEGIN_'
END = '_END_'


def tokenize(quote):
    # split quote into a list of runs (sentences)
    return


def store_ngram(storage, prefix, suffix, debug=False):
    # takes a tuple start and the next state,
    # stores start and next state as child of that start along with frequency of next state
    # NOTE: I really don't like mutating the 'storage' state like this. might want to refactor to a class
    if not(prefix or suffix):
        raise Exception('Start or next_state are required!')

    if not storage and type(storage) is not dict:
        raise Exception('Storage required!')

    if debug and type(storage) is dict:
        # if we're in debug mode, storage is a passed dict
        if prefix not in storage:
            storage[prefix] = {}

        if suffix not in storage[prefix]:
            storage[prefix][suffix] = 0

        storage[prefix][suffix] += 1
        return storage


def n_gram(run, n, debug=False):
    # take a string quote and produce an n-gram
    assert type(run) is str, 'quote is not a string %s' % run
    assert type(n) is int, 'n is not an integer %d' % n
    items = run.split(' ')
    storage = {} if debug else redis.StrictRedis(
        host='localhost', port=6379, db=0)

    for i in range(len(items) + 1):
        start = tuple(items[i:i + (n - 1)])
        print(start)
        # store_ngram(storage, start, next_state, debug)

    if debug:
        return storage
