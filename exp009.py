import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import pyjokes
import cv2
# import geocoder
import winsound
import psutil
import requests
import subprocess
import pyautogui
import speedtest
import os
import time as ti
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# import pywhatkit
from cvzone.HandTrackingModule import HandDetector
import mouse
import threading
import numpy as np
# import subprocess
import time
# import random
# import pygame
# from gtts import gTTS------used to save audio
# from googlesearch import search
import webbrowser
from forex_python.converter import CurrencyRates

# pyautogui.move(conv_x, conv_y)
# pyautogui.click(button="left")
# pyautogui.click(button="right")
# pyautogui.scroll(-1)  # Scroll down
# pyautogui.scroll(1)   # Scroll up
# pyautogui.hotkey("ctrl", "+")

# file_path = r"C:/Users/nithi/python/exp/open.mp3"
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load(file_path)          
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#    pygame.time.Clock().tick(10)
voice = pyttsx3.init()
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()


def mouse_ent():
    frameR = 100
    cam_w, cam_h = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, cam_w)
    cap.set(4, cam_h)
    detector = HandDetector(detectionCon=0.9, maxHands=1)
    l_delay = 0
    r_delay = 0
    double_delay = 0
    start = 0

    def l_clk_delay():
        global l_delay
        global l_clk_thread
        time.sleep(1)
        l_delay = 0
        l_clk_thread = threading.Thread(target=l_clk_delay)

    def r_clk_delay():
        global r_delay
        global r_clk_thread
        time.sleep(1)
        r_delay = 0
        r_clk_thread = threading.Thread(target=r_clk_delay)

    def double_clk_delay():
        global double_delay
        global double_clk_thread
        time.sleep(2)
        double_delay = 0
        double_clk_thread = threading.Thread(target=double_clk_delay)

    def clk_start():
        global start
        global clk_start_thread
        time.sleep(2)
        start = 0
        clk_start_thread = threading.Thread(target=clk_start)

    l_clk_thread = threading.Thread(target=l_clk_delay)
    r_clk_thread = threading.Thread(target=r_clk_delay)
    double_clk_thread = threading.Thread(target=double_clk_delay)
    clk_start_thread = threading.Thread(target=clk_start)

    while True:
        success, img = cap.read()
        if success:
            img = cv2.flip(img, 1)
            hands, img = detector.findHands(img, flipType=False)
            cv2.rectangle(img, (frameR, frameR), (cam_w - frameR, cam_h - frameR), (255, 0, 255), 2)
            if hands:
                lmlist = hands[0]['lmList']
                ind_x, ind_y = lmlist[8][0], lmlist[8][1]
                mid_x, mid_y = lmlist[12][0], lmlist[12][1]
                cv2.circle(img, (ind_x, ind_y), 5, (0, 255, 255), 2)
                cv2.circle(img, (mid_x, mid_y), 5, (0, 255, 255), 2)
                fingers = detector.fingersUp(hands[0])
                if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 1:
                    conv_x = int(np.interp(ind_x, (frameR, cam_w - frameR), (0, 1536)))
                    conv_y = int(np.interp(ind_y, (frameR, cam_h - frameR), (0, 864)))
                    mouse.move(conv_x, conv_y)
                    # print(conv_x, conv_y)
                if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 1:
                    mouse.click(button="right")
                if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[0] == 1:
                    mouse.click(button="left")
                if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 0 and fingers[4] == 0 and fingers[3] == 0:
                   if abs(ind_x - mid_x) > 95:
                       pyautogui.hotkey("ctrl", "+")
                   if abs(ind_x - mid_x) < 90:
                       pyautogui.hotkey("ctrl", "-")
                if fingers[1] == 0 and fingers[2] == 0 and fingers[0] == 0 and fingers[4] == 0:
                    # if abs(ind_x - mid_x) < 25:
                    mouse.wheel(delta=-1)
                if fingers[1] == 0 and fingers[2] == 0 and fingers[0] == 1 and fingers[4] == 1:
                    # if abs(ind_x - mid_x) < 25:
                    mouse.wheel(delta=1)
                # Double Mouse Click
                # if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 0 and fingers[4] == 0 and double_delay == 0:
                #     double_delay = 1
                #     mouse.double_click(button="left")
                #     double_clk_thread.start()
                if fingers[1] == 0 and fingers[2] == 0 and fingers[0] == 1 and fingers[4] == 0 and fingers[3] == 0:
                    cv2.destroyAllWindows()
                    main()
                    # continue
                    # clk_start_thread.start()
            cv2.imshow("Camera Feed", img)
            cv2.waitKey(1)


