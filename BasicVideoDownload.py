# BasicVideoDownload.py
from pytube import YouTube


def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download("X:\\Programming\\Python\\Downloads")
    finally:
        print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
download(link)

exit()
