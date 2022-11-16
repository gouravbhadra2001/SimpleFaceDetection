import pyttsx3

#this function takes the string as input and makes AI voices pronounce the string.
def t2s(text):
    textspeech = pyttsx3.init()
    answer = text
    voices = textspeech.getProperty("voices")
    textspeech.setProperty("rate", 130)
    textspeech.setProperty("volume", 10)
    textspeech.setProperty("voice",  "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    textspeech.say(answer)
    textspeech.runAndWait()

