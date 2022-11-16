import colors, winsound, TTS
from tkinter import filedialog
import cv2 as cv

def vid_detect():
    count1 = 0
    count2 = 0
    path = filedialog.askopenfilename()
    click_video = cv.VideoCapture(path.replace("\ \b", "/"))
    if click_video.isOpened()==False:
        print("Error opening the video file")
    
    while (click_video.isOpened()):
        count1 = count1 + 1 #counting the total number of frames while the video file is opened
        count3 = 0
        ret, frame = click_video.read() #reads the frames
        # haarcascade_frontalface_default.xml is fed to CascadeClassifier
        humanfaces = cv.CascadeClassifier("haarcascade_frontalface_default.xml").detectMultiScale(
        frame,1.2,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )
        for (x, y, w, h) in humanfaces:
            count2 = count2 + 1
            count3 = count3 + 1
            cv.rectangle(frame, (x, y), (x+w, y+h), colors.color1(), 2)
            winsound.Beep(2500,100)
            cv.putText(frame, 'Human Face Detected', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, colors.color2(), 2)
        if ret == True:
            cv.imshow('Showing the video and detecting face', frame) #the recorded video is shown.
            print("No of faces detected: "+str(count3))
            if (count3==0): print("Immediate Status: Failure")
            if (count3>0):print("Immediate Status: Success")
            if cv.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    click_video.release()
    cv.destroyAllWindows()

    TTS.t2s("Does the video contain similar number of faces all the time?")
    ask = input("\nDoes the video contain similar number of faces all the time?(y/n/don't know): ")
    if (ask == "y" or ask == "Y"):
        TTS.t2s("Enter the actual number of faces in the video")
        face_count = int(input("\nEnter the actual number of faces in the video: "))
        f = count1
        s = int(count2/face_count)
        return [f,s]

    if (ask=="n"or ask=="N" or "don't know"):
        return [0,0]
    
    


