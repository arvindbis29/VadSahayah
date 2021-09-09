import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import matplotlib.pyplot as plt
from os import environ
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', 'english+f2')
engine.say('hello arvind how are you ')
engine.say('i am your personal alexa')
engine.say('what can I do for you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.........')
            voice = listener.listen(source, phrase_time_limit=3)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('current time is ' + time)
        print(time)
    elif 'who the hell is' in command:
        person = command.replace('who the hell is', '')
        # pywhatkit.info(person)
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'tell me about yourself' in command:
        talk('namaste arvind, i am your voice assistant, i created in python, i can play songs, tell about time, search on google ,create graph, and also send message on whatapp.   ')
 
    elif 'joke' in command:
        my_joke = (pyjokes.get_joke(language="en", category="neutral"))
        print(my_joke)
        talk(my_joke)
    elif 'rest' in command:
        talk('ok  bye bye arvind , i miss you')
        quit()
    elif 'graph' in command:
        talk('hey arvind give the x axis value')
        x = [0, 0, 0, 0]
        for i in range(0, 4):
            ele = int(input())
            x.append(ele)  # adding the element
        talk('hey give me y axis value')
        y = [0, 0, 0, 0]
        for i in range(0, 4):
            ele = int(input())
            y.append(ele)
        # plotting the points
        plt.plot(x, y)
        # nameing the x axis
        plt.xlabel('x-axis')
        # nameing the y axis
        plt.ylabel('y- axis')
        # giving a title to my graph
        talk('your graph is ready ')
        plt.title('graph create by alexa')
        # function for show the plot
        plt.show()
    elif 'search' in command:
        search = command.replace('search', '')
        pywhatkit.search(search)
        talk('i am searching at chrome' + search)
        # tabUrl = "http://google.com/search?q="
        # webbrowser.open(tabUrl+search, new=2)
    elif 'whatsapp' in command:
        msj = command.replace('i want to send message on whatsapp', '')
        pywhatkit.sendwhatmsg('+916375811373', msj, 16, 15)
        talk('i am sending message on whatsapp' + msj)
    else:
        talk('please, say the command again.')


while True:
    run_alexa()
