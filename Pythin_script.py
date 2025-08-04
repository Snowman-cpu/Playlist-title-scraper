import yt_dlp

a = ("Enter your playlist url: \n")
playlist_url = a # You don't need to manually change the url in the now 

ydl_opts = {
    'quiet': True,
    'extract_flat': True,  # Don't download, just get metadata
    'skip_download': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(playlist_url, download=False)
    print(f"Playlist title: {info.get('title')}\n")
    print("Video Titles:\n")
    for i, entry in enumerate(info.get('entries', []),start =1):
        print(f"{i}.{entry.get('title')}")
        
         
         
import yt_dlp

a = input("Enter your url: \n")
playlist_url = a

ydl_ops = {
    'quiet' : True,
    'extract_flat': True,
    'skip_download':True,
}

with yt_dlp.YoutubeDL(ydl_ops) as ydl:
    info = ydl.extract_info(playlist_url,download = False)
    print(f"Playlist Titles: {info.get('title')}\n")
    print(f"Video Titles \n")
    
    for i,entry in enumerate(info.get('entries',[]),start=1):
        print(f"{i}.{entry.get('title')}")