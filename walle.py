from vosk import Model , KaldiRecognizer
import  speech_recognition as sr
import pyttsx3 as pyt



# model = Model(r"vosk-ar")
# walle = KaldiRecognizer(model,16000)
engine = pyt.Engine()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

listener = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print(f"Listening .....")
            voice = listener.listen(source)
            listener.adjust_for_ambient_noise(source, .3)
            command = listener.recognize_ibm(voice)
            print(command)
    except sr.UnknownValueError as err:
         listener = sr.Recognizer()
         print(f"Somthing Went Wrong .....")