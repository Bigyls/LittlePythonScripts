import os
from pathlib import Path
from pytube import YouTube
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Download Buttons
def download_mp4():
    Youtube_link = video_link.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.get_highest_resolution()
    videoStream.download(".")
    messagebox.showinfo("SUCCESSFULLY MP4", "DOWNLOADED\n")

def download_mp3():
    Youtube_link = video_link.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.filter(only_audio=True).first().download(".")
    base, ext = os.path.splitext(videoStream)
    new_file = base + '.mp3'
    os.rename(videoStream, new_file)
    messagebox.showinfo("SUCCESSFULLY MP3", "DOWNLOADED\n")

window = Tk()
window.geometry("862x209")
window.configure(bg = "#C4302B")

canvas = Canvas(
    window,
    bg = "#C4302B",
    height = 209,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    431.0,
    0.0,
    862.0,
    211.0,
    fill="#FCFCFC",
    outline="")

mp3_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
mp3 = Button(
    image=mp3_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=download_mp3,
    relief="flat"
)
mp3.place(
    x=441.0,
    y=129.0,
    width=180.0,
    height=55.0
)

mp4_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
mp4 = Button(
    image=mp4_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=download_mp4,
    relief="flat"
)
mp4.place(
    x=667.0,
    y=129.0,
    width=180.0,
    height=55.0
)

canvas.create_text(
    87.0,
    76.0,
    anchor="nw",
    text="Youtube Downloader",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    459.0,
    35.0,
    anchor="nw",
    text="Video link",
    fill="#505485",
    font=("Roboto Bold", 16 * -1)
)

canvas.create_rectangle(
    45.0,
    113.0,
    352.0,
    118.0,
    fill="#FCFCFC",
    outline="")

video_link_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
video_link_bg_1 = canvas.create_image(
    644.0,
    83.5,
    image=video_link_image_1
)
video_link = Entry(
    bd=0,
    bg="#F1F1F1",
    fg="#000716",
    highlightthickness=0
)
video_link.place(
    x=453.0,
    y=54.0,
    width=382.0,
    height=57.0
)

window.resizable(False, False)
window.title("Bigyls")
window.mainloop()