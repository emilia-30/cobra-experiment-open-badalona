import os
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from config import DISPLAY_IMAGE_SIZE

path_to_images_dir = "static/images/"


class Gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # setup screen

        self.title('')
        ## fullscreeen
        self.overrideredirect(True)
        self.overrideredirect(False)
        self.attributes('-fullscreen', True, )
        self.configure(bg='black')

        # dimensions used to set image size
        self.dimensions = {"w": self.winfo_screenwidth(), "h": self.winfo_screenheight()}

        # ESC key closes client
        self.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))

        # # setup widgets
        ## label widget used to display messages
        self.label = tk.Label(self, text="", font=("Arial", 22), background='black', foreground="white")
        self.label.place(relx=0.5,
                         rely=0.5,
                         anchor='center')

        self.instructions_header = tk.Label()
        self.instructions_details = tk.Label()

        self.connect_button = ttk.Button(self, text='Connect')
        self.connect_button.place(relx=0.5,
                                  rely=0.5,
                                  anchor='center')

    def remove_image(self):
        # hack: forgetting and re-placing stops occasional empty squares appearing, and non-determinate image removal time
        self.label.place_forget()
        self.label.config(image='')
        self.label.place(relx=0.5,
                         rely=0.5,
                         anchor='center')

    def remove_text(self):
        self.label['text'] = ''

    def show_text(self, text):
        self.remove_image()
        self.label['text'] = text

    def show_image(self, image_path):
        self.remove_text()

        path = image_path + ".jpg"

        self.label.config(image=self.loaded_images[path])
        self.label.image = self.loaded_images[path]

    def bind_key_listener(self, callback):
        def handle_keypress(event):
            if event.char == ' ':
                callback()
                self.unbind("<Key>", binding_id)

        binding_id = self.bind("<Key>", handle_keypress)

    def clear_instructions(self):
        self.instructions_header.grid_forget()
        self.instructions_details.grid_forget()

    def show_instructions_screen(self, callback, details, header_text=''):
        self.instructions_header = tk.Label(self, text=header_text, font=("Arial", 24), background='black',
                                            foreground="white",
                                            justify='center',
                                            )

        self.instructions_header.grid(row=2, column=0, pady=(70, 10))

        ## label widget used to display messages
        self.instructions_details = tk.Label(self, text=details, font=("Arial", 22), background='black',
                                             foreground="white",
                                             wraplength=(self.winfo_width() - 200), justify='left',
                                             )

        self.instructions_details.grid(row=4, column=0, padx=(100, 100), pady=(50, 100))

        self.bind_key_listener(callback)

    def run(self):
        self.mainloop()

    def load_images(self):
        images = os.listdir(path_to_images_dir)
        self.loaded_images = {}

        for i in images:
            pilImage = Image.open(path_to_images_dir + i)

            imgWidth, imgHeight = pilImage.size

            if imgWidth > DISPLAY_IMAGE_SIZE or imgHeight > DISPLAY_IMAGE_SIZE:
                ratio = min(DISPLAY_IMAGE_SIZE / imgWidth, DISPLAY_IMAGE_SIZE / imgHeight)

                imgWidth = int(imgWidth * ratio)
                imgHeight = int(imgHeight * ratio)
                pilImage = pilImage.resize((imgWidth, imgHeight), Image.ANTIALIAS)

            self.loaded_images[i] = ImageTk.PhotoImage(pilImage)


gui = Gui()
