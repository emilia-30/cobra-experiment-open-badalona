from const import PRIME_TYPES

Stim = {
    "stim": str,  # path to image file
    "prime": PRIME_TYPES,  # prime type
}

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
