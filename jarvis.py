import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pygame
from pygame.locals import *
import time
import pygame_widgets as pw
pygame.init()
green=(8,110,39)
def text(text,color,x,y):
        screen_text=font.render(text,True,color)
        display.blit(screen_text,(x,y))
font=pygame.font.SysFont(None,40)
width=800
height=600
display=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
background=pygame.image.load('C:\\Users\\Asus\\Downloads\\jarvis.jpg')
pygame.display.update()

pygame.display.set_caption('Jarvis (AI) version 1.0')
jarvis=pygame.image.load('C:\\Users\\Asus\\Downloads\\maxresdefault-removebg-preview.png')
terminal=pygame.image.load('C:\\Users\\Asus\\Downloads\\hacker.jpg')

        
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
        engine.say(audio)
        engine.runAndWait()
def welcome():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
                speak('good morning commander!')
        elif hour>=12 and hour<18:
                speak('good afternoone commander!')
        else:
                speak('good evening commander!')
        speak('i am jarvis sir may i help you')

def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print('listening....')
                r.pause_threshold=1
                audio=r.listen(source)
        try:
                print('recognizing')
                query=r.recognize_google(audio,language='en-in')
                print(f'user said : {query}')

        except Exception as e:
                print('can you say again')
                return'None'
        return query
def mainloop():
        if __name__=='__main__':
                welcome()
                query=takecommand().lower()
                if 'good morning'in query:
                        speak('good morning commander have a nice day')

                elif 'wikipedia'in query:
                        speak('searching wikipedia')
                        query=query.replace('wikipedia','')
                        result=wikipedia.summary(query,2)
                        text(result,green,0,400)
                        speak(result)
                elif 'open youtube'in query:
                        webbrowser.open('https://www.youtube.com')
                elif 'open google'in query:
                        webbrowser.open('https://www.google.com')
                        
                elif 'open facebook'in query:
                        webbrowser.open('https://www.facebook.com')
                elif 'open twitter'in query:
                        webbrowser.open('https://www.twitter.com')
button=pw.Button(display,393,460,60,90,text="Init(:)",fontsize=3,margin=20,inactivecolor=(50,50,50),pressedcolor=(255,255,255),radius=150,onClick=lambda:mainloop())
              
while True:
      display.blit(pygame.transform.scale(background,(800,600)),(0,0))
      display.blit(pygame.transform.scale(terminal,(200,200)),(0,400))
      display.blit(pygame.transform.scale(jarvis,(500,500)),(180,100))

      pygame.display.update()
      event=pygame.event.get()
      for event in event:
        if event.type==QUIT:
                quit()
                sys.exit()
                display.update()
      button.listen(event)
      button.draw()
      pygame.display.update()  


      clock.tick(5)





