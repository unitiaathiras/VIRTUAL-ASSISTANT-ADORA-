'''I need a assistant that would help me to do all things with a single command'''
# import keyboard
import pyttsx3
import pywhatkit
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import os
import wikipedia
from googletrans import Translator
import pyautogui
import requests
import PyPDF2
from gtts import gTTS
import datetime
from playsound import playsound
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction
import whatsapp

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')

Assistant.setProperty('voices', voices[1].id)
Assistant.setProperty('rate', 170)


def Speak(audio):
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()


def take_command():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language='en-in')
            print(f"You Said:{query}")
        except:
            return "none"
        return query.lower()


def Task_Execution():

    def Music():
        Speak("Tell me the name of the song")
        music_name = take_command()

        if 'Anti Hero' in music_name:
            os.startfile('E:\\Songs\\Anti Hero.mp3')

        elif 'Blank Space' in music_name:
            os.startfile('E:\\Songs\\Blank Space.mp3')

        elif 'Look' in music_name:
            os.startfile('E:\\Songs\\Look What You Made Me Do.mp3')

        elif 'Shake it' in music_name:
            os.startfile('E:\\Songs\\Shake it Off.mp3')
        else:
            pywhatkit.playonyt(music_name)

        Speak("Your song has been started enjoy sir")

    def OpenApps():
        Speak("Ok sir wait a second")

        if 'code' in query:
            os.startfile('"C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')

        elif 'notion' in query:
            os.startfile('C:\\Users\\admin\\AppData\\Local\\Programs\\Notion\\Notion.exe')

        elif 'git' in query:
            os.startfile('E:\\python_project\\Git\\git-bash.exe --cd-to-home')

        elif 'chrome' in query:
            os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/place/Kallamala+school+mukk(%E0%B4%95%E0%B4%B3%E0%B5%8D%E0%B4%B3%E0%B4%AE%E0%B4%B2+%E0%B4%B8%E0%B5%8D%E0%B4%95%E0%B5%82%E0%B5%BE+%E0%B4%AE%E0%B5%81%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%8D+)/@11.0527623,76.5638562,17z/data=!3m1!4b1!4m6!3m5!1s0x3ba8875b3b5db181:0x31e66dda658816e6!8m2!3d11.052757!4d76.5664311!16s%2Fg%2F11k4770bxv')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        elif 'telegram' in query:
            webbrowser.open('https://www.telegram.com')

        Speak("Your command has been completed")

    def SpeedTest():
        import speedtest
        Speak("Checking speed...")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctUpload = int(uploading/800000)

        if 'uploading' in query:
            Speak(f"The uploading speed is {correctUpload} mbp s")
        elif 'downloading' in query:
            Speak(f"The Downloading speed is {correctDown} mbp s")
        else:
            Speak(f"The Downloading speed is {correctDown} and the uploading spped is {correctUpload} mbp s")

    def Temp():
        search = "temperature in agali"
        url = "https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_="BNeawe").text
        Speak(f"The temperature outside is {temperature} celcius")

    def Reader():
        Speak("Tell me the name of the book")

        name = take_command()

        if 'database' in name:
            os.startfile('E:\\Books\\Silberschatz_A_databases_6th_ed (2)')
            book = open('E:\\Books\\Silberschatz_A_databases_6th_ed (2)')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number of pages in this book are {pages}")
            Speak("From which page i have to start reading?")
            numPage = int(input("enter the page number"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In which language, i have to read?")
            lang = take_command()

            if 'malayalam' in lang:
                transl = Translator()
                textMal = transl.translate(text, 'ml')
                textm = textMal.text
                speech = gTTS(text=textm)

                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    Speak(text)
            else:
                Speak(text)

        elif 'security' in name:
            os.startfile('E:\\Books\\DOC-20230315-WA0015_')
            book = open('E:\\Books\\DOC-20230315-WA0015_')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number of pages in this book are {pages}")
            Speak("From which page i have to start reading?")
            numPage = int(input("enter the page number"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In which language, i have to read?")
            lang = take_command()

            if 'malayalam' in lang:
                transl = Translator()
                textMal = transl.translate(text, 'ml')
                textm = textMal.text
                speech = gTTS(text=textm)

                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    Speak(text)
            else:
                Speak(text)


    def CloseApps():
        Speak("Ok sir wait a second")

        if 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'notion' in query:
            os.system("TASKKILL /F /im Notion.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im Code.exe")

        elif 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'git' in query:
            os.system("TASKKILL /F /im git-bash.exe")

        Speak("Your command has been successfully completed")


    def YoutubeAuto():
        Speak("Whats your command")
        comm = take_command()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        elif 'move to the next' in comm:
            keyboard.press('shift + p')

        elif 'move to the previous' in comm:
            keyboard.press('shift + n')

        Speak("Done sir")

    def TakeMalayalam():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing....")
                query = command.recognize_google(audio, language='ml')
                print(f"You Said:{query}")
            except:
                return "none"
            return query.lower()

    def Tran():
        Speak("Tell me the line")
        line = TakeMalayalam()
        traslate = Translator()
        result = traslate.translate(line)
        Text = result.text
        Speak("The translation for this line is " + Text)

    def ChromeAuto():
        Speak("Chrome Automation started")

        command = take_command()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')

    def Dict():
        Speak("activated dictionary")
        Speak("Tell me the word")
        probl = take_command()

        if 'meaning' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("adora", "")
            probl = probl.replace("of", "")
            probl = probl.replace("meaning of", "")
            result = Diction.meaning(probl)
            Speak(f"The meaning for {probl} is {result}")

        elif 'synonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("adora", "")
            probl = probl.replace("of", "")
            probl = probl.replace("synonym of", "")
            result = Diction.synonym(probl)
            Speak(f"The synonym for {probl} is {result}")

        elif 'antonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("adora", "")
            probl = probl.replace("of", "")
            probl = probl.replace("antonym of", "")
            result = Diction.antonym(probl)
            Speak(f"The antonym for {probl} is {result}")

        Speak("Exited Dictionary")

    def screenshot():
        Speak("Ok boss, what should i name that file")
        path = take_command()
        path1name = path + ".png"
        path1 = "E:\\Screenshots\\" + path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("E:\\Screenshots")
        Speak("Here is your screenshot")

    while True:

        query = take_command()

        if 'hello' in query:
            Speak("Hello boss, iam adora")
            Speak("Your personal virtual assistant")
            Speak("How may i help you")

        elif 'how are you' in query:
            Speak("iam fine sir")
            Speak("whats about you")

        elif 'you need a break' in query:
            Speak("Ok Sir, You can call me anytime")
            break

        elif 'enikk maduthu' in query:
            Speak("Go and take short break you will feel better")

        elif 'ok namukk pinne kanam' in query:
            Speak("Ok bye see you soon")
            break

        elif 'namukk enn kore work pending ind' in query:
            Speak("Fight for it boss")

        elif 'bye' in query:
            Speak("Ok sir, Bye")
            break

        elif 'youtube search' in query:
            Speak("Ok sir, This is what i found for your search")
            query = query.replace('adora', "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)
            Speak("Done sir")

        elif 'google search' in query:
            Speak("This is what i found for you")
            query = query.replace('adora', "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            Speak('Done ')

        elif 'website' in query:
            Speak("Ok sir, launching..")
            query = query.replace('adora', "")
            query = query.replace("website", "")
            query = query.replace(" ", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched ")
        elif 'launch' in query:
            Speak("Tell me name of the website")
            name = take_command()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done sir")
        elif 'facebook' in query:
            Speak("Ok sir")
            webbrowser.open("https://www.facebook.com")
            Speak("Done sir")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Searching wikipedia")
            query = query.replace("adora", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 2)
            Speak(f"According to wikipedia :{wiki}")

        elif 'whatsapp message' in query:
            query = query.replace("adora", "")
            query = query.replace("send", "")
            query = query.replace("whatsapp meassage", "")
            query = query.replace("to", "")
            name = query

            if 'Unni Mols' in name:
                numb = "+91 9744119339"
                Speak(f"Whats the message for {name}")
                mess = take_command()
                whatsapp.whatsapp(numb, mess)
                Speak("Ok boss, sending whatsapp message")

            elif 'Shibili' in name:
                numb = "+91 9744119339"
                Speak(f"Whats the message for {name}")
                mess = take_command()
                whatsapp.whatsapp(numb, mess)
                Speak("Ok boss, sending whatsapp message")

            elif 'cheriyachan' in name:
                numb = "+91 9656344316"
                Speak(f"Whats the message for {name}")
                mess = take_command()
                whatsapp.whatsapp(numb, mess)
                Speak("Ok boss, sending whatsapp message")

            elif 'database' in name:
                gro = "KRcJydibmPK2dJvgwQt0uB"
                Speak(f"Whats the message for {name}")
                mess = take_command()
                whatsapp.Whatsapp_Grp(gro, mess)

        elif 'screenshot' in query:
            screenshot()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()

        elif 'notion' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'close chrome' in query:
            CloseApps()

        elif 'close notion' in query:
            CloseApps()

        elif 'close facebook' in query:
            CloseApps()

        elif 'close instagram' in query:
            CloseApps()

        elif 'close telegram' in query:
            CloseApps()

        elif 'close maps' in query:
            CloseApps()

        elif 'close code' in query:
            CloseApps()

        elif 'close git' in query:
            CloseApps()

        elif 'close youtube' in query:
            CloseApps()

        # Youtube automation
        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'move to the next' in query:
            keyboard.press('shift + p')

        elif 'move to the previous' in query:
            keyboard.press('shift + n')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my words' in query:
            Speak("speak sir")
            jj = take_command()
            Speak(f"you said: {jj}")

        elif 'my location' in query:
            Speak("ok sir, wait a second")
            webbrowser.open('https://www.google.com/maps/place/Kallamala+school+mukk(%E0%B4%95%E0%B4%B3%E0%B5%8D%E0%B4%B3%E0%B4%AE%E0%B4%B2+%E0%B4%B8%E0%B5%8D%E0%B4%95%E0%B5%82%E0%B5%BE+%E0%B4%AE%E0%B5%81%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%8D+)/@11.0527623,76.5638562,17z/data=!3m1!4b1!4m6!3m5!1s0x3ba8875b3b5db181:0x31e66dda658816e6!8m2!3d11.052757!4d76.5664311!16s%2Fg%2F11k4770bxv')

        elif 'dictionary' in query:
            Dict()

        elif 'alarm' in query:
            Speak("Enter the time")
            time = input(": enter the time:")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake up boss")
                    playsound('Alarm.mp3')
                    Speak("boss alarm closed")

                elif now > time:
                    break

        elif 'translator' in query:
            Tran()

        elif 'remember that' in query:
            rememberMsg = query.replace("remember that", "")
            rememberMsg = rememberMsg.replace("adora", "")
            Speak(f"You tell me to remind you that: "+rememberMsg)
            remember = open('data.txt', 'w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query:
            remember = open('data.txt', 'r')
            Speak("You tell me that:" +remember.read())

        elif 'google scrap' in query:
            import wikipedia as googleScrap
            query = query.replace('adora')
            query = query.replace("google scrap", "")
            query = query.replace("google", "")
            Speak("This is what i found on the web")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query, 2)
                Speak(result)

            except:
                Speak("No speakable data available")

        elif 'temperature' in query:
            Temp()

        elif 'read a book' in query:
            Reader()

        elif 'downloading speed' in query:
            SpeedTest()

        elif 'uploading speed' in query:
            SpeedTest()

        elif 'internet speed' in query:
            SpeedTest()

        elif 'how to' in query:
            Speak("Getting data from internet")
            op = query.replace("adora", "")
            max_result = 1
            how_to_func = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)


