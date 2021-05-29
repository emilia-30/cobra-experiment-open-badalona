from .run_speaker import run_speaker


def do_trial(trial, send):
    run_speaker(trial["stim"], send)
