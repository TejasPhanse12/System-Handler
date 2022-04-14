
from typing import Dict
import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import os
import smtplib
import cv2
import requests
import pywhatkit as kit
import sys
from playsound import playsound
import pyjokes
import pyautogui
import requests
import operator
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
from tkinter import Text
from datetime import date
import calendar
from time import strftime
from tkinter import INSERT
from tkinter import Label


email = {"angad singh obbi":"obbiangad@kccemsr.edu.in",
		 "atharva mulgund":"mulgundatharva@kccemsr.edu.in",
		 "durgesh khole":"kholedurgesh@kccemsr.edu.in",
		 "mrunmai patil":"patilmrunmai@kccemsr.edu.in",
		 "baliram pansare":"pansarebaliram@kccemsr.edu.in",
		 "tejas phanse": "phansetejas@kccemsr.edu.in"}
		 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
Time = datetime.datetime.now()
alarm =0


def speak(speakup):
	engine.say(speakup)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if(hour>=0 and hour<12):
		speak("Very Good Morning")
		print("Good Morning")
		Time = datetime.datetime.now().strftime("%H:%M:%S")
		print(Time,"AM")
		speak(f"the time is {Time} AM")
	elif (hour>=12 and hour <18):
		speak("Good Afternoon")
		print("Good Afternoon")
		Time = datetime.datetime.now().strftime("%H:%M:%S")
		print(Time, "PM")
		speak(f"the time is {Time} PM")
	else:
		speak("Good Evening, I hope you had a great day")
		print("Good Evening, I hope you had a great day")
		Time = datetime.datetime.now().strftime("%H:%M:%S")
		print(Time, "PM")
		speak(f"the time is {Time} PM")
	
	speak("I'm Tron!! Putting All Systems Online")

def takeCommand():
	speak("Over To you sir......")
	Time = int(datetime.datetime.now().strftime("%H%M"))
	if(Time == alarm):
		for al in range(0,5):
			speak("It's time to wake")
			playsound('C:\\Users\\tejas\\Downloads\\track1.wav')
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source,phrase_time_limit=5)
	try:
		print("Recognizing...")    
		query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
		print(f"-> {query}\n")  #User query will be printed.
	except Exception as e:
		speak("Sorry sir... say that again please!!!")
		#print(e)    
		print("Say that again please...")   #Say that again will be printed in case of improper voice 
		return "None" #None string will be returned
	return query
	
def sendEmail(to,content):
	psw = open("D:\\clg stuff\\python prog\\internship\\password.txt")
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('tejas.phanse1205@gmail.com', psw.read())
	server.sendmail('tejas.phanse1205@gmail.com', to, content)
	server.close()
	psw.close()
	
def news():
	main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=dbdd1756283b4343a4fac485ea83ac6d"
	main_page = requests.get(main_url).json
	articles = main_page["articles"]
	head = []
	for ar in articles:
		head.append(ar[title])
	speak("todays top headlines are...")
	for i in range(0,10):
		speak(head[i])
	
if __name__ == "__main__":
	wishMe()
	
	a = True
	
	while a == True:
		query = takeCommand().lower()
#----------------------------WIKIPEDIA-------------------------------------
		if 'wikipedia' in query:
			speak("Searching in Wikipedia...")
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=3)
			speak("According to Wikipedia")
			print(results)
			speak(results)
#--------------------------YOU-TUBE----------------------------------------------			
		elif 'open youtube' in query:
			webbrowser.open("https://www.youtube.com")
		elif 'search' and 'on youtube' in query:
			query = query.replace("search", "")
			query = query.replace("on youtube", "")
			speak("Searching on YouTube...")
			webbrowser.open("https://www.youtube.com/results?search_query="+query)
		elif 'play' and 'song in youtube' in query:
			query = query.replace("play", "")
			query = query.replace("song", "")
			kit.playonyt(query)
