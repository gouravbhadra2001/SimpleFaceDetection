
import from_live_webcam, from_saved_image, from_saved_video, TTS, success

webcam_success = [] 
saved_video_success = []
saved_image_success = []
def detection_process():
    inst = "\nEnter your choice number: \n1: Live Face Detection from webcam, \n2: Face Detection from saved image, \n3: Face Detection from saved video \nYour choice: "
    TTS.t2s(inst)
    choice = input(inst)
    if choice == "1":
        a = from_live_webcam.webcam_detect()
        if (a[0]!=0 and a[1]!=0): #when same no of faces are there in video for the whole.
            print("\n[Total Frames, Success]:")
            print(a)
            webcam_success.append(a)
            TTS.t2s("Detection Status  \n"+success.status_calc(webcam_success)["Detection Status"])
            print("Webcam Success:\n"+str(success.status_calc(webcam_success)))
        else:
            print("Ok")
    if choice == "2":
        d = from_saved_image.img_detect()
        saved_image_success.append(d)
        TTS.t2s("Detection Status  \n"+ success.succ_img(saved_image_success[-1])["Detection Status"])
        print("Webcam Success:\n"+str(success.succ_img(saved_image_success[-1])))
        
    if choice == "3":
        b = from_saved_video.vid_detect()
        if (b[0]!=0 and b[1]!=0): #when same no of faces are there in video for the whole.
            print("\n[Total Frames, Success]:")
            print(b)
            saved_video_success.append(b)
            TTS.t2s("Detection Status  \n"+success.status_calc(saved_video_success)["Detection Status"])
            print("Webcam Success:\n"+str(success.status_calc(saved_video_success)))
        else:
            print("Ok")
   

    

    


from playsound import playsound
playsound("Welcome.mp3", True) #Cortana welcomes the user

print("\nWelcome to Simple Face Detection")
repp = "\nHow much times you want to test the Face Detection process?\n"
TTS.t2s(repp)
rep = int(input(repp))

for i in range(1,rep+1):
    tc = "\nTest Case "+ str(i) + ":\n"
    TTS.t2s(tc)
    print(tc)
    detection_process()


thanks = "\nThank you for using Simple Face Detection\n"

playsound("thanks.mp3", True) #Cortana says thanks to the user

print(thanks)




