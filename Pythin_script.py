import yt_dlp

playlist_url = input("Enter your playlist url: \n")

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