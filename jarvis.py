import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import datetime
import google.generativeai as genai
import re

from config import apikey
chatstr =""
def chat(query):
    global chatstr
    genai.configure(api_key=apikey)
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(query)
    reply = response.text.replace("*", "")

    # keep chat history updated
    chatstr += f"prem said: {query}\njarvis said: {reply}\n"

    # speak only the latest reply
    say(reply)




def ai(promptt):

    text = f"Gemin response for Prompt : {promptt} \n *************************************\n\n"

    genai.configure(api_key=apikey)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # custom prompt
    prompt = promptt
    #todo : wrap it inside of a try catch block

    response = model.generate_content(prompt)
    # text += response.text
    text = re.sub(r'[*_`#]', '', response.text)
    # print(response.text)
    if not os.path.exists("GENai"):
        os.mkdir("GENai")

    with open(f"Genai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


   # say(response.text)
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#say("")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try :
            print("recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e :
            return "Some error occurred. Sorry!!  "




if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("welcome to Jarvis AI")

    while True :  ## this while condition makes sure ki wo lagatar sunn raha hai
         print("Listening...")

         query = takeCommand()
         if "Some error occurred" in query:
             say(query)
             break  #
## todo : add more sites
         sites= [["Youtube" ,"http://www.youtube.com"] , ["instagram" ,"http://www.instagram.com"]]
         for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
## todo : add feature to play songs
            elif "open music".lower() in query.lower():
                musicpath = r"C:\Users\dell\Downloads\Arz Kiya Hai - PagalWorld.mp3"
                os.startfile(musicpath)

            elif "the time" in query.lower():
                hour = datetime.datetime.now().strftime("%H")
                minn = datetime.datetime.now().strftime("%M")
                seconds = datetime.datetime.now().strftime("%S")
                print(f"{hour}:{minn}:{seconds}")
                say(f"Sir the time is {hour} baajkee  {minn} minutes aurr {seconds} seconds")

            elif f"open discord".lower() in query.lower():
                pathh = r"C:\Users\dell\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk"
                os.startfile(pathh)

            elif f"open vs code".lower() in query.lower():
                path1 = r"C:\Users\dell\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"
                os.startfile(path1)

            elif f"using Artificial intelligence".lower() in query.lower():
                ai(promptt=query)

            elif "stop jarvis" in query.lower():
                say("Goodbye sir!")
                exit()

            else:
               chat(query)
               break

