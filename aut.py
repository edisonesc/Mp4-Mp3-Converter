import subprocess
import glob
import os

path = "/media/edison/STORAGE/Files/Music/"
songs = glob.glob(path + "*.mp4")
name = "/media/edison/STORAGE/Files/Music/Juice\ WRLD\ –\ Lucid\ Dreams.mp4"
# subprocess.call("cd venv", shell=True)
# subprocess.call("cd media/edison/STORAGE/Files/Screen\ Record")
# subprocess.call("pwd", cwd="/media/edison/STORAGE/Files/")
# subprocess.call("pwd", cwd="/media/edison/STORAGE/Files/Screen Record")
# subprocess.call("ffmpeg -i "+ name +" -f mp3 -vn exported/gu.mp3", cwd="/media/edison/STORAGE/Files/Music", shell=True)
# subprocess.call("ls", cwd="/media/edison/STORAGE/Files/Music", shell=True)
# print (songs[1])
# print(songs)


for e in songs:
    # newStr = e.replace(path, "")
    song_name = e.replace(path, "").replace(" ", "")
    newStr = e.replace(" ", "\ ")
    chars = set('()')
    if any((c in chars) for c in newStr):
        print(song_name + " " + "was found.")
        os.chdir(path)

        print(song_name)
        os.rename(e.replace(path, ""), song_name.replace("(", "").replace(")", ""))

    subprocess.call("ffmpeg -i " + newStr + " -f mp3 -vn exported/"+ song_name +".mp3", cwd="/media/edison/STORAGE/Files/Music", shell=True)
    print(songs.index(e))

