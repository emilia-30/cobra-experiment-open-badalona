host = "192.168.0.1"
port = 1233

db_path = "results_db"

COUNTDOWN_START = 3
COUNTDOWN_END = 0

EXPERIMENT_BREAK_POINTS = [27, 54, 81]

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
    "MAX_TRIAL_TIME_AFTER_STIM": 8,

    # pauses
    "PAUSE_BEFORE_PRIME": 1,
    "PAUSE_BEFORE_IMAGE": 1,
    "PAUSE_BEFORE_PROMPTING_SPEAKER": 2,
    "PAUSE_BEFORE_PROMPTING_LISTENER": 2,
    "PAUSE_BETWEEN_TRIALS": 2,
    "PAUSE_AFTER_BREAK": 1,

    # displays
    "DISPLAY_IMAGE": 5,
}
