from tkinter import filedialog
import cv2 as cv
import colors, TTS


def img_detect():
    count = 0
    path = filedialog.askopenfilename()
    #des = "C:\Users\hp\OneDrive\Documents\Python\College_Project\FaceDetection"
    #file_name = os.path.basename(path)
    #shutil.copy2(path.replace("\ \b", "/"), des.replace("\ \b", "/"))
    img = cv.imread(path.replace("\ \b", "/"))
    bw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    humanfaces = cv.CascadeClassifier("haarcascade_frontalface_default.xml").detectMultiScale(
    bw,1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv.CASCADE_SCALE_IMAGE
)
    for (x, y, w, h) in humanfaces:
        count = count + 1 #no of detected face is being counted
        cv.rectangle(img, (x, y), (x+w, y+h), colors.color1(), 2)
        cv.putText(img, 'Human Face Detected', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, colors.color2(), 2)
    cv.imshow('Face_Detection', img)
    if cv.waitKey(0) & 0xFF == ord('q'):
        cv.destroyAllWindows()

    print("No. of faces in selected image: "+ str(count))
    act = "Enter the actual number of the faces in the selected image"
    TTS.t2s(act)
    f = int(input(act+": "))
    return ((f-count)/f)*100 #percentage failure is returned

