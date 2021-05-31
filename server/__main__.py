import json
import socket
import threading
import time
from datetime import datetime

from db import create_connection, get_all, get_save_to_db
from duck import *
from results_audio import Results_audio
from results_csv import Results_csv
from stims import STIM_KEYS, PRACTICE_STIMS
# from detect_speech_offset import detect_speech_offset
from utils import create_dir, prepare_stims

ServerSocket = socket.socket()
clientsCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print("Waiting for a Connection..")

ServerSocket.listen(1)


def prepareOut(data: ServerOut):
    return str.encode(json.dumps(data))


def send_message_to_both(message: str):
    data = prepareOut({"message": message})

    partOne.send(data)
    partTwo.send(data)


def end_experiment():
    print('ending')
    time.sleep(1)
    send_message_to_both("complete")


def run_experiment():
    print('START server experiment set up')

    prepared_stims = prepare_stims(STIM_KEYS, PRIME_TYPES)

    db = create_connection(db_path)
    db_cursor = db.get("cursor")
    save_to_db = get_save_to_db(db_cursor)

    save_results_name = datetime.now().strftime("%b %d %Y %H:%M:%S")

    results_audio_folder = "results/audio/" + save_results_name

    create_dir(results_audio_folder)

    csv = Results_csv(save_results_name)

    print('END server experiment set up')

    print('START practice')
    for index, practice_stim in enumerate(PRACTICE_STIMS):
        speaker, listener = (
            (partTwo, partOne) if index % 2 == 0 else (partOne, partTwo)
        )

        speaker.send(
            prepareOut(
                {
                    "trial": {"phase": TRIAL_PHASES["SPEAKER"], "stim": practice_stim},
                }
            )
        )
        # blocks till speaker prime and image shown
        json.loads(speaker.recv(2048).decode("utf-8"))

        time.sleep(DURATIONS['MAX_TRIAL_TIME_AFTER_STIM'])

    print('END practice')

    instructions_and_confirm(INSTRUCTIONS_PHASE['PRACTICE_COMPLETE'])

    def do_trial(trial_index):

        stim = prepared_stims[trial_index - 1]

        speaker, listener = (
            (partTwo, partOne) if trial_index % 2 == 0 else (partOne, partTwo)
        )

        speaker.send(
            prepareOut(
                {
                    "trial": {"phase": TRIAL_PHASES["SPEAKER"], "stim": stim},
                }
            )
        )

        # record object should be initiated some seconds before we actually start recording as there is som e noise for first ~1 second
        audio_recording = Results_audio(results_audio_folder)

        recording_thread = threading.Thread(target=audio_recording.start, args=[stim])

        # blocks till speaker prime and image shown
        json.loads(speaker.recv(2048).decode("utf-8"))

        recording_thread.start()

        # todo get response times running detect in thread
        # detect_speech_offset()

        time.sleep(DURATIONS['MAX_TRIAL_TIME_AFTER_STIM'])

        audio_recording.stop()

        trial_results = {
            "prime": stim["prime"],
            "stim": stim["stim"],
        }

        save_to_db(trial_results)
        csv.add_entry(trial_results, trial_index)

        if trial_index < len(prepared_stims):
            if EXPERIMENT_BREAK_POINTS.__contains__(trial_index):
                instructions_and_confirm(INSTRUCTIONS_PHASE['BREAK'])

            do_trial(trial_index + 1)
        else:
            end = db.get("finish")
            get_all(db_cursor)
            end()
            end_experiment()
            exit()

    print('START trials')

    do_trial(1)


def instructions_and_confirm(phase: INSTRUCTIONS_PHASE):
    part_one_ready = False
    part_two_ready = False

    while not (part_two_ready and part_one_ready):
        print('asking for confirm: ' + phase)

        send_message_to_both(phase)

        one_confirm_response = json.loads(partOne.recv(2048).decode("utf-8"))
        print('one_confirm_response')
        two_confirm_response = json.loads(partTwo.recv(2048).decode("utf-8"))

        print('two_confirm_response')

        part_one_ready = one_confirm_response == "READY"
        part_two_ready = two_confirm_response == "READY"

        # hack clears both screens
        send_message_to_both(' ')
        time.sleep(DURATIONS['PAUSE_AFTER_BREAK'])


while True:
    Client, address = ServerSocket.accept()
    clientsCount += 1

    if clientsCount == 1:
        partOne = Client

        Client.send(
            prepareOut(
                {
                    "message": "Hello!\nwaiting for second participant\n...",
                }
            )
        )

    if clientsCount == 2:
        partTwo = Client

        instructions_and_confirm(INSTRUCTIONS_PHASE['INTRODUCTION'])

        run_experiment()
        send_message_to_both('complete')
        # ServerSocket.shutdown(0)
        ServerSocket.close()

    if clientsCount > 2:
        Client.send(
            prepareOut({"message": "connection refused - max number reached"})
        )
        Client.close()
