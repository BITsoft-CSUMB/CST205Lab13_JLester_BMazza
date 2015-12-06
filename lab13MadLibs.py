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

Original Article: "Sony shows a flawed PlayStation VR demo on a big stage"
    from
    http://venturebeat.com/2015/12/05/sony-shows-a-playstation-vr-demo-on-a-big-stage/

Mad Libs Outline (by index of array):
    0. product name ("VR")
    1. your name ("Richard Marks")
    2. place ("San Francisco")
    3. adjective ("hot")
    4. type of object ("virtual reality")
    5. number ("30")
    6. object plural ("Move controllers")
    7. object plural ("discs")
    8. type of place ("virtual space")
    9. name ("Oculus Rift")

Sony shows a flawed PlayStation (0) demo on a big stage


Sony's (1) showed off the PlayStation (0) system at the PlayStation Experience
fan event in San Francisco. Unfortunately, it went off the rails.

Debuting next spring, the PlayStation (0) is Sony's entry in the (3) field
of (4), which is expected to be a $(5) billion business by 2020.

(1)'s two-person demo didn't work as planned. Their own motion-detecting 
(6) failed. They couldn't throw (7) at their fellow (0) partner in a
virtual room. The other player could throw (7) at (1), but it was
clear that the controls weren't that precise. It took quite a long time before
they were able to throw accurately.

But the demo did show that two people could occupy the same (8) and throw
(7) at each other. Most demos of (0) games have been single-player experiences.

"I hope this demo gives you a taste of what PlayStation (0) is about," (1) said.

Sony is launching the PlayStation (0) early next year. It will
compete with the (9) coming from Facebook's Oculus (0) division.
"""

article = [
    "\n\n Sony shows a flawed PlayStation ", # 0 "product name"
    " demo on a big stage \n\n\n Sony's ", # 1 "your name"
    " showed off the PlayStation ", # 0 "product name"
    " system at the PlayStation Experience\n fan event in ", # 2 "place"
    ". Unfortunately, it went off the rails. \n\n Debuting next spring," +
        " the PlayStation ", # 0 "product name"
    " is Sony's entry in the ", # 3 "adjective"
    " field\n of ", # 4 "type of object"
    ", which is expected to be a $", # 5 "number"
    " billion business by 2020. \n\n ", # 1 "your name"
    "'s two-person demo didn't work as planned. Their own" +
        " motion-detecting\n ", # 6 "object plural"
    " failed. They couldn't throw ", # 7 "object plural"
    " at their fellow ", # 0 "product name"
    " partner in a\n virtual room. The other player could" +
        " throw ", #7 "object plural"
    " at ", # 1 "your name"
    ", but it was\n clear that the controls weren't that precise. It took" +
        " quite a long time before\n they were able to throw accurately." +
        "\n\n But the demo did show that two people could occupy the" +
        " same ", # 8 "type of place"
    " and throw\n ", # 7 "object plural"
    " at each other. Most demos of ", # 0 "product name"
    " games have been single-player experiences.\n\n \"I hope this demo" +
        " gives you a taste of what PlayStation ", # 0 "product name"
    " is about,\" ", # 1 "your name"
    " said.\n\n Sony is launching the PlayStation ", # 0 "product name"
    " early next year. It will\n compete with the ", # 9 "product name"
    " coming from Facebook's Oculus ", # 0 "product name"
    " division."
]
# Get words from the user.
wordTypes = [
    "name",
    "your name",
    "place",
    "adjective",
    "type of object",
    "number",
    "object plural",
    "object plural",
    "type of place",
    "name"]
chosenWords = []
for wordType in wordTypes:
    chosenWords.append(requestString("Enter a(n) " + wordType + "."))
# Fill entered words into appropriate spot.
words = [
    chosenWords[0],
    chosenWords[1],
    chosenWords[0],
    chosenWords[2],
    chosenWords[0],
    chosenWords[3],
    chosenWords[4],
    chosenWords[5],
    chosenWords[1],
    chosenWords[6],
    chosenWords[7],
    chosenWords[0],
    chosenWords[7],
    chosenWords[1],
    chosenWords[8],
    chosenWords[7],
    chosenWords[0],
    chosenWords[0],
    chosenWords[1],
    chosenWords[0],
    chosenWords[9]
]
# Combine the article with the entered words and display it.
newString = ""
for index in range(len(words)):
    newString += article[index] + words[index]
newString += article[len(article)-1]
printNow(newString)
