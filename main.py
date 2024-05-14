from pyyoutube import Client
from pytube import Playlist
from pytube import YouTube
import ffmpeg
import re
import os
import fnmatch 
import pathlib
import subprocess    

def combine_audio_and_video(video_path: str, audio_path: str, output_path: str):
    """
    This funciton combines the highest quality video track 
    and audio track and combines them because 
    pytube.get_highest_resolution() is broken

    Args:
        video_path (str): path to video file
        audio_path (str): path to audio file
        output_path (str): _description_
    """
    ffmpeg_path = 'C:/ffmpeg/bin/ffmpeg.exe' # Your path to ffmpeg here
    try:
        # Construct the ffmpeg command
        command = [
            ffmpeg_path,
            '-i', video_path,  # Input video file
            '-i', audio_path,  # Input audio file
            '-c:v', 'copy',    # Copy the video codec
            '-c:a', 'libvorbis',     # Use libvorbis codec for mpeg files
            # '-strict', 'experimental',  # Allow experimental AAC codec
            output_path  # Output file path
        ]
        
        # Run the command
        subprocess.run(command, check=True)
        print(f'Successfully combined video and audio into {output_path}')
    except subprocess.CalledProcessError as e:
        print(f'Error occurred: {e}')


def navigate_folders(video_directory: str, vfilePattern: str,afilePattern: str) -> str:
    """_summary_

    Args:
        video_directory (str): _description_
        vfilePattern (str): _description_
        afilePattern (str): _description_

    Returns:
        str: _description_
    """

    for path, dirs, files in os.walk(os.path.abspath(video_directory)):
        for filename in fnmatch.filter(files, vfilePattern): 
            for apath, adirs, afiles in os.walk(os.path.abspath(video_directory)):
                for afilename in fnmatch.filter(afiles, afilePattern): 
                    # print(afilename)
                    # print(files, afiles)
                    # print("-------"+ filename.strip("video_*.mp4",))
                    if filename.strip("video_*.mp4") == afilename.strip("audio_*.webm"):
                        
                        # print("------------", filename, afilename)
                        yield filename, afilename
                    else:
                        yield 0

    
def combine_audio_and_video() -> None:
    """
    # TODO: 
    """
    video_directory = "./video_track"
    filePattern = "*.*"
    
    # video_directory_path = "./video_track"
    # video_directory = pathlib.PureWindowsPath(video_directory_path).as_posix()
    
    for path, dirs, files in os.walk(os.path.abspath(video_directory)):
        for filename in fnmatch.filter(files, filePattern):
            for apath, adirs, afiles in os.walk(os.path.abspath(video_directory)):
                for afilename in fnmatch.filter(afiles, filePattern):         
                    
                    print(f"first: {filename}")
                    print(f"Second: {afilename}")
                    
                    aud = afilename.strip("audio_")
                    aud2 = aud.strip(".webm")
                    
                    vid = filename.strip("video_")
                    vid2 = vid.strip(".mp4")

                    # TODO: Compare stripped aud and vid and then combine the two if equal
                    if aud2 == vid2:
                        print(f"Compare: {aud2} - {vid2}")
                        print(f"File: {afilename} - {filename}")
                        print((f'./audio_track/{afilename}'))
                        
                        input_video = ffmpeg.input(f'./video_track/{afilename}')
                        input_audio = ffmpeg.input(f'./video_track/{filename}')
                        
                        # print(filename, afilename)
                        # subprocess.run(f"ffmpeg -i ./video_track/{filename} -i ./video_track/{afilename} -c:v copy -c:a aac {vid2}.mp4")
                        print(f'\"./processed_folder/{filename}\"')
                        ffmpeg.concat(input_video, input_audio, v=1, a=1).output(f'\"./processed_folder/{filename}\"').run()

    """
    # Combining Audio and Video Code
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
            
            # print(f"Resolution: {video.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first()}")
            print("-->Downloading Video Track...")
            video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename_prefix="video_", output_path=video_path)
            print("-->Downloading Audio Track...")
            video.streams.filter(only_audio=True, progressive=False).desc().first().download(filename_prefix="audio_", output_path=video_path)

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


def main():
    
    # Combine Audio and Video
    video_directory = "./video_track"
    vfilePattern = "*.mp4"
    afilePattern = "*.webm" 
    for value in navigate_folders(video_directory,vfilePattern, afilePattern):
        if value != 0:
            print(f"---> Combining Tracks: {value[0]} - {value[1]}")
            path1 = f"video_track/{value[0]}"
            path2 = f"video_track/{value[1]}"
            output_path = f"processed_folder/{value[0].strip("video_")}"
            combine_audio_and_video(path1, path2, output_path)
    
    # Display Video Titles in a Playlist
    # display_playlists()
    
    # Download Video and Audio Tracks Seperataly from a playlist
    # download_playlist()
    
    # Download an individual video using a link 
    # download_video()  
    
    
if __name__ == "__main__":
    main()
