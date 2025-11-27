#program to text to speech

import pyttsx3
text = input("Enter the name of the song you wmnat to play:- ")

speaker = pyttsx3.init()
speaker.say({text})
speaker.runAndWait()
