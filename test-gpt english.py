import pytesseract
import cv2
from PIL import ImageGrab
import re
import numpy as np
from pynput import keyboard
import pyautogui
from PIL import Image
import openai
from fnmatch import translate
import speech_recognition as sr
from pydub import AudioSegment
from pydub import effects
from pydub.playback import play
import os
import random
from gtts import gTTS
from pydub import AudioSegment
from playsound import playsound
import time
import pyperclip
import win32clipboard

while True:

    def speak(string):
        tts = gTTS(string, lang='en')
        rand = random.randint(1, 10000)
        filed = 'audio-' + str(rand) + '.mp3'
        tts.save(filed)
        velocipede = 1.30 # Hız
        sound = AudioSegment.from_file(filed)
        so = sound.speedup(velocipede, 150, 25)
        so.export(filed, format='mp3')
        time.sleep(1)
        playsound(filed)
        time.sleep(1)
        os.remove(filed)


    def chtGPT():
        print("panodan alıyor")
        openai.api_key = "APİ_KEY"
        messages = [ {"role": "system", "content": 
                    "You are a intelligent assistant."} ]
        message = pyperclip.paste()
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            reply = chat.choices[0].message.content
            print(f"ChatGPT: {reply}")
            messages.append({"role": "assistant", "content": reply})
            
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.CloseClipboard()

            # ChatGPT'nin cevabını yazdırın
            cevap = reply
            tts = gTTS(cevap, lang='tr')
            rand = random.randint(1, 10000)
            filed = 'audio-' + str(rand) + '.mp3'
            tts.save(filed)
            playsound(filed)
            time.sleep(1)
            os.remove(filed)
        


    first_position = None
    second_position = None
    keep_running = True

    def on_press(key):
        global first_position, second_position, keep_running
        try:
            if key.char == '1':
                first_position = pyautogui.position()
                print("İlk konum kaydedildi:", first_position)
            elif key.char == '2':
                second_position = pyautogui.position()
                print("İkinci konum kaydedildi:", second_position)
                keep_running = False
            elif pyperclip.paste() != '':
                chtGPT()
        except AttributeError:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        while keep_running:
            pass

    # İki konum arasındaki ekran görüntüsünü al
    left = min(first_position[0], second_position[0])
    top = min(first_position[1], second_position[1])
    width = abs(first_position[0] - second_position[0])
    height = abs(first_position[1] - second_position[1])
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save("screenshot.png")
    print("Ekran görüntüsü kaydedildi.")

    # Tesseract'in yolunu belirtin
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # Windows için
    # pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract" # Linux için

    # Ekran görüntüsü al
    screenshot = Image.open("screenshot.png")

    # Ekran görüntüsünü OpenCV formatına dönüştür
    opencv_screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    # OCR işlemini gerçekleştir
    sorular = pytesseract.image_to_string(opencv_screenshot,lang="eng").split("\n")
    # Tüm soruları birleştir
    tum_sorular = " ".join(sorular)

    # Birleştirilmiş soruları görüntüle
    print("Tüm sorular:", tum_sorular)


    # OpenAI API anahtarını buraya girin
    openai.api_key = "APİ_KEY"
    messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
    message = tum_sorular
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    speak(reply)
