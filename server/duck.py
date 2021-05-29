from const import *

InputMethod = {"SPEECH": "SPEECH", "SPACEBAR": "SPACEBAR", "TEXT": "TEXT"}

Stim = {
    "key": str,  # stim key and path to image file
    "prime": str,  # path to sound file
    "prime_type": str,  # prime type, unused on client
}

TrialStart = {"phase": TRIAL_PHASES, "stim": Stim}

ServerOut = {
    "message": str,  # maybe no use - maybe to send instructions
    "expected_input_method": str,  # what should client prompt
    "stim": Stim,
}

ServerIn = {
    "participant": int,
    "response": str,
    "response_time": int,  # measure on client to exclude transfer time
    "stim": Stim,  # store trial data
}
