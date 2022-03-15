import PyPDF2
import speech_recognition as sr
import pyttsx3 
pdf=PyPDF2.PdfFileReader("/home/manikam/Downloads/how to.pdf")
page_1_obj = pdf.getPage(4)

data = page_1_obj.extractText()
list=data.split(".")
# print(list)
no=0
for li in list:
    with open("/home/manikam/ponni_4","a")as file1:
        file1.write(str(no)+")")
        file1.write(li+".\n")
        no+=1

r = sr.Recognizer() 
def SpeakText(command):
        engine = pyttsx3.init()
        rate = engine.setProperty('rate',115)
        # print(rate)
        for i in range(3):
            engine.say(command) 
            engine.runAndWait()
            engine.stop()
# for i in range(40,45):
#  SpeakText(list[i])