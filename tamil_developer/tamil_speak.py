import speech_recognition as sr
import pyttsx3 
from gtts import gTTS

needed_list=[]

with open("/home/manikam/Downloads/css_tamil.txt","r")as file1:
    list=file1.read().split(".")
    for li in list:
        li=(li.replace("\n"," "))
        needed_list.append(li)

gTTS.__init__()
# def SpeakText(command):
#         engine = pyttsx3.init()
#         rate = engine.setProperty('rate',200)
#         # print(rate)
#         for i in range(1):
#             engine.say(command) 
#             engine.runAndWait()
#             engine.stop()

SpeakText(needed_list[0])