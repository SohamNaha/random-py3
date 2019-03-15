"""
Description : 
No more hiding from your alarm clock! You've decided you want your computer to keep you updated on the time so you're never late again. A talking clock takes a 24-hr time and translates it intowords.

Input Description :
An hour(0-23) followed by a colon followed by the minute (0-59).

Output Description : 
The time in words, using 12-hour format followed by an am or pm.

Sample Input Data : 
00:00
01:30
12:05
14:01
20:29
21:00

Sample Output Data : 
It's twelve am.
It's one thirty am.
It's twelve oh five pm.
It's two oh one pm.
It's eigth twenty nine pm.
It's nine pm.

"""
# global declarations
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
tens = ["", "", "twenty", "thirty", "forty", "fifty"]
hours = [
    "twelve",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
]
ap = ["am", "pm"]


def calculateMinutes(m):
    if m == 0:
        return tens[m]
    if m < 10:
        return " ".join(["oh", ones[m]])
    elif m < 20:
        return teens[m % 10]
    else:
        temp = m % 10
        h = m // 10
        return " ".join([tens[h], ones[temp]])


# taking input
[hour, minutes] = list(map(int, input().split(":")))

am_or_pm = ap[0] if hour < 12 else ap[1]
hours_ = hours[hour % 12]
minutes = calculateMinutes(minutes)
s = " ".join(["It's", hours_, minutes, am_or_pm, "."]).replace("  "," ")
print(s)

"""
# Using gTTS (Google Text To Speech API)
# text to speech conversion
from gtts import gTTS

engine = gTTS(text=s, lang="en")
engine.save("Voice.mp3")

import os
os.system("Voice.mp3")
"""


# Using pyttsx3
import pyttsx3

engine = pyttsx3.init()
engine.say(s)
engine.setProperty("rate", 120)
engine.runAndWait()
