# Automated-Q-A-using-OpenAI-s-ChatGPT


Bu kod, Python programlama dili kullanılarak yazılmış bir OpenAI Chatbotu'dur. Bu Chatbot, kullanıcının ekran görüntüsü aldığı sorulara cevap vermek için OpenAI'nın ChatGPT modelini kullanır.

Program ayrıca, ekran görüntüsü almak için PyAutoGUI, optik karakter tanıma (OCR) için Tesseract, ve konuşma sentezi için gTTS kütüphanelerini kullanır.

Ayrıca program, kullanıcının klavyeden 1 ve 2 tuşlarına basarak ekran görüntüsü alacağı bölgenin köşe noktalarını belirleyebilmesi için Pynput kütüphanesi kullanır.

Program, aldığı soruların yanı sıra, cevabı sesli olarak söylemek için konuşma sentezini de kullanır. Bunun yanı sıra, program, sesli komutlara cevap vermek için Python'un SpeechRecognition kütüphanesini kullanır.

Bu kod, OpenAI API'sine erişmek için bir API anahtarı gerektirir. Ayrıca, Tesseract'in yüklü olduğu konumun doğru bir şekilde belirtilmesi gerekir. Bu kod, sadece Windows işletim sistemi için test edilmiştir ve Linux işletim sistemlerinde farklı bir yolda Tesseract yüklendiği için düzenleme gerektirebilir.



This code is an OpenAI Chatbot written in the Python programming language. The Chatbot uses OpenAI's ChatGPT model to answer questions that the user takes a screenshot of.The program also uses the PyAutoGUI library to take screenshots, the Tesseract library for optical character recognition (OCR), and the gTTS library for speech synthesis.Additionally, the program uses the Pynput library for the user to select the corner points of the area where they want to take a screenshot by pressing the 1 and 2 keys on their keyboard.The program uses speech synthesis to audibly speak the answer to the question it receives. Additionally, it uses Python's SpeechRecognition library to respond to voice commands.This code requires an API key to access the OpenAI API, and the correct location of Tesseract must be specified. It has only been tested on Windows operating systems and may require editing for different paths to Tesseract on Linux operating systems.
