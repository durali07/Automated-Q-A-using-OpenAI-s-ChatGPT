# Automated-Q-A-using-OpenAI-s-ChatGPT


Bu kod, Python programlama dili kullanılarak yazılmış bir OpenAI Chatbotu'dur. Bu Chatbot, kullanıcının ekran görüntüsü aldığı sorulara cevap vermek için OpenAI'nın ChatGPT modelini kullanır.

Program ayrıca, ekran görüntüsü almak için PyAutoGUI, optik karakter tanıma (OCR) için Tesseract, ve konuşma sentezi için gTTS kütüphanelerini kullanır.

Ayrıca program, kullanıcının klavyeden 1 ve 2 tuşlarına basarak ekran görüntüsü alacağı bölgenin köşe noktalarını belirleyebilmesi için Pynput kütüphanesi kullanır.

Program, aldığı soruların yanı sıra, cevabı sesli olarak söylemek için konuşma sentezini de kullanır. Bunun yanı sıra, program, sesli komutlara cevap vermek için Python'un SpeechRecognition kütüphanesini kullanır.

Bu kod, OpenAI API'sine erişmek için bir API anahtarı gerektirir. Ayrıca, Tesseract'in yüklü olduğu konumun doğru bir şekilde belirtilmesi gerekir. Bu kod, sadece Windows işletim sistemi için test edilmiştir ve Linux işletim sistemlerinde farklı bir yolda Tesseract yüklendiği için düzenleme gerektirebilir.

