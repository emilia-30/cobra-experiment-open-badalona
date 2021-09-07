from const import *

TrialStart = {"phase": TRIAL_PHASES, "stim": str}

ServerOut = {
    "message": str,  # maybe no use - maybe to send instructions
    "expected_input_method": str,  # what should client prompt
    "stim": str,
}

ServerIn = {
    "participant": int,
    "response": str,
    "response_time": int,  # measure on client to exclude transfer time
    "stim": str,  # store trial data
}
