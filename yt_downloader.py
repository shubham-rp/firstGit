from pytube import YouTube 
x=input("Enter the URL of the video to be downloaded: ")
print("")
print("Downloading..........")
x="'"+x+"'"
yt=YouTube(x)
print("")
print(yt.title)
some_video=yt.streams.first()


some_video.download()
print("")
print("Download Successful !!")

#successfully gitted