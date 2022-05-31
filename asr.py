from pickle import TRUE
from typing_extensions import Self
from vosk import Model, KaldiRecognizer

import pyttsx3
import pyaudio
import ast
from pattern.text.en import parse, Sentence

import os


def Analyze(txt):
    parsed = parse(txt)
    result = Sentence(parsed)
    cmd = ""
    for ch in result.chunk:
        cmd += ch.string+" "

    return cmd


def clear():
    def clean(): return os.system('cls')
    clean()


def GetText(text_dic):
    return ast.literal_eval(text_dic)["text"]


engine = pyttsx3.Engine()

bufferSize = 16000

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

model = Model(r'D:\\Apps\\Python\\Vosk-2\\vosk-en')

walle = KaldiRecognizer(model, bufferSize)

cap = pyaudio.PyAudio()

stream = cap.open(format=pyaudio.paInt16, channels=1,
                  rate=bufferSize, input=True, frames_per_buffer=8192)
stream.start_stream()





def StandBy(stand_by = True) :
    print("On Stand By.......")
    on_standby = stand_by
    while on_standby:
        data = stream.read(2048, False)
        if walle.AcceptWaveform(data):
            text = walle.Result()
            text: str = GetText(text)
            if len(text) > 0 :
                if "eve" in text :
                    on_standby = False
                    wake()

def wake():
    
    on_wake = True
    
    print('Hi Am Listening....... ')
    while on_wake :
        data = stream.read(2048, False)
        if walle.AcceptWaveform(data):
            text = walle.Result()
            text: str = GetText(text)
            print(text)
            on_wake = False
            StandBy(True)
            
            
            



clear()
StandBy()

