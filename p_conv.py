import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from moviepy.editor import *


class Converter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("455x100")
        self.title("MP4_To_MP3_Converter")
        self.configure(bg="#c7bb81")
        convert_label = tk.Label(self, text="Convert to .mp3 from .mp4/.avi:",bg="#faefae", font="verdana 12")
        convert_label.pack()

        select_mp3 = tk.Button(self, text="Convert from .mp4", font="verdana 10", command=self.convert_from_mp4)
        select_mp3.pack()

        select_mpeg = tk.Button(self, text="Convert from .avi", font="verdana 10", command=self.convert_from_avi)
        select_mpeg.pack()

    def convert_from_mp4(self):
        file = askopenfile(mode="r", filetypes=[('mp4 file', '*.mp4')])
        mp4_file = file.name
        mp3_file = mp4_file.replace("mp4", "mp3")

        audioclip = AudioFileClip(mp4_file)
        audioclip.write_audiofile(mp3_file)
        audioclip.close() 

        showinfo(title="Done", message=".mp4 file has been converted to .mp3 successfully\nCheck your directory")

    def convert_from_avi(self):
        file = askopenfile(mode="r", filetypes=[('avi file', '*.avi')])
        avi_file = file.name
        mp3_file = avi_file.replace("avi", "mp3")

        audioclip = AudioFileClip(avi_file)
        audioclip.write_audiofile(mp3_file)
        audioclip.close() 

        showinfo(title="Done", message=".avi file has been converted to .mp3 successfully\nCheck your directory")

convert = Converter()
convert.mainloop()