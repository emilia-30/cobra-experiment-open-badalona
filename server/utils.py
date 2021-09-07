import os
import random

from config import REPEAT_STIMS_PER_SESSION_TIMES


def create_dir(dir_path):
    try:
        os.mkdir(dir_path)
    except OSError:
        print("Creation of the directory %s failed" % dir_path)
    else:
        print("Successfully created the directory %s " % dir_path)


def prepare_stims(stims):
    result = []

    for i in range(REPEAT_STIMS_PER_SESSION_TIMES):
        random.shuffle(stims)

        result = result + stims

    return result
