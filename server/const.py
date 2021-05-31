# host = "127.0.0.1"
host = "192.168.0.1"
port = 1233

db_path = "results_db"

EXPERIMENT_BREAK_POINTS = [27, 54, 81]

USE_ALL_STIMS_PER_SESSION_COUNT = 2

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
    "PRACTICE_COMPLETE": "PRACTICE_COMPLETE",
    "BREAK": "BREAK"
}

DURATIONS = {
    "MAX_TRIAL_TIME_AFTER_STIM": 8,

    # pauses
    "PAUSE_AFTER_BREAK": 1,
}