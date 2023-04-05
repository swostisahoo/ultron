import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser  
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning sir!")
    elif hour>=12 and hour<18:
        speak ("good afternoon sir!")
    else:
        speak("good eveing sir!")
    speak("sir how may i help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listenning .....")
        r.pause_threshold = 1
        audio =  r.listen(source)
    try:
        print("Recognizing .....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n" )
        speak(f"user said{query}")
    except Exception as e:
        
        print("say that again please.")
        return "none"
    return query
        
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
           webbrowser.open("youtube.com")
      
        elif 'open amazon prime' in query:
           webbrowser.open("https://www.primevideo.com/gp/video/storefront?filterId=OFFER_FILTER=ALL")
      
        elif 'open disney plus' in query:
           webbrowser.open("https://www.hotstar.com/in")
      
        elif 'open google' in query:
           webbrowser.open("google.com")
        elif '  the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)
        elif 'send email' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
         
