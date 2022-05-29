from vosk import Model, KaldiRecognizer
import pyaudio
from mytools import Analyze
import ast

model = Model(r'D:\\Apps\\Python\\Vosk-2\\vosk-en')

walle = KaldiRecognizer(model, 16000)

cap = pyaudio.PyAudio()

stream = cap.open(format=pyaudio.paInt32, channels=1, rate=16000, input=True, frames_per_buffer=8000)

stream.start_stream()
print('Listening....... ')
sentence = ""
while True:
    data = stream.read(2048)
    if walle.AcceptWaveform(data):
        print("Full " , walle.Result())
        # result = ast.literal_eval(walle.Result())
        # result = result["text"]
        # print(result)
        # print(Analyze(walle.Result()))
