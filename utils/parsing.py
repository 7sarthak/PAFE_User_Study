import yt_dlp

def get_best_url(path):
    ydl_opts = {
        "format": "best[ext=mp4]/best",
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(path, download=False)

        formats = info.get("formats", [])

        for f in reversed(formats):
            if f.get("url"):
                return f["url"]

        return info.get("url")
