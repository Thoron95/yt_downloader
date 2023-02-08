'''
A simple script which downloads a video from YouTube using `pytube` library.
It also can download just a audio from a video.
Files are saved in .mp4 format
'''

import argparse
from pytube import YouTube
import os

#Taking care of flags
parser = argparse.ArgumentParser(description='Download YouTube video from a specified link.')
parser.add_argument('link', metavar='link',
                    help='a link to youtube video')
args = parser.parse_args()

#Creating an instance of YouTube with link provided
yt = YouTube(args.link)

print(f'{yt.author} - {yt.title}')


while True:
    print('Do you want to download a file as audio-only?\n')
    mode = input('<<<yes/no>>>')
    check_yes = mode.lower() == 'y' or mode.lower() == 'yes'
    check_no = mode.lower() == 'n' or mode.lower() == 'no'
    if check_yes or check_no:
        break
    else:
        print('Unrecognized answer. Lets try that again.\n' )

current_directory = os.getcwd()
if check_yes:
    #Download audio-only if check_yes == True
    save_directory = os.path.join(current_directory, 'YT_audio')
    yd = yt.streams.get_audio_only()
    yd.download(save_directory)
    print(f'An audio only file has been saved to: {save_directory}')
elif check_no:
    #Else download whole video
    save_directory = os.path.join(current_directory, 'YT_video')
    yd = yt.streams.get_highest_resolution()
    yd.download(save_directory)
    print(f'A video file has been saved to: {save_directory}')