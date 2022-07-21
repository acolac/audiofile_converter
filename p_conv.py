import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from moviepy.editor import *


class Converter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("455x200")
        self.title("Video_To_Audio_Converter")
        self.configure(bg="#c7bb81")
        
        convert_label = tk.Label(self, text="Convert to .mp3\n from .mp4/.avi/.wmv/.flv/.mov:",bg="#faefae", font="verdana 12")
        convert_label.pack()

        select_mp3 = tk.Button(self, text="Convert from .mp4", font="verdana 10", command=self.convert_from_mp4)
        select_mp3.pack()

        select_mpeg = tk.Button(self, text="Convert from .avi", font="verdana 10", command=self.convert_from_avi)
        select_mpeg.pack()

        select_mpeg = tk.Button(self, text="Convert from .wmv", font="verdana 10", command=self.convert_from_wmv)
        select_mpeg.pack()
        
        select_mpeg = tk.Button(self, text="Convert from .flv", font="verdana 10", command=self.convert_from_flv)
        select_mpeg.pack()

        select_mpeg = tk.Button(self, text="Convert from .mov", font="verdana 10", command=self.convert_from_mov)
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

    def convert_from_wmv(self):
        file = askopenfile(mode="r", filetypes=[('wmv file', '*.wmv')])
        wmv_file = file.name
        mp3_file = wmv_file.replace("wmv", "mp3")

        audioclip = AudioFileClip(wmv_file)
        audioclip.write_audiofile(mp3_file)
        audioclip.close() 

        showinfo(title="Done", message=".wmv file has been converted to .mp3 successfully\nCheck your directory")

    def convert_from_flv(self):
        file = askopenfile(mode="r", filetypes=[('flv file', '*.flv')])
        flv_file = file.name
        mp3_file = flv_file.replace("flv", "mp3")

        audioclip = AudioFileClip(flv_file)
        audioclip.write_audiofile(mp3_file)
        audioclip.close() 

        showinfo(title="Done", message=".flv file has been converted to .mp3 successfully\nCheck your directory")

    def convert_from_mov(self):
        file = askopenfile(mode="r", filetypes=[('mov file', '*.mov')])
        mov_file = file.name
        mp3_file = mov_file.replace("mov", "mp3")

        audioclip = AudioFileClip(mov_file)
        audioclip.write_audiofile(mp3_file)
        audioclip.close() 

        showinfo(title="Done", message=".mov file has been converted to .mp3 successfully\nCheck your directory")

convert = Converter()
convert.mainloop()
