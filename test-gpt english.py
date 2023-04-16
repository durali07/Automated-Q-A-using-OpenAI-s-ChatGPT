import cv2
import pytesseract
import numpy as np
import pyautogui
from PIL import Image
import openai
import os
import random
from gtts import gTTS
from playsound import playsound
import time

while True:
    
    def speak(string):
        tts = gTTS(string, lang='en')
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
                print("First position saved:", first_position)
            elif key.char == '2':
                second_position = pyautogui.position()
                print("Second position saved:", second_position)
                keep_running = False
        except AttributeError:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        while keep_running:
            pass

    # Take a screenshot of the specified region
    left = min(first_position[0], second_position[0])
    top = min(first_position[1], second_position[1])
    width = abs(first_position[0] - second_position[0])
    height = abs(first_position[1] - second_position[1])
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save("screenshot.png")
    print("Screenshot saved.")

    time.sleep(2)

    # Set the path for Tesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # For Windows
    # pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract" # For Linux

    # Convert the screenshot to OpenCV format
    screenshot = Image.open("screenshot.png")
    opencv_screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Perform OCR on the screenshot
    questions = pytesseract.image_to_string(opencv_screenshot, lang="eng").split("\n")
    all_questions = " ".join(questions)

    # Print the extracted questions
    print("All questions:", all_questions)

    # Set up the OpenAI API key
    openai.api_key = "YOUR_API_KEY"

    # Ask the ChatGPT API a question
    prompt = all_questions
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the response from ChatGPT
    answer = response.choices[0].text.strip()
    print("Answer to the question:", answer)
    speak(answer)
