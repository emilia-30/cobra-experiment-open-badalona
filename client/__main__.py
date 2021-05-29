import json
import socket
import threading

from gui import gui
from trial import do_trial
from utils import prepare_out
from instrctions import *
from const import *


class Client():
    def __init__(self):
        self.s = socket.socket()

    def connect(self):
        try:
            self.s.connect((host, port))
            self.receive()
        except ConnectionRefusedError:
            gui.show_text("The server is not online.\n")

    def receive(self):
        while True:

            received = self.s.recv(1024)

            if not received:
                print('exiting')
                self.s.close()
                exit()
            if (received):
                response = json.loads(received.decode("utf-8"))

                print(response)

                message = response.get("message")

                if message:
                    if message == INSTRUCTIONS_PHASE['INTRODUCTION']:
                        gui.show_instructions_screen(self.on_spacebar_callback, INTRO_DETAILS, INTRO_HEADER)
                    elif message == INSTRUCTIONS_PHASE['BREAK']:
                        gui.show_instructions_screen(self.on_spacebar_callback, BREAK_DETAILS, BREAK_HEADER)
                    else:
                        gui.show_text(response.get("message"))

                if response.get("trial"):
                    do_trial(response.get("trial"), self.send)

    def send(self, data):
        try:
            self.s.send(data)

        except BrokenPipeError:
            self.s.close()

    def on_spacebar_callback(self):
        self.send(prepare_out('READY'))
        # remove instructions
        gui.clear_instructions()
        gui.show_text('waiting for the other participant')


c1 = Client()


def connect():
    gui.load_images()
    gui.connect_button.destroy()
    t1 = threading.Thread(target=c1.connect)
    t1.start()


if __name__ == "__main__":
    gui.connect_button.configure(command=connect)
    t0 = threading.Thread(target=gui.run)
    t0.run()
