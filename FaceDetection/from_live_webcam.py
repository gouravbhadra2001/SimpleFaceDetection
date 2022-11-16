import os, winsound, colors, TTS
import cv2 as cv


def webcam_detect():
    count1 = 0
    count2 = 0
    
    click_video = cv.VideoCapture(0)
    while True:
        count1 = count1 + 1 #counting the total number of frames while camera is on
        count3 = 0
        ret, frames = click_video.read()    #reads the frames
        bw = cv.cvtColor(frames, cv.COLOR_BGR2GRAY) #frames are converted into grey mode
        humanfaces = cv.CascadeClassifier("haarcascade_frontalface_default.xml").detectMultiScale(
        bw,1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )
    # haarcascade_frontalface_default.xml is fed to CascadeClassifier 
        for (x, y, w, h) in humanfaces: #for each detection with rectangle
            count2 = count2 + 1 
            count3 = count3 + 1 #total number of faces detected
            cv.rectangle(frames, (x, y), (x+w, y+h), colors.color1(), 2)
            cv.putText(frames, 'Human Face Detected', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, colors.color2(), 2)
            winsound.Beep(2500, 100) #beep sound is excerted for each detection.

        cv.imshow('Showing Live Webcam Video and Face Detection', frames) #the live video is shown.
        print("No of face detected: "+str(count3))
        if (count3==0): print("Immediate Status: Failure") #status of face detection per frame.
        if (count3>0):print("Immediate Status: Success")
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break               #on pressing 'q' from keyboard, the camera is shut down
    click_video.release()
    cv.destroyAllWindows()
    TTS.t2s("Does the video contain similar number of faces all the time?") #Test-To-Speech
    ask = input("\nDoes the video contain similar number of faces all the time?(y/n/don't know): ")
    if (ask == "y" or ask == "Y"):
        TTS.t2s("Enter the actual number of faces in front of webcam")
        face_count = int(input("\nEnter the actual number of faces in front of webcam: "))
        f = count1 #total no of frames
        s = int(count2/face_count) # total no. of units, each unit being all the actual face count 
        return [f,s]

    if (ask=="n"or ask=="N" or "don't know"):
        return [0,0]
    
