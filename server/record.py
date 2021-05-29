SAMPLE_RATE = 44100

import pyaudio
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = 10  # DURATIONS['MAX_TRIAL_TIME_AFTER_STIM']


class record():
    def __init__(self, results_folder):
        self.results_folder = results_folder
        self.recording = False
        self.p = pyaudio.PyAudio()  # Create an interface to PortAudio

    def start(self, stim):
        self.recording = True

        self.ended_before_max_time = False
        print('Recording')

        self.stream = self.p.open(format=sample_format,
                                  channels=channels,
                                  rate=fs,
                                  frames_per_buffer=chunk,
                                  input=True)

        self.frames = []  # Initialize array to store frames

        while self.recording:
            # for i in range(0, int(fs / chunk * seconds)): # for time limit
            data = self.stream.read(chunk)
            self.frames.append(data)

        # Stop and close the stream

        self.stream.stop_stream()
        self.stream.close()
        # Terminate the PortAudio interface
        self.p.terminate()

        print('Finished recording')

        # Save the recorded data as a WAV file
        filename = self.results_folder + '/' + stim["prime"] + '_' + stim["stim"] + '.wav'
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(self.p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def stop(self):
        self.recording = False
