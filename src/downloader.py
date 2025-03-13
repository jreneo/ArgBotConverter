from pytubefix import YouTube
from pytubefix.cli import on_progress

def download(url : str,location : str):
    print("Download function:")
    try:
        yt = YouTube(
            url,
            on_progress_callback=on_progress
        )
        print(yt.title)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=location)
        print("Downloading...")
        
        print("Download complete!")

    except Exception as e:
        print(f"An error occured: {e}")
        
