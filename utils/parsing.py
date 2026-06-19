from urlvalidator import URLValidator, ValidationError
import yt_dlp

def get_best_url(path):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(path, download=False)
        # Return the direct streaming URL
        return info.get('url')
