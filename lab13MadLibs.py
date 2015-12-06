"""
School: CSU, Monterey Bay
Course: CST 205 Multimedia Design and Programming
Instructor: Allie Xiong
Assignment: Lab #13 Pt. 1 Mad Libs
Authors: John Lester & Brittany Mazza
Date: December 2-8, 2015
Filename: lab13MadLibs.py
Python Version: 2.2.1 (JES 4.3)
Version: 1
# CST205 Lab 13 - Programmer: John Lester
"""

#article from http://venturebeat.com/2015/12/05/sony-shows-a-playstation-vr-demo-on-a-big-stage/
article = [
  "Sony's Richard Marks showed off the PlayStation ", #_0 (VR) 0
  " system at the PlayStation Experience fan event in ", #_1 (San Francisco) 1
  ". Unfortunately, it went off the rails. \n\nDebuting next spring, the PlayStation ", #_2 (VR) 0
  " is Sony's entry in the hot field of ", #_3 (virtual reality) 3
  ", which is expected to be a $30 billion business by 2020. \n\nMarks' two-person demo didn't work as planned. His own motion-detection ", #_4 (Move controllers) 4
  " failed. He couldn't throw ", #_5 (discs) 5
  " at his fellow VR partner in a virtual room. The other player could throw ", #_6 (discs) 5
  " at Marks, but it was clear that the controls weren't that precise. It took quite a long time before he was able to throw accurately. \n\nBut the demo did show that two people could occupy the same ", #_7 (virtual space) 7 
  " and throw ", #_8 (discs) 5
  " at each other. Most demos of ", #_9 (VR) 0
  " games have been single-player experiences. \n\n\"I hope this demo gives you a taste of what PlayStation ", #_10 (VR) 0
  " is about,\" Marks said. \n\nSony is launching the PlayStation ", #_11 (VR) 0
  " early next year. It will compete with the ", #_12 (Oculus Rift) 12
  " coming from Facebook's Oculus ", #_13 (VR) 0
  " division" #_14 (.) -
]

words = []
for key in range(len(article)):
  words.append("")
words[0] = requestString('Give me a name: ') #VR
words[1] = requestString('Give me a place: ') #San Francisco
words[2] = words[0]
words[3] = requestString('Give me a type of object: ') #virtual reality
words[4] = requestString('Give me an object: ') #Move controller
words[5] = requestString('Give me another object: ') #discs
words[6] = words[5]
words[7] = requestString('Give me a type of place: ') #virtual space
words[8] = words[5]
words[9] = words[0]
words[10] = words[0]
words[11] = words[0]
words[12] = requestString('Give me another name: ') #Oculus Rift
words[13] = words[0]
words[14] = ".\n"

newString = ""
for key in range(len(words)):
  newString += article[key]
  newString += words[key]
for num in range(5):
  printNow("")
printNow(newString)