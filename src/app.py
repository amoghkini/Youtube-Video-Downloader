from pytube import YouTube

youtube_video_link = "https://www.youtube.com/watch?v=LXb3EKWsInQ"

def on_download_process(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percentage = bytes_downloaded * 100 / stream.filesize
    
    print(f"Downloading...{int(percentage)}")
    
youtube_video = YouTube(youtube_video_link)

youtube_video.register_on_progress_callback(on_download_process)
print("Title: ", youtube_video.title)
print("No of views: ", youtube_video.views)
print("Description: ", youtube_video.description)

stream = youtube_video.streams.get_highest_resolution()
print("Loading...")

stream.download()
print("Ok")