#-------------------------------GOOGLE--------------------------------------------------------
		elif 'open google' in query:
			webbrowser.open("https://www.google.co.in/")
		elif 'search' and 'on google' in query:
			query = query.replace("search", "")
			query = query.replace("on google", "")
			speak("Searching on Google...")
			speak("According to Google.....")
			webbrowser.open("https://www.google.co.in/search?q="+query)
			try:
				results = wikipedia.summary(query, sentences=3)
				speak(results)
			except Exception as e:
				print(e)
				speak("Sorry... No voice assist available for this search")
#----------------------------To SWITCH WINDOWs-----------------------------------------
		elif ('change the window' in query):
			pyautogui.keyDown("alt")
			pyautogui.press("tab")
			time.sleep(1)
			pyautogui.keyUp("alt")
#----------------------------NEWS------------------------------------------------------
		elif('current news' in query):
			speak("please wait fetching the news....")
			news()
#----------------------------WHATSAPP------------------------------------------------------
		elif 'open whatsapp' in query:
			webbrowser.open("https://web.whatsapp.com/")
#-----------------------------MUSIC-----------------------------------------------------------
		elif 'play music' in query:
			webbrowser.open("https://music.youtube.com")
		elif 'my favourite music' in query:
			webbrowser.open("https://music.youtube.com/watch?v=55ATjCZCjuM&list=RDAMVM55ATjCZCjuM")
#------------------------------CSGO-----------------------------------------------------
		elif 'cs go' in query:
			webbrowser.open("steam://rungameid/730")
#-------------------------------TIME------------------------------------------------------------
		elif ('time' in query):
			hour = int(datetime.datetime.now().hour)
			Time = datetime.datetime.now().strftime("%H:%M:%S")
			if(hour>=0 and hour<12):
				print(Time,"AM")
				speak(f"the time is {Time} AM")
			elif (hour>=12 and hour <18):
				print(Time, "PM")
				speak(f"the time is {Time} PM")
			else:
				print(Time, "PM")
				speak(f"the time is {Time} PM")
#---------------------------CALCULATOR----------------------------------------------------------
		elif('calculate for me' in query):
			print("Say what you want to calculate")
			speak("Say what you want to calculate....")
			r = sr.Recognizer()
			my_mic_device = sr.Microphone(device_index=1)
			with my_mic_device as source:
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
			my_string=r.recognize_google(audio)
			print(my_string)
			speak(my_string," is...")
			def get_operator_fn(op):
				return {
					'+' : operator.add,
					'-' : operator.sub,
					'*' : operator.mul,
					'divided' :operator.__truediv__,
					'Mod' : operator.mod,
					'mod' : operator.mod,
					'^' : operator.xor,
					}[op]

			def eval_binary_expr(op1, oper, op2):
				op1,op2 = int(op1), int(op2)
				return get_operator_fn(oper)(op1, op2)

			print(eval_binary_expr(*(my_string.split())))
			speak(eval_binary_expr(*(my_string.split())))
#-------------------------SYSTEM APPLICATION COMMANDS--------------------------------------------#
		#--------------------------notepad----------------------------------------
		elif ('open notepad' in query):
			np = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
			os.startfile(np)
		elif('close notepad' in query):
			os.system("taskkill /f /im notepad++.exe")
		#-----------------------command prompt--------------------------------------------
		elif ('open command prompt' in query):
			os.system("start cmd")
		elif ('close command prompt' in query):
			os.system("stop cmd")
		#---------------------------discord------------------------------------------
		elif ('open discord' in query):
			np = "C:\\Users\\tejas\\AppData\\Local\\Discord\\app-0.0.309\\Discord.exe"
			os.startfile(np)
		elif('close discord' in query):
			os.system("taskkill /f /im Discord.exe")
		#---------------------------excel-----------------------------------------------
		elif ('open excel' in query):
			np = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
			os.startfile(np)
		elif('close excel' in query):
			os.system("taskkill /f /im EXCEL.exe")
		#----------------------------word-----------------------------------------------
		elif ('open word' in query):
			np = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
			os.startfile(np)
		elif('close word' in query):
			os.system("taskkill /f /im WINWORD.exe")
		#----------------------------ppt----------------------------------------------
		elif ('open ppt' in query):
			np = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
			os.startfile(np)
		elif('close ppt' in query):
			os.system("taskkill /f /im POWERPNT.EXE")		
