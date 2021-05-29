import os
import random


def create_dir(dir_path):
    try:
        os.mkdir(dir_path)
    except OSError:
        print("Creation of the directory %s failed" % dir_path)
    else:
        print("Successfully created the directory %s " % dir_path)

def prepare_stims(stims, prime_types):
    result = []
    for s in stims:
        for t in prime_types:
            result.append({
                "stim": s,
                "prime": t
            })

    random.shuffle(result)

    return result
