import time

from const import DURATIONS
from duck import Stim
from utils import prepare_out


# from trial.duck import DURATIONS, Stim


# def run_listener(stim: Stim, send):
#     time.sleep(DURATIONS["PAUSE_BEFORE_PROMPTING_LISTENER"])

    # start = time.time()
    # time.sleep(1.3)
    #
    # response = "listener says something"
    #
    # response_time = time.time() - start
    #
    # send(
    #     prepare_out(
    #         {
    #             "response_time": response_time,
    #             "response": response,
    #             "stim": stim,
    #         }
    #     )
    # )
