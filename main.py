import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import datetime
import smtplib
import pyjokes
import ctypes
import random
import time
import cv2
import requests
import subprocess
import winshell




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

assname = 'Ghost'


def search_web(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def take_photo():
    
    ctime = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    path = "./captured_images/img_" + ctime + ".jpg"
    assistant_speaks("I am taking a picture")
            
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    if not camera.isOpened():
        assistant_speaks("Unable to open the camera")
        return
    ret, frame = camera.read()
    if not ret:
        assistant_speaks("Failed to capture frame")
        return
    # frame = cv2.detailEnhance(frame, sigma_s=10, sigma_r=0.15)
    cv2.imwrite(path, frame)
    cv2.imshow("Captured Photo", frame)
    camera.release()
    
    assistant_speaks("Photo captured! Press any key to close the window.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_weather(query):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    api_key = 'API KEY'

    if "here" in query:
        response = requests.get("https://ipapi.co/json/")
        location_data = response.json()
        city_name = location_data["city"]
    else:
        assistant_speaks("City name ")
        city_name = get_audio()

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = round((y['temp'])-273)
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]  
        z = x["weather"]
        weather_description = z[0]["description"]
        return {
            "city":city_name,
            "temperature": current_temperature,
            "pressure": current_pressure,
            "humidity": current_humidity,
            "description": weather_description
        }
    else:
        return None

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        assistant_speaks("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        assistant_speaks("Good Afternoon Sir !")

    else:
        assistant_speaks("Good Evening Sir !")

    assistant_speaks("Ghost is at your service!")


def assistant_speaks(text):
    print("Ghost: ", text)
    engine.say(text)
    engine.runAndWait()


def get_audio():

    audio = ''
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Ghost: Listening...")
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Ghost: Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You : {query}\n")

    except Exception as e:
        print(e)
        print("Ghost: Unable to Recognize your voice.")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


def tellTime():
    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]
    assistant_speaks("The time is " + hour + " Hours and " + min + " Minutes")


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        assistant_speaks("Today is " + day_of_the_week)


def pick_random_file(folder_path):
    files = os.listdir(folder_path)
    if len(files) == 0:
        print("Folder is empty.")
        return None

    random_file = random.choice(files)
    return os.path.join(folder_path, random_file)


def search_web(input):

    if 'youtube' in input.lower():

        assistant_speaks("Opening in youtube")
        query = input.replace("play", "").replace("on YouTube", "").strip()
        search_url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(search_url)
        return

    elif 'wikipedia' in input.lower():
        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        search_url = f"https://en.wikipedia.org/wiki/" + '_'.join(query)
        webbrowser.open(search_url)
        return

    else:

        if 'google' in input:

            query = input.replace("google", "").strip()
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)

        elif 'search' in input:

            query = input.replace("search", "").strip()
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)

        else:

            query = input.replace("", "").strip()
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
        return


