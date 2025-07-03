import sounddevice as sd
import queue, json
from vosk import Model, KaldiRecognizer
import numpy as np

model = Model("model") 

def recognize_speech_from_mic(duration=5):
    q = queue.Queue()
    samplerate = 16000
    rec = KaldiRecognizer(model, samplerate)

    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening...")
        data = b''
        for _ in range(int(samplerate / 8000 * duration)):
            data += q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            return result.get("text", "")
        return ""
