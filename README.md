# yt_downloader
 
 A simple script that download a video from YouTube.
 
 It requires "pytube" library which you can get by using:
 `pip install pytube`
 
 It takes a link to a youtube video as argument. The link must be provided in quotation marks.
 The script can download a whole video or just its audio track. In both cases the file will be saved in ".mp4" format.
 For clarity sake the video files are saved in "YT_video" folder where audio files are saved in "YT_audio" folder.
 
 An example of use:
 `python yt_downloader.py "https://www.youtube.com/watch?v=cE0wfjsybIQ&ab_channel=Noisestorm"`
 Short links also works:
 `python yt_downloader.py "https://youtu.be/cE0wfjsybIQ"
 
 And yes, both link I used are for the Crab Rave. You are welcome :)