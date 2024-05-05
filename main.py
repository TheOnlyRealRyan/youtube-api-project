from pyyoutube import Client
from pytube import Playlist
from pytube import YouTube
import ffmpeg
import re
import os
import fnmatch 


def main():
    # playlists()
    combine_audio_and_video()
    # download_playlist()
    # download_video()
    
    
def combine_audio_and_video() -> None:
    """
    # TODO: this module finds the highest quality video track and audio track and combines them because pytube.get_highest_resolution() is broken
    """
    
    video_directory = "./video_track"
    filePattern = "*.*"
    #TODO: Ping pong between directories and combine tracks

    # Find Audio track
    audio_directory = "./audio_track"
    for path, dirs, files in os.walk(os.path.abspath(audio_directory)):
        for afilename in fnmatch.filter(files, filePattern):
            
            aud = afilename.strip("audio_")

            print(afilename)
            print(aud)

            # TODO: Compare stripped aud and vid and then combine the two if equal
            """
            if len(aud)> 0:
                input_audio = ffmpeg.input(f'./downloads/{afilename}')
                # print("-->" +  aud[0])
            
                # Find the matching video file
                for path, dirs, files in os.walk(os.path.abspath(video_directory)):
                    for vfilename in fnmatch.filter(files, filePattern):
                        # print(filename)
                        vid = re.findall('video_*', vfilename)
                        if len(vid)> 0:
                            input_video = ffmpeg.input(f'./downloads/{vfilename}')
                            # print(vid)
                    print(afilename)
                    print(vfilename)
                    if afilename == vfilename:
                        print("here")   
                        
            """
      
    """
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./processed_folder/finished_video.mp4').run()            
    """            
                
    """
    input_video = ffmpeg.input(re.findall('./downloads/video_(*).mp4'))

    input_audio = ffmpeg.input(re.findall('./downloads/audio_(*).(*))'))

    ffmpeg.concat(input_video, input_audio, v=1, a=1).output('./processed_folder/finished_video.mp4').run()
    """


def display_playlists() -> None:
    url = "https://www.youtube.com/playlist?list=PLmwmioLhtgmBc-ScvtbTXaWe27icfy4Kf"
    
    try: 
        playlist = Playlist(url) 
        print('Number of videos in playlist: %s' % len(playlist.video_urls))

        for urls in playlist.video_urls:
            print(f"url: {urls}")
            yt = YouTube(urls)
            print(yt.vid_info["videoDetails"]["title"]) 
            # print(yt.vid_info["videoDetails"])
    except Exception as e: 
        print(f"Error {str(e)}")
    

def download_playlist() -> None:
    video_path = "./video_track"
    audio_path = "./audio_track"
    # Download all videos in a playlist
    url = "https://www.youtube.com/playlist?list=PLmwmioLhtgmBc-ScvtbTXaWe27icfy4Kf"

    try:
        playlist = Playlist(url)
        print('Number of videos in playlist: %s' % len(playlist.video_urls))
        print(f'-->Downloading: {playlist.title}')
        # print(f'Downloading: {playlist.title}')
        for video in playlist.videos:
            # print(video.title)
            print(f"-->Downloading: {video.title}")
            # print(f"Resolution: {video.streams.get_highest_resolution()}")
            # video.streams.get_highest_resolution().download(path)
            
            
            print(f"Resolution: {video.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first()}")
            video.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first().download(filename_prefix="video_", output_path=video_path)
            video.streams.filter(only_audio=True, progressive=False).desc().first().download(filename_prefix="audio_", output_path=audio_path)

    except Exception as e: 
        print(f"Error {str(e)}")
    
        
def download_video() -> None:
    
    url = "https://www.youtube.com/watch?v=0hEmxOEeVO0"
    resolution = "720p"  #  "720p" "480p" "1080p"
    try: 
        yt = YouTube(url) 
        stream = yt.streams.filter(res=resolution).first() 
        print(yt.title)
        # stream.download() 
    except Exception as e: 
        print(f"Error {str(e)}")

    
if __name__ == "__main__":
    main()
