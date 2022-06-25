from fileinput import close
from ftplib import MAXLINE
from json.tool import main
from logging import exception
from multiprocessing.spawn import _main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from email.message import EmailMessage


email_book={
    'Sonal':'sonalagrawal1101@gmail.com',
    'Sonu':'sonalagrawal320@gmail.com'
    }



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hr=int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("Good Morning!")

    elif hr>=12 and hr<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am Alex Please tell me how may I help you")

def SendMail(to,sub,cont):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("testalexprojectmail123@gmail.com","testalex")
    email=EmailMessage()
    email['From']='testalexprojectmail123@gmail.com'
    email['To']=to
    email['subject']=sub
    email.set_content(cont)
    server.sendmail('testalexprojectmail123@gmail.com',to,cont)
    server.send_message(email)
    server.close()    

def takeCommand():
    # takes voice command and gives string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising....")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
       # print(e)

        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    speak("hello Sonal")
    wishme()
    query=takeCommand().lower()

    if 'wikipedia' in query:
        print("searching Wikipedia.....please wait")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query, sentences=2)
        #speak("According to wikipedia")
        speak(results)

    if 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open geeksforgeeks' in query:
        webbrowser.open("geeksfoegeeks.org")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'open gmail' in query:
        webbrowser.open("gmail.com")
    elif 'play music' in query:
        music_dir='C:\\Users\\Hp\\Music\\Maroon'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%s")
        speak(f"the time is {strTime}")

    elif 'open code' in query:
        codepath="C:\\Users\\Hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
        os.startfile(codepath)

    elif 'open teams' in query:
        teamspath="C:\\Users\\Hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams"
        os.startfile(teamspath)

    elif 'open notepad' in query:
        padpath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
        os.startfile(padpath)

    elif 'open dictionary' in query:
        dicpath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Sheel's Dictionary"
        os.startfile(dicpath)

    elif 'send mail' in query:
        try:
            speak("to whome do you wish to send mail?")
            find=takeCommand()
            speak("what is the subject of your mail?")
            sub=takeCommand()
            speak("what is the content of the mail?")
            cont=takeCommand()
            to=email_book[find]
            SendMail(to,sub,cont)
            speak("mail sent!")

        except Exception as e:
            print(e)
            print("Sorry Sonal I am unable to send this email")

        


    

    




    