name = "nithin"  # change this with SQL


def talk(text):
    voice.say(text)
    voice.runAndWait()


def start_intro():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        talk("Good Morning,")  # add name
    elif hour > 12 and hour <= 18:
        talk("Good Afternoon ")
    else:
        talk("Good Evening")
    talk("hello " + name + ", how can i help you today")


# def wait_for(time):
#     sec=time*60
#     time.sleep(sec)
#     main()
# def opened_app():
x = 1


def capture_voice_input():
    with sr.Microphone() as source:
        # if x == 1:
        #     start_intro()
        #     x=x+1
        print("Speak now..........")
        # print("\U0001F3A4")
        audio = recognizer.listen(source)
    return audio


def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.check microphone and try again")
        # file_path = r"C:/Users/nithi/python/exp/close.mp3"
        # pygame.init()
        # pygame.mixer.init()
        # pygame.mixer.music.load(file_path)
        # pygame.mixer.music.play()
        # while pygame.mixer.music.get_busy():
        #     pygame.time.Clock().tick(10)
        # exit()
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text


def speakout(text):
    voice.setProperty('rate', 130)
    nithin = text.lower()
    if 'name' in nithin:
        speak = talk("My name is pluto")
    elif 'my name' in nithin:
        speak = talk("your name is " + name)  # initilize name if want_______
    elif 'what can you do' in nithin:
        speak = talk(
            "I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, take photos, open google browser,and I can search for some thing in google and I can tell jokes")
    elif 'date' in nithin:
        speak = talk('Sorry not intreseted, I am having headache, we will catch up some other time')
    elif 'are you single' in nithin:
        speak = talk('No, I am in a relationship with wifi')
    elif 'are you there' in nithin:
        speak = talk('Yes, I am here')
    elif 'tell me something' in nithin:
        speak = talk(' I don\'t have much to say, you only tell me someting i will give you the company')
    elif 'thank you' in nithin:
        speak = talk(' I am here to help you..., your welcome')
        speak = talk("I can only shutdown if you say close or shutdown or turn off")
    elif 'your free time' in nithin:
        speak = talk(' I will be listening to all your words')
    elif 'i love you' in nithin:
        speak = talk('I love you too ')
    elif 'can you hear me' in nithin:
        speak = talk('Yes, I can hear you')
    elif ('do you ever get tired' in nithin) or ("are you tired" in nithin):
        speak = talk('It would be impossible to tire of our conversation')
    elif ("hello" in nithin) or ("hi" in nithin) or ("hey" in nithin):
        speak = talk("hello how can i help you")
    elif ("bye" in nithin) or ("turn off" in nithin) or ("shut down" in nithin) or ("close" in nithin):
        speak = talk("i am glad for helping you")
        exit()
    elif ("date" in nithin) or ("time" in nithin) or ("date and time" in nithin):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Formatted date and time: {formatted_datetime}")
        voice.say(formatted_datetime)
        voice.runAndWait()
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            speak = talk("today is " + day_of_the_week)
    elif ("photo" in nithin) or ("selfie" in nithin) or ("snap" in nithin):
        voices = voice.getProperty('voices')
        voice.setProperty('voice', voices[1].id)
        speak = talk("sayyy cheeseeee")
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            exit()  # 3 exits to speek
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            exit()
        image_dir = r"C:/Users/nithi/python/exp"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{image_dir}/{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        cap.release()
        cv2.imshow('Image', filename)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        speak = talk("Image captured and saved as image")
    elif ("tell me a joke" in nithin) or ("tell a joke" in nithin) or ("tell joke" in nithin):
        voice.setProperty('rate', 120)
        speak = talk(pyjokes.get_joke())
    elif ("fuck" in nithin) or ("fuck off" in nithin) or ("bitch" in nithin):
        speak = talk("this words are not in my dictionary")
        exit()
    # elif ("what is your age" in nithin) or ("your age" in nithin):
    #     speak = talk(
    #         "Age is but a measure of the time one has journeyed around the sun, marking the accumulation of experiences, wisdom, and the relentless passage of moments")
    elif ("find my location" in nithin) or ("location" in nithin) or ("where am i" in nithin):
        speak = talk("you are redirecting to maps with current ip adress")
        response_ip = requests.get('https://api.ipify.org?format=json')
        current_ip = response_ip.json()['ip']
        response_location = requests.get(f'https://ipinfo.io/{current_ip}/json')
        location_data = response_location.json()
        latitude, longitude = location_data['loc'].split(',')
        maps_link = f'https://www.google.com/maps/search/?api=1&query={latitude},{longitude}'
        driver = webdriver.Chrome()
        driver.get(maps_link)
        speak = talk("maps has been opened sucessfully")
        ti.sleep(17)
        main()
    elif ("calculate currency" in nithin) or ("covert currency" in nithin) or ("convert money" in nithin):
        speak1 = "Enter the amount to convert"
        voice.say(speak1)
        voice.runAndWait()
        amount = float(input("Amount : "))
        speak2 = "enter country currency code you have"
        voice.say(speak2)
        voice.runAndWait()
        from_currency = input("(e.g., USD,EUR,INR): ").upper()
        speak3 = "enter country currency code you want to change"
        voice.say(speak3)
        voice.runAndWait()
        to_currency = input("(e.g., USD,EUR,INR): ").upper()
        c = CurrencyRates()
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        speak4 = "amount is", to_currency
        voice.say(speak4)
        voice.runAndWait()
    elif ("speaker check" in nithin) or ("make a sound" in nithin) or ("sound check" in nithin):
        winsound.Beep(1000, 5000)
    elif ("day" in nithin):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            speak = talk("today is " + day_of_the_week)
    # elif("play music" or "music" or "play songs" or "songs" or "play a song"):                                              #selenium
    #         file_path = r"C:\Users\nithi\OneDrive\Desktop\python\exp\Badass.mp3"
    #         try:
    #             pygame.init()
    #             pygame.mixer.init()
    #             pygame.mixer.music.load(file_path)
    #             pygame.mixer.music.play()
    #             while pygame.mixer.music.get_busy():
    #               pygame.time.Clock().tick(10)
    #         except KeyboardInterrupt:
    #               pass
    elif ("female voice" in nithin) or ("change to female voice" in nithin):
        voices = voice.getProperty('voices')
        voice.setProperty('voice', voices[1].id)
        speak = talk("changed to female voice")
        return True
    elif ("male voice" in nithin) or ("change to male voice" in nithin):
        voices = voice.getProperty('voices')
        voice.setProperty('voice', voices[0].id)
        speak = talk("changed to male voice")
        return False
    elif ("set timer" in nithin) or ("set alarm" in nithin):  # check_________|
        speak = talk("enter minutes to set timer")
        minutes = int(input("enter time in minutes to set....."))
        seconds = minutes * 60
        print(f"Timer set for {minutes} minutes.")
        winsound.Beep(1000, 1000)
        ti.sleep(seconds)
        print("Time's up!")
        winsound.Beep(1000, 5000)
    elif ("i hate you" in nithin):
        speak = talk("i don't have any feelings but i love speeking with people")
    elif ("gmail" in nithin):
        talk('opening your google gmail')
        webbrowser.open('https://mail.google.com/mail/')
        talk("opened sucessfuly")
    elif ("news" in nithin):
        talk('opening google news')
        webbrowser.open('https://news.google.com/')
        talk("opened sucessfuly")
    elif ("calender" in nithin):
        talk('opening google calender')
        webbrowser.open('https://calendar.google.com/calendar/')
        talk("opened sucessfuly")
    elif ("photos" in nithin):
        talk('opening your google photos')
        webbrowser.open('https://photos.google.com/')
        talk("opened sucessfuly")
    elif ("document" in nithin):
        talk('opening your google documents')
        webbrowser.open('https://docs.google.com/document/')
        talk("opened sucessfuly")
    elif ("spreadsheet" in nithin):
        talk('opening your google spreadsheet')
        webbrowser.open('https://docs.google.com/spreadsheets/')
        talk("opened sucessfuly")

    elif ("weather" in nithin) or ("temperature" in nithin):
        speak = talk("you are redirecting to weather page")                             # add mouse for all this below and 7 above*******
        webbrowser.open('https:accuweather.com')
        talk("enter how much time you would like to use this")
        time = int(input("enter in minute :"))
        sec = time * 60
        ti.sleep(sec)
        winsound.Beep(1000, 1000)
        main()
        mouse_ent()
    elif (("open instagram" or "instagram" or "open insta") in nithin):
        speak = talk("you are redirecting to instagram page")
        webbrowser.open('https:instagram.com')
        speak = talk("instagram has been opened sucessfully")
        talk("enter how much time you would like to use instagram")
        time = int(input("enter in minute :"))
        sec = time * 60
        ti.sleep(sec)
        winsound.Beep(1000, 1000)
        main()
        mouse_ent()
    elif (("open maps" or "open gps" or "open google maps" or "google maps") in nithin):
        speak = talk("you are redirecting to maps")
        webbrowser.open('https://www.google.com/maps')
        ti.sleep(5)
        speak = talk("maps has been opened sucessfully")
        talk("you are enabled to use mouse")                                    # add mouse function:and also other social applications
        ti.sleep(10)                                                              # add pyautogui
        mouse_ent()
    elif (("open youtube normally") in nithin):                                    # check4444444444
        speak = talk("you are redirecting to youtube")
        webbrowser.open('https://www.youtube.com')
        speak = talk("youtube has been opened sucessfully")
        talk("enter how much time you want to keep this window awake")
        time = int(input("enter in minute :"))
        sec = time * 60
        ti.sleep(sec)
        winsound.Beep(1000, 1000)
        main()
        mouse_ent()
    elif (("open youtube") in nithin):
        speak = talk("you are redirecting to youtube")
        driver = webdriver.Chrome()
        driver.get("https://www.youtube.com/")
        speak = talk("youtube has been opened sucessfully")

        talk("tell me what would you like to search")
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)

        search_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#container.ytd-searchbox>[slot=search-input] input")))
        search_input.send_keys(text)
        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#search-icon-legacy.ytd-searchbox ")))
        search_button.click()
        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#video-title.ytd-video-renderer")))
        search_button.click()
        talk("enter time to keep this environment awake")
        time = int(input("enter in minute :"))
        sec = time * 60
        ti.sleep(sec)
        winsound.Beep(1000, 1000)
        main()
        # talk(" can you please say the name to search")                                   # choose one @@@@@@@@@@@@@@@@@@@
        # song = convert_voice_input()
        # if "play" in song:                                                               # pywhatkit.playonyt(song)
        #     song = song.replace("play","")
        # speak=talk('playing '+song)
        # pywhatkit.playonyt(song)

        # speak("This is what I found for your search!") 
        # query = query.replace("youtube search","")
        # query = query.replace("youtube","")
        # query = query.replace("jarvis","")
        # web  = "https://www.youtube.com/results?search_query=" + query
        # webbrowser.open(web)
        # pywhatkit.playonyt(query)
    elif (("open twitter") in nithin):
        speak = talk("you are redirecting to twitter")  # add mouse function:and also other social applications
        webbrowser.open('https://www.twitter.com')
        ti.sleep(10)
        # print(" ")
        speak = talk("twitter has been opened sucessfully")
        talk("enter time to put me in sleep")
        time = int(input("enter in minute :"))
        mouse_ent()
        sec = time * 60
        ti.sleep(sec)
        winsound.Beep(1000, 1000)
        speak = talk("i am back")
        main()
        
    elif (("open google") in nithin):
        talk("in any case if you want mouse ")                                # add mouse function:and also other social applications
        speak = talk("now you are redirecting to google")
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        speak = talk("google  has been opened sucessfully")
        speak = talk("what do you want to search for ")
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        search_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.gLFyf")))
        search_input.send_keys(text)
        search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wM6W7d span")))
        search_button.click()
        talk("from now you can use mouse")
        mouse_ent()
    elif("chrome" or "google") in nithin:
        speak = talk("you are redirecting to google")  # add mouse function:and also other social applications
        subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'])
        ti.sleep(10)     
        talk("Google Chrome opened successfully!")
        ti.sleep(2)
        talk("enter time to put me in sleep")
        time = int(input("enter in minute :"))
        mouse_ent()
        sec = time * 60
        ti.sleep(sec)
        winsound.Beep(1000, 1000)
        speak = talk("i am back")
        main()
    elif (("wait" or "pause") in nithin):
        speak = talk("enter how much time you would you like to suspend me in minutes")
        time = int(input("enter in minute :"))
        sec = time * 60
        ti.sleep(sec)
        winsound.Beep(1000, 1000)
        speak = talk("i am back")
        main()
    elif ("close chrome" in nithin):
        os.system("C:\Program Files\Google\Chrome\Application\chrome.exe")
        speak = talk("chrome has been closed successfully")
        talk("if you want to close me say shut down or bye")
        main()
    elif ("close all" in nithin) or ("close all tabs" in nithin):
        talk("are sure to close all tabs for conformations say again")
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        if ("close all tabs" in text) or ("yes" in text):
            for proc in psutil.process_iter():
                proc.terminate()
        else:
            speakout(text)
    elif ("screenshot" or "screen shot") in nithin:
        talk("screen shot will be taken in 5 seconds")
        ti.sleep(5)
        talk("Please boss hold the screen for few seconds, I am taking screenshot")
        img = pyautogui.screenshot()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        img.save(f"{timestamp}.png")
        talk("I am done, the screenshot is saved in main folder.")
        main()
    elif ("calculator") in nithin:
        talk('Opening calculator')
        os.startfile('C:\Windows\System32\calc.exe')
        talk("calculator opened sucessfully")
        main()
    elif (("record " or "record video") in nithin):
        talk("get ready video capturing will start in 3 seconds and to stop enter ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        image_dir = "C:/Users/nithi/python/exp"
        filename = f"{image_dir}/{timestamp}.avi"
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))                                       # first try  # check
        cap = cv2.VideoCapture(0)
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                out.write(frame)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    elif "internet speed" in nithin:
        wifi = speedtest.Speedtest()
        upload_net = wifi.upload() / 1048576                                                      # Megabyte = 1024*1024 Bytes
        download_net = wifi.download() / 1048576
        print("Wifi Upload Speed is", upload_net)
        print("Wifi download speed is ", download_net)
        talk(f"Wifi download speed is {download_net}")
        talk(f"Wifi Upload speed is {upload_net}")
    elif "spotify" in nithin:
        spotify_exe_path = "C:/Users/nithi/AppData/Local/Microsoft/WindowsApps/Spotify.exe"
        playlist_uri = "https://open.spotify.com/track/7MXVkk9YMctZqd1Srtv4MB?si=a505d01d91a14e98"
        webbrowser.open(playlist_uri)
        mouse_ent()
    elif("who is" or "what is" or "tell me about" or "tell") in nithin:
        nithin = nithin.replace("who is", "")
        nithin = nithin.replace("what is", "")
        nithin = nithin.replace("tell me about", "")
        nithin = nithin.replace("tell", "")
        driver = webdriver.Chrome()
        driver.get("https://www.wikipedia.org")
        search_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchInput ")))
        search_input.send_keys(nithin)
        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-container button ")))
        search_button.click()
        speak = talk(wikipedia.summary(nithin, sentences=2))
        ti.sleep(20)
    elif("mouse" in nithin ):
        mouse_ent()




    else:
        talk("sorry that your command has been missing we will add it soon")
        speak = nithin
        # In = text
        # speak = talk(wikipedia.summary(In, sentences=2))
        # print(result)
        # speak=talk("we dont't have that much information soon we will add"


def main():
    end_program = False
    start_intro()
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        # end_program = speakout(text)
        end_program = speakout(text)
        if end_program == True:
            voice = pyttsx3.init()
            voices = voice.getProperty('voices')
            voice.setProperty('voice', voices[1].id)
        if end_program == False:
            voice = pyttsx3.init()
            voices = voice.getProperty('voices')
            voice.setProperty('voice', voices[0].id)
        end_program = False

main()
