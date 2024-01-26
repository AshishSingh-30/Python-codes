import pyttsx3
import speech_recognition as sr
import datetime
import os
import time
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import pyjokes
import sys
import pyautogui
import random
import psutil
import speedtest
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#==========Text to Speech=========================
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#==========To convert voice into text================
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=8,phrase_time_limit=8)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said: {query}")
    except:
        pass
        return "none"
    return query

#==========To wish me==========================
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ,sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon ,sir")   
    else:
        speak("Good Evening , sir")
    speak("I am zela , What may I help you ?")

def sendEmail(To,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    speak("Sir,There are 3 account from which account you want to send mail: first,second or college id ??")
    command = take_command().lower()
    try:
        if "first" in command or "default" in command or "to me" in command:
            server.login("ashish.ksingh8765@gmail.com","8850ashish")
            server.sendmail("ashish.ksingh8765@gmail.com",To,content)
            server.close()
            speak("Email has been send.")       
        elif "second" in command:
            server.login("ashish.asingh8765@gmail.com","ashish8850")
            server.sendmail("ashish.asingh8765@gmail.com",To,content)
            server.close()
            speak("Email has been send.") 
        elif "college id" in command or "third" in command:
            server.login("singhashish@kccemsr.edu.in","ash1234ish")
            server.sendmail("singhashish@kccemsr.edu.in",To,content)
            server.close()
            speak("Email has been send.")
        else:
            speak("Sorry sir,There is no another account.!")
            speak("Email has not send !")    
    except:
        pass

#==========Task Execution===========================
def Task_Execution():
    wish_me()
    while True:

        query = take_command().lower()       
#===========System task==========================
        if "cmd" in query or "command prompt" in query:
            os.system("start cmd")
        elif "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        elif "open code" in query:
            np_path = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(np_path)
        elif "music" in query:
            music_dir = "C:\\Users\\amar singh\\Music\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif "video" in query:
            video_dir = "C:\\Users\\amar singh\\Videos"
            vi_songs = os.listdir(video_dir)
            rd = random.choice(vi_songs)
            os.startfile(os.path.join(video_dir, rd))
        elif "screenshot" in query:
            speak("Sir tell me the name of screenshot ?")
            name = take_command().lower()
            speak("Sir hold the screen for few seconds")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot done,next commnad sir")
        elif "battery" in query or "power" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percentage battery.")

#==========Online task============================

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is: {ip}")
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open google" in query:
            speak("Sir, What should I have to serach on google ?")
            search = take_command().lower()
            webbrowser.open(f"{search}")
        elif "go to instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "go to facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "play song on youtube" in query:
            song_yt = query.replace("play song on youtube","")
            speak("playing: " + song_yt)
            pywhatkit.playonyt(song_yt)     
        elif "who is" in query or "tell me about" in query or "information" in query:
            speak("Searching information..")
            query = query.replace("who is","")
            results = wikipedia.summary(query,sentences=2)
            speak(f"According to wikipedia: {results}")
        elif "message" in query:
            speak("To  whom you want to send a message ?")
            command = take_command().lower()
            if "danish" in command:
                speak("Enter the Message and correct timing.")
                msg = input("Message: ")
                tim_hour = int(input("The timing of hour should be in 24 format: "))
                tim_min = int(input("The timing of minute: "))
                pywhatkit.sendwhatmsg("+91-8689844904",msg, tim_hour,tim_min + 2)
                speak(f"Message has been send {command}")
            elif "aniket" in command:
                speak("Enter the Message and correct timing.")
                msg = input("Message: ")
                tim_hour = int(input("The timing of hour should be in 24 format: "))
                tim_min = int(input("The timing of minute: "))
                pywhatkit.sendwhatmsg("+91-9619269398",msg, tim_hour,tim_min + 2)
                speak(f"Message has been send to {command}")
            elif "python group" in command:
                speak("Enter the Message and correct timing.")
                msg = input("Message: ")
                tim_hour = int(input("The timing of hour should be in 24 format: "))
                tim_min = int(input("The timing of minute: "))
                pywhatkit.sendwhatmsg_to_group("EmvzPPn3MMgHfGGWiWAVUZ",msg, tim_hour,tim_min + 2)
                speak(f"Message has been send to {command}")
            else:
                speak("I don't have phone number.")    
                speak("Enter the phone number and Message with correct timing.")
                num = int(input("Enter the phone no.: "))
                msg = input("Message: ")
                tim_hour = int(input("The timing of hour should be in 24 format: "))
                tim_min = int(input("The timing of minute: "))
                pywhatkit.sendwhatmsg(f"+91{num}", msg, tim_hour,tim_min + 2)
                speak("Message has been send.")
        elif "internet speed" in query or "speedtest" in query or "speed" in query:
            speak("wait sir, for few seconds........")
            try:
                st = speedtest.Speedtest()
                download = (st.download()/(1025*1025))
                upload = (st.upload()/(1025*1025))
                ping = st.results.ping
                speak(f"Downloading speed: {download} Mbps.\nUploading speed: {upload} Mbps.\nPing: {ping}")
            except:
                speak("internet problem .!!!!!!!")
                pass
        elif "location" in query or "where we are" in query or "where i am" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir we are in {city} city of country {country}.")
            except:
                speak("Sorry sir due to network problem i am not able to find location !")
                pass
        elif "news" in query:
            speak("wait sir, fetching the news")
            news_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=bfbb0a9d7f624b5fa166c9b691caecd2"
            news_page = requests.get(news_url).json()
            articles = news_page["articles"]
            head = []
            content = []
            day = [" [first] = "," [second] = "," [third] = "]
            for ar in articles:
                head.append(ar["title"])
                content.append(ar["content"])
            for i in range (len(day)):
                speak(f"\nToday's {day[i]} news is: {head[i]} \ncontent is:[ {content[i]} ]\n")
        elif "weather" in query:
            speak("Tell me the city name")
            search = take_command().lower()
            url = f"http://www.google.com/search?q=temperature+in+{search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"Current temperature in {search} is {temp}")

#=============Bots===================================

        elif "send email" in query or "email" in query or "mail" in query:
            try:
                speak("what mail you want to send ?")
                content = input("Enter content: ")
                speak("Enter the Email id ")
                To = input("Email id: ")
                sendEmail(To,content)    
            except:
                speak("Sorry sir, I am not able to send email.")
                pass

        elif "instagram" in query:
            speak("Please wait sir,For few second.")
            try:
                def account_info():
                    with open('account_info.txt','r') as f:
                        info = f.read().split()
                        email = info[0]
                        password = info[1]
                    return email, password

                email, password = account_info()

                options = Options()
                options.add_argument("start-maximized")
                driver = webdriver.Chrome(executable_path='C:\\Users\\amar singh\\Desktop\\python\\Bot\\chromedriver.exe', options=options)

                driver.get("https://www.instagram.com/accounts/login/")

                email_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
                password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
                login_xpath = '//*[@id="loginForm"]/div/div[3]'

                time.sleep(2)

                driver.find_element_by_xpath(email_xpath).send_keys(email)
                time.sleep(0.5)
                driver.find_element_by_xpath(password_xpath).send_keys(password)
                time.sleep(0.5)
                driver.find_element_by_xpath(login_xpath).click()
                speak("instagram has been opened")
                speak("Next command sir.")
            except:
                pass


#===========Fun========================

        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "calculations" in query or "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("sir, what you want to calculate ?,example 1 plus 2")
                print("listening--------")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(operator):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.__truediv__,
                    }[operator]
            def cal(op1,oper,op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("your result is:")
            speak(cal(*(my_string.split())))

        elif "date" in query:
            speak("no")
        elif "are you single" in query or "do you have boyfriend" in query:
            speak("I am in relationship with wifi !!")
        elif "where are you" in query:
            speak("I am in front of you")
        elif "who are you" in query or "yourself" in query:
            speak("I am a Personal Virtaul Assistant (AI): \nintelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals, which involves consciousness and emotionality.")
        elif "what are you doing" in query:
            speak("I am helping you")
        elif "hello" in query or "hey" in query:
            speak("hello sir, may i help you with something.")
        elif "how are you" in query:
            speak("I am fine sir, what about you")
        elif "same here" in query or "fine" in query:
            speak("That's great to hear from you sir")
        elif "thank you" in query or "thanks" in query:
            speak("It's my pleasure sir.")
        elif "you can sleep" in query or "sleep" in query:
            speak("Okay sir, I am going to sleep you can call me anytime.")
            break
        else:
            speak("Please say the commnad again..")

#===========Main function======================
if __name__ == "__main__":
    while True:
        permission = take_command().lower()
        if "wake up" in permission:
            Task_Execution()
        elif "ok bye" in permission or "bye" in permission or "you can go" in permission:
            speak("Thanks sir for using me. Have a good day sir.")
            sys.exit()