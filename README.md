# YT2MP3
## Windows 7 or Newer, 64-bit only
## Does not currently support 32-bit, linux, mac, or any other OS
Automatically downloads and converts YouTube videos to MP3 format.
No malware, no nonsense, just a clean and simple, open-source client.

### Usage

By using YT2MP3 you accept the LICENSE and FFMPEG_LICENSE included with YT2MP3

#### Releases

- Extract the executable into the folder you want your MP3s to end up in.
- Run the executable, which will start up and ask you to enter a youtube link.

   Note that at this point you can paste as many YouTube links as you like,
   one at a time followed by pressing enter, and the program will build a list
   of Youtube Videos you wish to download and convert. When you have entered
   the last one you desire, simply press enter again to put in a blank entry.

   - YouTube URLs must be complete, https://www.youtube.com/watch?v=rxGtJBOtmHI
   is such an example.

- Once you submit a blank entry, YT2MP3 will utilize the maximum number of
threads possible to download each of the videos as quickly as possible. As you
might expect, the more videos in your list, the more your bandwidth will have to
be split among these threads. It might be obvious, but more videos will take more
time to complete.

- Once the videos are finished downloading, YT2MP3 will temporarily extract and
utilize FFmpeg to convert any .mp4 files in the directory to .mp3 and then delete
the .mp4 copies once the .mp3 is finished.

   **Note that this will happen to ALL MP4s IN THE DIRECTORY** so you can also use
   YT2MP3 as a simple converter to turn .mp4 files into .mp3 files. This is thanks
   to the magic that FFmpeg brings to the table. This is a double edge sword, so
   do NOT run YT2MP3 in a directory with .mp4 files you do not wish to lose.

#### Running From Source

- You will require:
   - YT2MP3.py
   - ffmpeg_encoded.py
   - Python 3.7.2

- Run the YT2MP3.py with python, which will ask you to enter a youtube link.

   Note that at this point you can paste as many YouTube links as you like,
   one at a time followed by pressing enter, and the program will build a list
   of Youtube Videos you wish to download and convert. When you have entered
   the last one you desire, simply press enter again to put in a blank entry.

   - YouTube URLs must be complete, https://www.youtube.com/watch?v=rxGtJBOtmHI
   is such an example.

- Once you submit a blank entry, YT2MP3 will utilize the maximum number of
threads possible to download each of the videos as quickly as possible. As you
might expect, the more videos in your list, the more your bandwidth will have to
be split among these threads. It might be obvious, but more videos will take more
time to complete.

- Once the videos are finished downloading, YT2MP3 will temporarily extract and
utilize FFmpeg to convert any .mp4 files in the directory to .mp3 and then delete
the .mp4 copies once the .mp3 is finished.

   **Note that this will happen to ALL MP4s IN THE DIRECTORY** so you can also use
   YT2MP3 as a simple converter to turn .mp4 files into .mp3 files. This is thanks
   to the magic that FFmpeg brings to the table. This is a double edge sword, so
   do NOT run YT2MP3 in a directory with .mp4 files you do not wish to lose.

## Piracy Warning

You may only use YT2MP3 to download and convert videos to which you have the rights.
It is a violation of copyright laws to download and keep a copy of audio for which
you do not possess the rights. I do not condone such acts and using this software
for that purpose is expressly prohibited.