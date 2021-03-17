import speech_recognition as sr  #for voice recogonition
import playsound #to play the audio
import random   #to make random choices
from gtts import gTTS  #google text to speech package 
import os  #to manage the files 
import wolframalpha #a computational knowledge engine
import webbrowser #to manage browser
import wikipedia #to Get Wikipeda information
import datetime #for date and time
import sys #to manipulate the different parts of the python environment
num = 1


def assistant_speaks(output): #output audio and text 
    global num
    num +=1
    print("Adjutant : ", output)
    toSpeak = gTTS(text=output, lang='en-US', slow=False)
    file = str(num)+".mp3"
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)
def get_audio(): #to get inp audio and convert it into text 
    r = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Receiving...")
        audio = r.listen(source, phrase_time_limit=5)
    print("Received.")
    try:
        text = r.recognize_google(audio,language='en-US')
        print("You : ", text)
        return text
    except:
        assistant_speaks("Could not understand your audio, Please try again!")
        return ''

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        assistant_speaks('Good Morning! Would you like to text or speak?')

    if currentH >= 12 and currentH < 18:
        assistant_speaks('Good Afternoon! Would you like to text or speak?')

    if currentH >= 18 and currentH !=0:
        assistant_speaks('Good Evening! Would you like to text or speak?')
    mode = input()
    return mode


def search_web(inp): #to open google for search
    webbrowser.open('www.google.com')
    return

def edu_search(mode): #opens specific websites
    speak = 'Please specify an institution'
    assistant_speaks(speak)
    inp = ''
    if 'speak' in mode or 'talk' in mode:
        inp = get_audio().lower()
    elif 'text' in mode or 'type' in mode:
        inp = input().lower()
    if 'kite' in inp or 'kgkite' in inp or 'engineering' in inp:
        assistant_speaks('Affirmative, please wait while www.kgkite.ac.in opens')
        webbrowser.open('www.kgkite.ac.in')
        return
    elif 'cass' in inp or 'arts' in inp or 'science' in inp or 'cas' in inp :
        assistant_speaks('Affirmative, please wait while www.kgcas.com opens')
        webbrowser.open('www.kgcas.com')
        return
    elif 'nursing' in inp or 'nurse' in inp or 'medical' in inp :
        assistant_speaks('Affirmative, please wait while https://www.kghospital.com/nursing-college.html opens')
        webbrowser.open('https://www.kghospital.com/nursing-college.html')
        return
    return


def process_text(inp,mode): #function to interact with Adjutant and also to determine other functions
    try:
        if "who are you" in inp:
            speak = 'Hello, I am your Adjutant'
            assistant_speaks(speak)
            return
        elif 'hello' in inp or 'hey' in inp or inp == 'hi':
            stMsgs = ['Greetings','Hello', 'Hi']
            assistant_speaks(random.choice(stMsgs))
            return
        elif "joke" in inp :
            stMsgs=["I just got a photo from a speeding camera through the mail. I send it right back - way too expensive and really bad quality","8 pm I get an SMS from my girlfriend : Me or football?! 11pm. I SMS my girlfriend.You ofcourse."]
            assistant_speaks(random.choice(stMsgs))
            return
        elif "thanks" in inp or "thank you" in inp:
            stMsgs=["I am here to serve"]
            assistant_speaks(random.choice(stMsgs))
            return
        elif "time" in inp :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            assistant_speaks(f"the time is {strTime}")
            return
        elif 'bye' in inp:
            currentH = int(datetime.datetime.now().hour)
            if currentH >= 18 and currentH !=0:
                speak('Good Night')
            else:
                stMsgs=['Bye , have a good day.','see you soon']
                speak(random.choice(stMsgs))
                sys.exit()
            return
        elif "wikipedia" in inp :
            results = wikipedia.summary(inp.lower(), sentences=2)
            assistant_speaks('Got it.')
            assistant_speaks('According to wikipedia : ')
            assistant_speaks(results)
            return  
        elif 'search' in inp or 'play' in inp:
            search_web(inp.lower())
            return
        elif 'education' in inp or 'college' in inp or 'admission' in inp:
            edu_search(mode)
            return
        elif 'consultancy' in inp or 'development' in inp or 'cloud' in inp or 'security' in inp :
            assistant_speaks('Affirmative, please wait while https://www.kgisl.com/gss/ opens')
            webbrowser.open('https://www.kgisl.com/gss/')
            return
        elif 'sick' in inp or 'doctor' in inp or 'hospital' in inp or 'emergency' in inp or 'ill' in inp or 'appointment' in inp or 'diagnose' in inp or 'corona' in inp or 'disease' in inp or 'virus' in inp or 'covid' in inp or 'cold' in inp or 'fever' in inp or 'runny nose' in inp:
            assistant_speaks('Affirmative, please wait while https://www.kghospital.com/telehealth.html opens')
            webbrowser.open('https://www.kghospital.com/telehealth.html')
            return

        else:
            query = inp
            assistant_speaks('Let me see')
            try:
                try:
                    client = wolframalpha.Client('XVLP9Q-7YTYAQ3WHA')
                    res = client.query(query)
                    results = next(res.results).text
                    assistant_speaks('Got it.')
                    assistant_speaks(results)
                except:
                    assistant_speaks("May I search the web for you?")
                    if 'speak' in mode or 'talk' in mode:
                        ans = get_audio()
                    else:
                        ans = input()
                    if 'yes' in str(ans) or 'yeah' in str(ans):
                        search_web(inp)
            except :
                return
    except Exception as e:
        print(e)
        assistant_speaks("I don't understand, may I search the web for you?")
        if 'speak' in mode or 'talk' in mode:
            ans = get_audio()
        else:
            ans = input()
        if 'yes' in str(ans) or 'yeah' in str(ans) or 'sure' in str(ans) or 'fine' in str(ans) or 'OK' in str(ans):
            search_web(inp)

if __name__ == "__main__": #to run directly
    mode = greetMe()
    assistant_speaks("How may I serve?")

    text = ''
    if 'speak' in mode or 'talk' in mode:

        while(1):
            if isinstance(text,str):
                text = get_audio().lower()
            if text == '':
                continue
            if "exit" in str(text) or "bye" in str(text) or "good bye" in str(text) or "stop" in str(text):
                assistant_speaks("It has been an honour.")
                break
            process_text(text,mode)
    elif 'text' in mode or 'type' in mode :
        while (1):
            if isinstance(text, str):
                text = input().lower()
            if text == '':
                continue
            if "exit" in str(text) or "bye" in str(text) or "good bye" in str(text) or "stop" in str(text):
                assistant_speaks("It has been an honour.")
                break
            process_text(text,mode)