#------------------------CAMERA---------------------------------	
		elif ('open camera' in query):
			cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
			while True:
				ret, img = cap.read()
				k = cv2.waitKey(5)
				cv2.imshow('my frame', img)
				if k == 1:
					break			
			cap.release()
			cv2.destroyAllWindows()
#----------------------IP ADDRESS--------------------------------------
		elif ('ip address' in query):
			ip = requests.get('https://api.ipify.org').text
			print("Your IP address: ", ip)
			speak(f"your IP address is {ip}")
		elif ('where am i' in query or 'where are we' in query):
			ip = requests.get('https://api.ipify.org').text
			try:
				url = 'https://get.geojs.io/v1/ip/geo/'+ip+'.json'
				geo_request = requests.get(url)
				geo_data= geo_request.jason()
				country = geo_data['country']
				state = geo_data['state']
				city = geo_data['city']
				speak(f"Currently we are in {state}, {city} located in {country}")
			except Exception as e:
				print(e)
				speak("Sorry sir, Due to no proper network I'm not able to get your location")
				
#----------------------ALARM--------------------------------------------
		elif('set alarm of' in query):
			speak("your alarm has been set...")
			alarm = int(query.replace("set alarm of ", ""))	
#------------------------JOKES-------------------------------------------
		elif("tell me a joke" in query):
			speak("Here's a joke for you....")
			joke = pyjokes.get_joke()
			print(joke)
			speak(joke)
#------------------------VOLUME CONTROLL----------------------------------
		elif ('volume up' in query):
			pyautogui.press("volumeup")
		elif ('volume down' in query):
			pyautogui.press("volumedown")
		elif ('mute yourself' in query):
			pyautogui.press("volumemute")
#------------------------COVID CASES---------------------------------------
		elif("current covid cases" in query):
			'''url = "https://worldometers.p.rapidapi.com/api/coronavirus/world"
			headers = {
				'x-rapidapi-key': "bb99da44b6msh285e85559582ea1p18cae3jsnbbdec86bcdcb",
				'x-rapidapi-host': "worldometers.p.rapidapi.com"
				}
			response = requests.request("GET", url, headers=headers)
			print(response.text)
			speak(response.text)'''
			url = "https://worldometers.p.rapidapi.com/api/coronavirus/country/India"
			headers = {
				'x-rapidapi-key': "ae2c3fd144msh8584fe991a66c61p1c5f17jsn057f1e129734",
				'x-rapidapi-host': "worldometers.p.rapidapi.com"
				}
			response = requests.request("GET", url, headers=headers)
			print(response.text)

#---------------------------EMAIL-------------------------------
		elif 'email to' in query:
			to = ""
			try:
				if 'angad singh obbi' in query:
					to = email["angad singh obbi"]
				elif 'atharva mulgund' in query:
					to = email["atharva mulgund"]
				elif 'mrunmai patil' in query:
					to = email["mrunmai patil"]
				elif 'durgesh khole' in query:
					to = email["durgesh khole"]
				elif 'baliram pansare' in query:
					to = email["baliram pansare"]
				elif 'tejas phanse' in query:
					to = email["tejas phanse"]
				else:
					speak("Email not registered")
				
				speak("What should I say?")
				content = takeCommand()
				sendEmail(to,content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("Sorry... I am not able to send this email")
				
#-------------------------------------PROGRAM COMMANDS-------------------------------------
		elif('open desktop' in query):
			speak("Showing up the Desktop....")
			os.startfile(Dict)
		elif 'power off' in query :
			speak("POWERING of in.....3......2.....1.....")
			a = False
		elif 'make all systems offline' in query:
			speak("It's pleasure to work with you sir!!!..... SHUTING OFF in....................3.............2.................1 ")
			os.system("shutdown /s /t 1")
		elif ('pause the system' in query):
			os.system("rundll32.exe powrporf.dll,SetSuspendState 0,1,0")
		elif 'reboot the system' in query:
			speak("REBOOTING in....................3.............2.................1 ")
			os.system("shutdown /r /t 5")
	