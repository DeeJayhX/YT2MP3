from threading import Thread
import pytube as pt
import sys
import os
import tempfile
import base64
import subprocess
import ffmpeg_encoded

##Using FFMPEG by the FFmpeg team.
##Purpose in this project: Convert mp4 files to mp3 audio.
##Website: https://www.ffmpeg.org/
##Build: ffmpeg-20190211-6174686-win64-static
##Source code available from the official repositories: https://www.ffmpeg.org/download.html#repositories
##I am using FFmpeg unmodified and so no source changes have been made.
##If you are an FFmpeg developer/team member/etc and I have not properly accredited your work, please advise
##me how to correct it and I will be happy to oblige.

#Instantiate variables
downloadList = []
convertList = []
threads = []

#check if ran with arguments

#if first argument is present, use it as directory instead of current directory
try:
    dir = sys.argv[1]
except IndexError:
    dir = os.getcwd()

#make sure directory is valid by checking if it exists
if not os.path.isdir(dir):
    print("Directory provided is invalid. Defaulting to current working directory.")
    dir = os.getcwd()



def Download_mp4(url,downloadList):
    print("[{0} of {1}] {2} Downloading...".format(downloadList.index(url)+1,downloadList.index(max(url)),url))
    pt.YouTube(url).streams.first().download()
    print("[{0} of {1}] {2} Complete.".format(downloadList.index(url)+1,downloadList.index(max(url)),url))

def Convert_mp3(file, path):
    newfile = file.split(".")[0] + ".mp3"
    result = subprocess.call([path, "-i", file, newfile])
    os.remove(os.getcwd() + "\\" + file)

def start_threads(threads):
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

while True:
    video = input("Paste a youtube link and hit enter, or leave blank to begin converting:\n")
    if video != "":
        downloadList.append(video)
        print("Added {0} to list of videos to download.".format(video))
    else:
        print("Finished adding videos to be downloaded.")
        break

for url in downloadList:
    thread = Thread(target = Download_mp4, args = (url,downloadList))
    threads.append(thread)

start_threads(threads)

print("Converting MP4s in directory: {0}".format(dir))

threads = []

##Unpack ffmpeg
print("Unpacking ffmpeg.")
fd, path = tempfile.mkstemp(suffix='.exe')
code = base64.b64decode(ffmpeg_encoded.encoded)
os.write(fd, code)
os.close(fd)
print("Unpack Complete")

for file in os.listdir(dir):
    if file.endswith(".mp4"):
        print("Queueing file {0} for conversion.".format(file))
        thread = Thread(target = Convert_mp3, args = (file, path))
        threads.append(thread)
   
start_threads(threads)

os.remove(path)

print("Finished.")