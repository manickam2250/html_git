import speech_recognition as sr
import os
import pyttsx3 
with open("/home/manikam/Downloads/jokerim.txt","r")as file1:
    list=file1.read().split(".")
    i=0
    list2=[]
    # print(list)
    for li in list:
        li=li.replace("\n"," ")
        list2.append(li)

        with open("/home/manikam/write.txt","a")as file2:
         for li2 in list2:   
            file2.write(str(i)+")")   
            file2.write(li2+".\n")
            i+=1


r = sr.Recognizer() 
def SpeakText(command):
        engine = pyttsx3.init()
        rate = engine.setProperty('rate',120)
        # print(rate)
        for i in range(3):
            engine.say(command) 
            engine.runAndWait()
            engine.stop()

# print(list2)
for i in range(10,25):
 SpeakText(list2[i])