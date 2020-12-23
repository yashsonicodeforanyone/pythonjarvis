import pyttsx3  #sudio module
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)  #to show how many voices is here
engine.setProperty('voice',voices[0].id)
# print(voices[1].id)  #to show voice male or female
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    
    elif hour>=12 and hour<18:
        speak("good afternonn")

    else:
        speak("good evening")

    speak("i am jarvis sir how may i help you")


def takeCommand():
    #it take microphon on user and give string output 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1  
        #go to the module ctrl and click argument
        audio=r.listen(source)

    try:
        print("Recorgnize...")
        query=r.recognize_google(audio,language='en-IN')
        print(f"user said: {query}")

    except Exception as e:
        print(e)
        print("say that again")
        return "None"
        

    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('/*here enter your email addreess*/','/*here enter your email addreess password*/')
    server.sendmail('/*here enter your email addreess*/',to,content)
    print("this sent success to function")
    server.close()




if __name__ == "__main__":
    
    wishme()
    # while True:
    if 1 :
        query=takeCommand().lower()
        # #login execute taksk for said

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia..")
            print(results)
            speak(results) 

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir='C:\\Users\\akash\\Music\\favsong'
            song=os.listdir(music_dir)
            print(song)
            print(type(song))
            os.startfile(os.path.join(music_dir,song[0]))

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:hour %M minute:%S second")
            speak(f"thie time is sir {strtime}")

        elif 'code open' in query:
            path_code="C:\\Users\\akash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path_code)
            print("code is open")

        elif 'email to yash' in query:
            try:
                speak("what should say")
                content=takeCommand()
                to="/*here enter email those person to send email addreess*/"
                sendEmail(to,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorryy i will not send this mail")

        elif 'wish me' in query:
            wishme()

        