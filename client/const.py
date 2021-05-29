host = "192.168.0.1"
port = 1233

db_path = "results_db"

DISPLAY_IMAGE_SIZE = 450

PRIME_TYPES = {
    "predictable": "predictable",
    "unpredictable": "unpredictable",
    "beep": "beep",
}


TRIAL_PHASES = {
    "SPEAKER": "SPEAKER",
    "LISTENER": "LISTENER",
}

INSTRUCTIONS_PHASE = {
    "INTRODUCTION": "INTRODUCTION",
    "BREAK": "BREAK"
}

DURATIONS = {
    # pauses
    "PAUSE_BEFORE_PRIME": 0,
    "PAUSE_BEFORE_IMAGE": 0,

    # displays
    "DISPLAY_IMAGE_TIME": 3,
}
