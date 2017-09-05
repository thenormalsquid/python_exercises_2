# All of the necessary classes and functions for creating an n-gram, processing text
# and generating our markov text
import redis


BEGIN = '_BEGIN_'
END = '_END_'


def store_ngram(storage, start, next_state, debug=False):
    # takes a tuple start and the next state,
    # stores start and next state as child of that start along with frequency of next state
    # NOTE: I really don't like mutating the 'storage' state like this. might want to refactor to a class
    if not(start or next_state):
        raise Exception('Start or next_state are required!')

    if not storage:
        raise Exception('Storage required!')

    if debug and type(storage) is dict:
        # if we're in debug mode, storage is a passed dict
        if start not in storage:
            storage[start] = {}

        if next_state not in storage[start]:
            storage[start][next_state] = 0

        storage[start][next_state] += 1
        return storage


def n_gram(quote, n, debug=False):
    # take a string quote and produce an n-gram
    assert type(quote) is str, 'quote is not a string %s' % quote
    assert type(n) is int, 'n is not an integer %d' % n
    items = quote.split(' ')
    storage = {} if debug else redis.StrictRedis(
        host='localhost', port=6379, db=0)

    for i in range(len(items) - 1):
        start = tuple(items[i:i + (n - 1)])
        print(start)
        # store_ngram(storage, start, next_state, debug)

    if debug:
        return storage
