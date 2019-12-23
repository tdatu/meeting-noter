import time
import speech_recognition as sr
from datetime import datetime

r = sr.Recognizer()
fs = open("converted_audio.txt","w+")

with sr.Microphone() as source:
	print("Audio conversion now:")
	while True:
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			n = datetime.now()			
			fs.write('{} -- {}\n'.format(n.strftime("%Y-%m-%d %H:%M:%S"),text))
			print("recorded: {}".format(text))
			time.sleep(.5)
			if text == "stop recording":
				print("Ending recording session")
				fs.close()
				break
		except sr.UnknownValueError:
			print("Google speech recognition could not understand your audio")
		except sr.RequestError as e:
			print("Could not request results from Google")
