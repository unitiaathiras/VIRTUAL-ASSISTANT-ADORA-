'''I need a assistant that would help me to do all things with a single command'''
# import keyboard
import pyttsx3
import pywhatkit
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import pyautogui
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')

Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 170)


def Speak(audio):
    print("   ")
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

    def Whatsapp():
        Speak("Tell me the name of the person")
        name = take_command()

        if 'Unni Mols' in name:
            Speak("Tell me the message")
            msg = take_command()
            Speak("Tell me the time boss")
            Speak("Time in hour")
            hour = int(take_command())
            Speak("Time in minutes")
            min = int(take_command())
            pywhatkit.sendwhatmsg("+91 9744119339", msg, hour, min, 20)
            Speak("Ok boss, sending whatsapp message")

        elif 'Shibili' in name:
            Speak("Tell me the message")
            msg = take_command()
            Speak("Tell me the time boss")
            Speak("Time in hour")
            hour = int(take_command())
            Speak("Time in minutes")
            min = int(take_command())
            pywhatkit.sendwhatmsg("+91 9656344316", msg, hour, min, 20)

        elif 'Cheriyachan2' in name:
            Speak("Tell me the message")
            msg = take_command()
            pywhatkit.sendwhatmsg("+91 9656344316", msg)

        else:
            Speak("Tell me the phone number")
            phone = int(take_command())
            ph = '+91' + phone
            Speak("Tell me the message")
            msg = take_command()
            Speak("Tell me the time boss")
            Speak("Time in hour")
            hour = int(take_command())
            Speak("Time in minutes")
            min = int(take_command())
            pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)

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
            query = query.replace('adora',"")
            query = query.replace("website","")
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
            Whatsapp()

        elif 'screenshot' in query:
            Speak("Ok boss, what should i name that file")
            path = take_command()
            path1name = path + ".png"
            path1 = "E:\\Screenshots\\" + path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile("E:\\Screenshots")
            Speak("Here is your screenshot")

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
Speak("hello boss iam adora your personal virtual assistant how may i help you")
Task_Execution()