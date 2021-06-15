"""тестовый запуск речевых функций"""
from gtts import gTTS


def Say_my_name(myText, language):
    output = gTTS(text=myText, lang=language, slow=False)

    output.save("output.mp3")
