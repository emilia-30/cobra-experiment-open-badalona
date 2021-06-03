import wave
import pyaudio

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second


class Results_audio():
    def __init__(self, results_folder):
        self.results_folder = results_folder
        self.recording = False
        self.p = pyaudio.PyAudio()  # Create an interface to PortAudio

    def start(self, stim, trial_index):
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
            data = self.stream.read(chunk)
            self.frames.append(data)

        # Stop and close the stream

        self.stream.stop_stream()
        self.stream.close()
        # Terminate the PortAudio interface
        self.p.terminate()

        print('Finished recording')

        # Save the recorded data as a WAV file
        filename = self.results_folder + '/' + stim["prime"] + '_' + stim["stim"] + '_' + str(trial_index) + '.wav'
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(self.p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def stop(self):
        self.recording = False
