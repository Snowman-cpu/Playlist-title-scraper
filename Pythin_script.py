import yt_dlp

playlist_url = "https://www.youtube.com/playlist?list=PLU6SqdYcYsfJPF-4HphQQ8OceDtqhlSW8"

ydl_opts = {
    'quiet': True,
    'extract_flat': True,  # Don't download, just get metadata
    'skip_download': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(playlist_url, download=False)
    print(f"Playlist title: {info.get('title')}\n")
    print("Video Titles:\n")
    for entry in info.get('entries', []):
        print(entry.get('title'))