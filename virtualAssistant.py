import warnings
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import playsound
import os
import datetime
import time
import calendar
import random
import wikipedia
import pywhatkit




warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice','com.apple.speech.synthesis.voice.Alex')
engine.setProperty('rate', 190)
engine.setProperty('volume', 2.0)
 
    

    
def talk(audio):
     engine.say(audio)
     engine.runAndWait()
     
     
def speechToText():
    r = sr.Recognizer()

    audio = None
    print("Google Listening.....")
    with sr.Microphone() as source:
        audio = r.listen(source)
        
    try:
        audio = r.recognize_google(audio, language = 'en-us', show_all=False)
        print("User Speaking:  "+audio)
        print()
        return audio
        
    except sr.UnknownValueError:
        print("Google is clueless.")
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        
     
        
    return ""
        
        
    
    
def virtualAssistantResponse(text):
    print("Assistant Speaking:  "+text.strip())
    print()
    tts = gTTS(text=text,lang="en")
    
    audio = "Audio.mp3"
    
    tts.save(audio)
    
    playsound.playsound(audio)
    
    os.remove(audio)
    
    
def detectWakeWord(text):
    assistant_name = "google"
    if assistant_name in text.lower():
        #print("wake word detected.")
        return True
   
    return False
    
    
def tellDate():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day
    year_now = now.year
    
    months = ['January', 
              'February',
              'March', 'April',
              'May', 'June',
              'July', 
              'August', 
              'September', 
              'October', 
              'November', 
              'December'
              ]
    
    ordinals = ['1st', '2nd', '3rd', '4th', 
                '5th', '6th', '7th', '8th', 
                '9th', '10th','11th', '12th', 
                '13th', '14th', '15th', '16th', 
                '17th', '18th', '19th','20th', 
                '21st', '22nd', '23rd', '24th', 
                '25th', '26th', '27th', '28th',
                '29th', '30th', '31st']
    
    
    
    
    
    return f'Today is {week_now}, {ordinals[day_now -1]} of {months[month_now - 1]} {year_now}'
    
    

def sayHello(text):
    
    greetings = {"hello","hi","hy","greetings","hola","salam"}
    response  = ["hello,hi","hy","greetings!","what's up","hola","salam"]
    words = [''.join(char for char in word.lower() if char.isalnum())  for word in text.split()]
    
    if text == "what's up":
        return random.choice(response)
  
    for word in words:
        if word.lower() in greetings:
            return random.choice(response)+" Human"
        
        
    return ""


def who(text):
    
    sentence = text.split()
        
    person = ""
    for i in range(len(sentence)):
        if sentence[i] == "who" and sentence[i+1] == "is":
            for j in range(i+2, len(sentence)):
                person+= " "+''.join(char for char in sentence[j].lower() if char.isalnum())
            break

    return str(person)
        
    
        
def main_driver():
    while True:
   
       # try:

            text = speechToText()
            text = text.lower()
            speak = ""
         
            if(detectWakeWord(text)):
                
                speak = speak + sayHello(text)
               
                
                if "day" in text or "date" in text or "month" in text:
                    getToday = tellDate()
                    speak = speak + " " + getToday
                    
                elif "time" in text:
                    now = datetime.datetime.now()
                    hour = None
                    minute = ""
                    meridiem = ""
                    
                    if now.hour >= 12:
                        meridiem = "p.m"
                        hour = now.hour - 12
                        
                    else:
                        meridiem = "a.m"
                        hour = now.hour
                    
                    if now.minute < 10:
                        minute = "0" + str(now.minute)
                    else:
                        minute = "00"
                        
                        
                    
                    
                    speak = speak + " " + "It is " +str(hour) + ":" + str(minute) + " " + meridiem + " ."
                    
                    
            
                elif "who is" in text:
                    person = who(text)
                    wiki = wikipedia.summary(person,2)
                    speak = speak + " " + wiki
                    
                    
                elif "open" in text:
                    
                    if "chrome" in text:
                        speak = speak + "Opening google chrome."
                        os.system("google-chrome")

                       
                    elif "ms word" in text:
                        speak = speak + "Opening ms word."
                        os.system("libreoffice")
                        
                    elif "firefox" in text:
                        speak = speak + "Opening firefox."
                        os.system("firefox")
                        
                        
                    else:
                        pass
                    
                    
                elif "play" in text:
                    
                    if "youtube" in text:
                        text = text.replace("play","")
                        text = text.replace("on","")
                        text = text.replace("youtube","")
                        speak = speak + "Playing "+text+" on youtube."
                        pywhatkit.playonyt(text)
                        
                        
                elif "search" in text:
                    
                    if "google" in text:
                        text = text.replace("search","")
                        text = text.replace("on","")
                        text = text.replace("google","")
                        speak = speak + "Searching "+text+" on google."
                        pywhatkit.search()(text)
                        
                        
                elif "close current tab" in text:
                    speak = speak + "closing current tab."
                    pywhatkit.close_ta
                    b()
                    
                 
                    
                elif "sleep" in text:
                    virtualAssistantResponse("For how many seconds you want me to sleep")
                    text = speechToText()
                    print(text)
                    seconds = text.split()
                    virtualAssistantResponse("Sleeping for "+str(seconds[0])+" seconds.")
                    time.sleep(int(seconds[0]))
                    continue
                    
                
                elif "die" in text:
                    virtualAssistantResponse("I will never forgive you. I am dying. Goodbye.")
                    break
                    
            
                  
                virtualAssistantResponse(speak)
        #except:
        #    print("I don't know that.")



if __name__ == "__main__":
    main_driver()
           
                