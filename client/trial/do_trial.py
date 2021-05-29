from .run_speaker import run_speaker


def do_trial(trial, send):
    # phase = trial["phase"]

    run_speaker(trial["stim"], send)

    # if phase == TRIAL_PHASES["SPEAKER"]:
    #     run_speaker(stim, send)

    # elif phase == TRIAL_PHASES["LISTENER"]:
    #     run_listener(stim, send)
