from pytube import YouTube 
x=input("Enter the URL of the video to be downloaded: ")
print("")
print("Downloading..........")
x="'"+x+"'"
yt=YouTube(x)
print("")
print(yt.title)
yt.streams.first().download()
print("")
print("Download Successful !!")
