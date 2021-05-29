import os
import random

from const import USE_ALL_STIMS_PER_SESSION_COUNT


def create_dir(dir_path):
    try:
        os.mkdir(dir_path)
    except OSError:
        print("Creation of the directory %s failed" % dir_path)
    else:
        print("Successfully created the directory %s " % dir_path)


def prepare_stims(stims, prime_types):
    result = []

    for i in range(USE_ALL_STIMS_PER_SESSION_COUNT):
        stims_with_primes = []
        for s in stims:
            for t in prime_types:
                stims_with_primes.append({
                    "stim": s,
                    "prime": t
                })

        random.shuffle(stims_with_primes)

        result = result + stims_with_primes

    return result