def open_application(input):

    if "chrome" in input:
        assistant_speaks("Google Chrome")
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        return

    elif "vs code" in input or "code" in input:
        assistant_speaks("Opening Microsoft Visual Studio Code")
        os.startfile(
            r'C:\Users\deeps\AppData\Local\Programs\Microsoft VS Code\Code.exe')

    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return

    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile(
            r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
        return

    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile(
            r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
        return

    elif "file explorer" in input or "file manegar" in input:
        assistant_speaks("Opening File Explorer")
        os.startfile(r"C:\Users\deeps\Desktop")

    else:
        assistant_speaks("Application not available")
        return


def process_text(input):
    try:
        if 'search' in input or 'play' in input:
            search_web(input)
            return

        elif 'time now' in input or 'time right now' in input:
            tellTime()
            return

        elif 'what day it is' in input or 'which day it is' in input:
            tellDay()
            return

        elif "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am Python Program. Your personal Assistant.
			I am here to make your life easier. You can command me to perform
			various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak)
            return

        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Deep Senchowa."
            assistant_speaks(speak)
            return

        elif 'open' in input:
            open_application(input.lower())
            return

        elif 'send an email' in input or 'write an email' in input:
            try:
                assistant_speaks("What should I say?")
                content = get_audio()
                assistant_speaks("whome should i send")
                to = input()
                sendEmail(to, content)
                assistant_speaks("Email has been sent !")
                return
            except Exception as e:
                print(e)
                assistant_speaks("I am not able to send this email")
                return

        elif "what's your name" in input or "What is your name" in input:
            assistant_speaks("My friends call me")
            assistant_speaks(assname)
            print("Ghost: My friends call me", assname)
            return

        elif 'joke' in input:
            assistant_speaks(pyjokes.get_joke())
            return

        elif 'change background' in input:
            folder_path = r"C:\Users\deeps\Pictures\wallpaper"
            random_file_path = pick_random_file(folder_path)
            if random_file_path:
                ctypes.windll.user32.SystemParametersInfoW(
                    20, 0, random_file_path, 0)
                assistant_speaks("Background changed successfully")
                return
            else:
                assistant_speaks("Background changing unsuccessfull")
                return
            
        elif 'shutdown system' in input:
                assistant_speaks("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                return
                
        elif "restart" in input:
            subprocess.call(["shutdown", "/r"])
            return
        
        elif 'lock window' in input:
                assistant_speaks("locking the device")
                ctypes.windll.user32.LockWorkStation()
                return
        
        elif "restart" in input:
            subprocess.call(["shutdown", "/r"])
            return
             
        elif "hibernate" in input or "sleep" in input:
            assistant_speaks("Hibernating")
            subprocess.call("shutdown /h")
            return
 
        elif "log off" in input or "sign out" in input:
            assistant_speaks("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown /l"])
            return
 
        elif "write a note" in input:
            assistant_speaks("What should i write, sir")
            note = get_audio()
            file = open('Ghost.txt', 'w')
            assistant_speaks("Sir, Should i include date and time")
            snfm = get_audio()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                return
            else:
                file.write(note)
                return
                
        elif "show my notes" in input:
            assistant_speaks("Showing Notes")
            file = open("Ghost.txt", "r")
            print(file.read())
            assistant_speaks(file.read(6))
            return
            
        elif 'is love' in input:
            assistant_speaks("It is 7th sense that destroy all other senses")
            return
                
        elif "click a photo" or "take a picture" in input or "take a photo" in input:
            take_photo()
            return
                
        elif "where is " in input:
            query = input.replace("where is", "")
            location = query
            assistant_speaks("You asked to Locate")
            assistant_speaks(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            return

        elif 'empty recycle bin' in input:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            assistant_speaks("Recycle Bin Recycled") 
            return
            
        elif "weather" in input:
            weather_data  =  get_weather(input)
            if weather_data is not None:
                data = "Weather today in "+ weather_data["city"] +" is "+ weather_data["description"]+"\nTemperature (in celsius) is "+ str(weather_data["temperature"]) + "\nAtmospheric pressure (in hPa) is "+ str(weather_data["pressure"])+"\nHumidity (in percentage) is "+ str(weather_data["humidity"])
                assistant_speaks(data)
                return
            else:
                assistant_speaks(" City Not Found ")
                return
                
        
        else:
            assistant_speaks(
                "I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
                return
            else:
                return
    except:

        assistant_speaks(
            "I don't understand")
        return

# Driver Code
if __name__ == "__main__":
    name = 'Mr. Deep'
    wishMe()
    assistant_speaks("What can i do for you, Sir?")
    text = get_audio().lower()

    process_text(text)

    while True:
        assistant_speaks("What else can i do for you?")
        text = get_audio().lower()

        if text == 0:
            continue

        if 'exit' in text:
            assistant_speaks("Thanks for giving me your time")
            exit()

        process_text(text)
