import pyttsx3
import speech_recognition
import wikipedia
import pywhatkit
import pyjokes
import datetime
import pyaudio
import webbrowser
import os




engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
print(voice[1].id)
engine.setProperty('voice',voice[1].id)



def say_(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greatMe():
    hour= int(datetime.datetime.now().hour)    
    if hour>=0 and hour<12:
        say_("Good Morning! ")
        say_("I hope your day wil be great.")

    elif hour>=12 and hour<18:
        say_("Good Afternoon! ")

    else:
        say_("Good Evenine! ")

    say_("I am Memo. Your personal voice assistant. please tell me how may I help you ?")            

def takeInput():

    res = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listining.....")
        res.pause_threshold = 2
        audio=res.listen(source)
    try:
        print("Recognizing...")    
        query=res.recognize_google(audio, language='en-in')
    except Exception as e:
        print(e) 
        say_("Sorry for concern. would you please say it again.")
        return "None" 
    return query    

def commands():
     while True:
        query = takeInput().lower()

        if 'wikipedia' in query:
            say_('Searching Wikipedia....')
            query= query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            say_("According to Wikipedia")
            print(results)
            say_(results)
        elif 'hi!' or 'hello!' or 'hey' in query:
            say_("hello boss!") 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'play music' in query:
            music_dir='G:\\music'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            say_(f"Sir, the time is {strTime}")
        elif 'stop' in query:
            if 'wait' in query:
                commands()
            else:
                exit()
if __name__== "__main__": 
    greatMe()
    commands()