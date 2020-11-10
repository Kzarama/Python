from __future__ import unicode_literals
import youtube_dl
import os
'''from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog as fd'''


class Download(object):
    def __init__(self, url):
        self.url = url
        self.save_path = os.path.join(os.path.expanduser('-'), 'Downloads')
        self.song()

    def song(self):
        opts = {
            'verbose': False,
            'fixup': 'detect_or_warn',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '1411'
            }],
            'extractaudio': True,
            'outtmpl': self.save_path + '/%(title)s.%(ext)s',
            'noplaylist': True
        }
        ydl = youtube_dl.YoutubeDL(opts)
        ydl.download([self.url])


if __name__ == "__main__":
    url = input('Enter url to song here\n >>')
    Download(url)
