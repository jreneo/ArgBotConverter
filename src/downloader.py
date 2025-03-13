from pytubefix import YouTube
from pytubefix.cli import on_progress

def download(url : str) -> bool:
    print("Download function:")
    try:
        yt = YouTube(
            url,
            on_progress_callback=on_progress
        )
        print(yt.title)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Downloading...")
        
        print("Download complete!")

    except Exception as e:
        print(f"An error occured: {e}")
        
