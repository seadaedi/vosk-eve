from vosk import Model , KaldiRecognizer

import pyttsx3
import pyaudio
# from mytools import Analyze
import ast
engine = pyttsx3.Engine()

bufferSize = 16000

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

model = Model(r'D:\\Apps\\Python\\Vosk-2\\vosk-en')

walle =  KaldiRecognizer(model,bufferSize)

cap = pyaudio.PyAudio()

stream  = cap.open(format=pyaudio.paInt16 , channels=1 , rate=bufferSize , input=True , frames_per_buffer= 8192)
i=0
stream.start_stream()
print('Listening....... ')
while True :
    data = stream.read(2048,False)
    if walle.AcceptWaveform(data):
        text = walle.Result()
        text = ast.literal_eval(text)["text"]
        print(text)
        # print(Analyze(text))

        # engine.say(text)
        # engine.runAndWait()