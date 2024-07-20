from tkinter import *  #graphics
# GRAPHICS needed:
# window for downloading speed and internet speed
# button

import speedtest #speedtest module to check the internet speed

def bytes_to_mb(bytes):
    KB = 1024 # One Kilobyte is 1024 bytes
    MB = KB * 1024 # One MB is 1024 KB
    return str(int(bytes/MB))

def speedcheck():
    sp = speedtest.Speedtest()
    #get servers speed
    sp.get_servers()
    
    #downloading and uploading speed in bytes converted to mb
    downloading = bytes_to_mb(sp.download())+" Mb"
    uploading = bytes_to_mb(sp.upload())+" Mb"

    lab_down.config(text = downloading) #take values from download funs in speedtest here stored in download
    lab_up.config(text = uploading)# take value from upload func in speedtest here stored in upload
    
sp = Tk() # variable to call tkinker class
sp.title(" Internet Speed Test ") #title of page
sp.geometry("500x550") #dimensions of window
sp.config(bg="black")

# name/label
lab = Label(sp,text = "Internet Speed Test ", font=("Times New Roman", 30,"bold"),bg ="black" ,fg="White")
lab.place(x=70, y=40,height = 50, width=360)

# downloading speed
lab = Label(sp,text = "Downloading speed ", font=("Times New Roman", 30,"bold"))
lab.place(x=70, y=130,height = 50, width=360)

lab_down = Label(sp,text = "00", font=("Times New Roman", 30,"bold"))
lab_down.place(x=70, y=200,height = 50, width=360)

# uploading speed
lab = Label(sp,text = "Uploading speed ", font=("Times New Roman", 30,"bold"))
lab.place(x=70, y=290,height = 50, width=360)

lab_up = Label(sp,text = "00", font=("Times New Roman", 30,"bold"))
lab_up.place(x=70, y=360,height = 50, width=360)

#button for GUI
button = Button(sp, text = "Check speed",font=("Times New Roman", 30,"bold"), relief=RAISED, bg = "green",command=speedcheck)
button.place(x=70, y=460,height = 50, width=360)


sp.mainloop() #window













    # downloading = str(round(sp.download()/(10**6),3))+" Mbps"
    # uploading = str(round(sp.upload()/(10**6),3))+" Mbps"























# import speedtest

# speed_test = speedtest.Speedtest()

# def bytes_to_mb(bytes):
#   KB = 1024 # One Kilobyte is 1024 bytes
#   MB = KB * 1024 # One MB is 1024 KB
#   return int(bytes/MB)

# download_speed = bytes_to_mb(speed_test.download())
# print("Your Download speed is", download_speed, "MB") 

# upload_speed = bytes_to_mb(speed_test.upload())
# print("Your Upload speed is", upload_speed)