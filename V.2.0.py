import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import numpy as np 
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import multiprocessing
import time
import cv2
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
	engine.say(audio)
	engine.runAndWait()
	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

def video():

	while True:
		#This is to check whether to break the first loop
		isclosed=0
		cap = cv2.VideoCapture('sirilike.gif')
		while (True):

			ret, frame = cap.read()
			# It should only show the frame when the ret is true
			if ret == True:
				cv2.imshow('frame',frame)
				if cv2.waitKey(12) == 27:
					# When esc is pressed isclosed is 1
					isclosed=1
					break
			else:
				break
		# To break the loop if it is closed manually
		if isclosed:
			break
	cap.release()
	cv2.destroyAllWindows()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 5 and hour<12:
		speak("Good Morning Sir !")
	elif hour>= 0 and hour<5:
		speak("Good Evening Sir! Maybe you should be sleeping?")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("V 2 point o")
	speak("I am your Assistant")
	speak(assname)
	

def usrname():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

def sendEmail(email_id,email_password,to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login(email_id , email_password)
	server.sendmail(email_id, to, content)
	server.close()

def comm():

	while True:
		
		query = takeCommand().lower()
		
		# All the commands said by user will be
		# stored here in 'query' and will be
		# converted to lower case for easily
		# recognition of command
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.get('chrome').open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.get('chrome').open("google.com")

		elif 'open instagram' in query:
			speak("Here you go to Instagram\n")
			webbrowser.get('chrome').open("instagram.com")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.get('chrome').open("stackoverflow.com")

		elif 'open' and 'in browser' in query:
			speak("Here you go to requested site\n")
			query = query.replace('open ', "")
			query = query.replace(' in browser', "")
			webbrowser.get('chrome').open(query+".com")

		elif 'play music' in query or "play song" in query:
			speak("What streaming service do you prefer Spotify , Youtube or Local Storage")
			# music_dir = "G:\\Song"
			#music_dir = "C:\\Users\\Administartor\\Music"
			#songs = os.listdir(music_dir)
			#print(songs)
			#random = os.startfile(os.path.join(music_dir, songs[1]))
			choice=takeCommand()
			if "spotify" or "Spotify" in choice:
					webbrowser.get('chrome').open("https://open.spotify.com/")
			elif "youtube" or "Youtube" in choice:
					webbrowser.get('chrome').open("youtube.com")
			else:
				music_dir = "C:\\Users\\Administartor\\Music"
				songs = os.listdir(music_dir)
				print(songs)
				random = os.startfile(os.path.join(music_dir, songs[1]))


		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H %M %S")
			speak(f"Sir, the time is {strTime}")

		elif 'open opera' in query:
			#use what is necessary for your pc
			codePath = r"C:\\Users\\Administrator\\AppData\\Local\\Programs\\Opera\\launcher.exe"
			os.startfile(codePath)

		elif 'send a mail' in query:
			try:
				speak("Enter your email_id")
				email_id=input()
				speak("Enter your password")
				email_password=input()
				speak("What should I say?")
				content = takeCommand()
				speak("whom should i send it to")
				to = input()
				sendEmail(email_id,email_password,to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by Godizon.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			
		elif "calculate" in query:
			
			app_id = "Wolframalpha api id"
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate')
			query = query.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			print("The answer is " + answer)
			speak("The answer is " + answer)

		#elif 'search' in query or 'play' in query:
			
			#query = query.replace("search", "")
			#query = query.replace("play", "")		
			#webbrowser.open(query)
			#print("hello")
			#webbrowser.get('windows-default').open("http://google.com/?#q="+query)

		elif "who i am" in query:
			speak("If you talk then definately your human.")

		elif "why you came to world" in query:
			speak("To Serve")

		elif 'power point presentation' in query:
			speak("opening Power Point presentation")
			power = r"file location"
			os.startfile(power)

		elif 'what is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant created by godizon")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by godizon ")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"Location of wallpaper",
													0)
			speak("Background changed succesfully")

		elif 'open bluestack' in query:
			appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
			os.startfile(appli)

		elif 'news' in query:
			
			try:
				jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
				data = json.load(jsonObj)
				i = 1
				
				speak('here are some top news from the times of india')
				print('''=============== TIMES OF INDIA ============'''+ '\n')
				
				for item in data['articles']:
					
					print(str(i) + '. ' + item['title'] + '\n')
					print(item['description'] + '\n')
					speak(str(i) + '. ' + item['title'] + '\n')
					i += 1
			except Exception as e:
				
				print(str(e))

		
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time do you want to stop me from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.com / maps / place/" + location + "")

		elif "camera" in query or "take a photo" in query:
			ec.capture(0, "V Camera ", "img.jpg")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('v.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = str(datetime.datetime.now())
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("v.txt", "r")
			print(file.read())
			speak(file.read(6))

		elif "update assistant" in query:
			speak("After downloading file please replace this file with the downloaded one")
			url = '# url after uploading file'
			r = requests.get(url, stream = True)
			
			with open("Voice.py", "wb") as Pypdf:
				
				total_length = int(r.headers.get('content-length'))
				
				for ch in progress.bar(r.iter_content(chunk_size = 2391975),
									expected_size =(total_length / 1024) + 1):
					if ch:
					 Pypdf.write(ch)
					
		elif "V " in query:
			
			wishMe()
			speak("V 2 point o in your service Mister")
			speak(assname)

		elif "weather" in query:
			
			# Google Open weather website
			# to get API of Open weather
			api_key = "Api key"
			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
			speak(" City name ")
			print("City name : ")
			city_name = takeCommand()
			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
			response = requests.get(complete_url)
			x = response.json()
			
			if x["cod"] != "404":
				y = x["main"]
				current_temperature = y["temp"]
				current_pressure = y["pressure"]
				current_humidiy = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
			
			else:
				speak(" City Not Found ")
			
		elif "send message " in query:
				# You need to create an account on Twilio to use this service
				account_sid = 'Account Sid key'
				auth_token = 'Auth token'
				client = Client(account_sid, auth_token)

				message = client.messages \
								.create(
									body = takeCommand(),
									from_='Sender No',
									to ='Receiver No'
								)

				print(message.sid)

		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query:
			speak("I'm not sure about that, may be you should give me some more time")

		elif "how are you" in query:
			speak("I'm fine, glad you asked me that")

		elif "i love you" in query:
			speak("It's too hard for me to comprehend the significance of such words")

		elif "what is" in query or "who is" in query:
			
			# Use the same API key
			# that we have generated earlier
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

		# elif "" in query:
			# Command go here
			# For adding more commands
if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	p1 = multiprocessing.Process(name='p1', target=video)
	p = multiprocessing.Process(name='p1', target=wishMe)
	p3 = multiprocessing.Process(name='p1', target=usrname)
	p4 = multiprocessing.Process(name='p1', target=comm)
	p1.start()
	p.start()
	p.join()
	p3.start()
	p3.join()
	p4.start()
	p4.join()
