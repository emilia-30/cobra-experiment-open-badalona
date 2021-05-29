import speech_recognition as sr

r = sr.Recognizer()
# these parameters should match in recording function or can cause an os error

m = sr.Microphone(sample_rate=44100, chunk_size=1024, device_index=0, )
sr.Microphone.list_microphone_names()

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


r.energy_threshold = 400
r.pause_threshold = 0.1
# r.phrase_threshold = 0.1
r.non_speaking_duration = 0.1


def detect_speech_offset(speech_offset_callback=lambda: print('speech event complete'), expected_speech_events=2):
    speech_events = 0

    # r.listen_in_background(m, cb)

    with m as source:
        # adjust_for_ambient_noise can be used if needed but will introduce a delay before speech detection
        # r.adjust_for_ambient_noise(source)

        while speech_events < expected_speech_events:
            print('listening')
            a = r.listen(source)

            print(len(a.frame_data) / a.sample_rate / a.sample_width)

            speech_events += 1
        speech_offset_callback()

# detect_speech_offset(expected_speech_events=10)
