import yt_dlp

class VideoDownloader:
    def __init__(self, url):
        self.url = url
        self.ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }

    def fetch_video_info(self):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info_dict = ydl.extract_info(self.url, download=False)
                video_title = info_dict.get('title', None)
                return video_title
        except Exception as e:
            raise Exception(f"Error fetching video info: {e}")

    def download(self, save_path='.'):
        self.ydl_opts['outtmpl'] = save_path + '/%(title)s.%(ext)s'
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([self.url])
                info_dict = ydl.extract_info(self.url, download=False)
                file_name = ydl.prepare_filename(info_dict)
                return file_name
        except Exception as e:
            raise Exception(f"Error downloading video: {e}")
