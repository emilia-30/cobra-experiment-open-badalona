import time
from datetime import datetime

from config import DURATIONS
from const import TRIAL_PHASES
from gui import gui
from utils import prepare_out


# path_to_audio_dir = "static/audio/"


def do_trial(trial, send):
    now = datetime.now()

    print(trial, now)

    gui.show_text('+')
    time.sleep(DURATIONS['DISPLAY_FIXATION_CROSS'])
    gui.remove_text()

    gui.show_image(trial["stim"])

    # this "callback" is used to notify the server to start recording as image has loaded and displayed
    if (trial['phase'] == TRIAL_PHASES['SPEAKER']):
        send(
            prepare_out(
                "prime and image shown"
            )
        )

    time.sleep(DURATIONS['DISPLAY_IMAGE_TIME'])
    gui.remove_image()
