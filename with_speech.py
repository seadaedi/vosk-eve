from numpy import rec
import speech_recognition as sr
from vosk import Model , KaldiRecognizer

reco = sr.Recognizer()
audio_file = sr.AudioFile(r"D:\\Apps\\Python\\Vosk-2\\test.wav")
while True :
    try :
        print("Listening....")
        with sr.Microphone() as source : 
            audio_file =reco.record(source)
            print("Done")
    except sr.UnknownValueError as err :
          reco = sr.Recognizer()
          print('Somthing is Wrong Looping')
         
