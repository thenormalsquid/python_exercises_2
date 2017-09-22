# All of the necessary classes and functions for creating an n-gram, processing text
# and generating our markov text
import redis


BEGIN = '_BEGIN_'
END = '_END_'
N = 3 # start with a 3 gram. This needs to be > 1

def store_ngram(storage, prefix, suffix, debug=False):
    # takes a tuple start and the next state,
    # stores stat and next state as child of that start along with frequency of next state
    # NOTE: I really don't like mutating the 'storage' state like this. might want to refactor to a class
    if not(prefix or suffix):
        raise Exception('Start or next_state are required!')

    if debug and type(storage) is dict:
        # if we're in debug mode, storage is a passed dict
        if prefix not in storage:
            storage[prefix] = {}
            storage[prefix]['total_suffixes'] = 0

        if suffix not in storage[prefix]:
            storage[prefix][suffix] = 0

        storage[prefix][suffix] += 1
        storage[prefix]['total_suffixes'] += 1
        return storage


def n_gram(run, debug=False):
    # take a string quote and produce an n-gram
    assert type(run) is str, 'quote is not a string %s' % run
    assert run is not '', 'Cannot process empty quote'
    items = run.split(' ')
    assert len(items) > N, 'Cannot process strings less than size N'

    storage = {} if debug else redis.StrictRedis(
        host='localhost', port=6379, db=0)

    items.insert(0, BEGIN) # add our begin and stop to our quote source
    # TODO: add this end to the end of every sentence inside the quote
    items.append(END)

    for i in range(len(items) - 1):
        right_idx = i + N - 1
        prefix = tuple(items[i:right_idx])
        suffix = items[right_idx] 
        store_ngram(storage, prefix, suffix, True)
        if items[right_idx] == END:
            break

    if debug:
        return storage

# TODO; integrate markov generator with bot

def text_generate():
    pass

def random_selection():
    pass