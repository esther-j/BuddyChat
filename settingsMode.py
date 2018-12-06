"""Credit for file writing: https://www.cs.cmu.edu/~112/notes/notes-strings.html"""

from tkinter import *
import cv2
import os
from widgets import *

##### settings mode
def settingsMousePressed(event, data, log):
    if data.settingsIcon.isPressed(event.x, event.y):
        if data.previousMode == "run":
            data.mode = "run"
        elif data.previousMode == "friend":
            data.mode = "friend"
    elif data.goHomeOption.isPressed(event.x, event.y):
        data.mode = "start"
    elif data.changeColorOption.isPressed(event.x, event.y):
        colorIndex = data.colorOptions.index(data.botColor)
        if colorIndex + 1 == len(data.colorOptions):
            newColor = 0
        else:
            newColor = colorIndex + 1
        data.botColor = data.colorOptions[newColor]
        data.changeColorOption.color = data.botColor
    elif data.faceDetectionOption.isPressed(event.x, event.y):
        if data.detectFace:
            data.detectFace = False
            data.faceDetectionOption.option = "Turn on face detection (currently off)"
        else:
            data.detectFace = True
            data.faceDetectionOption.option = "Turn off face detection (currently on)"            
    elif data.clearLogOption.isPressed(event.x, event.y):
        clearLog(log)
    elif data.saveLogOption.isPressed(event.x, event.y):
        saveLog(data.chatLog)
    
def settingsKeyPressed(event, data):
    pass
    
def settingsTimerFired(data):
    cv2.destroyAllWindows()
    
def settingsRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "gray", width = 0)
    subtitle(data, canvas, data.width / 10, data.height / 120, "Settings")
    canvas.create_text(data.width * 7 / 20, data.height / 15, text = "(Click square to select/change)", font = "arial %d bold" % (data.height // 30), anchor = NW)
    data.settingsIcon.color = "white"
    data.settingsIcon.draw(canvas)
    data.goHomeOption.draw(canvas)
    data.changeColorOption.draw(canvas)
    data.clearLogOption.draw(canvas)
    data.faceDetectionOption.draw(canvas)
    data.saveLogOption.draw(canvas)
    
def clearLog(log):
    log.config(state = NORMAL)
    log.delete(1.0, END)
    log.yview_pickplace(END)
    log.config(state = DISABLED)

def saveLog(chatLog):
    chatScript = ""
    for line in chatLog:
        chatScript += line + "\n"
    chatScript.strip()
    writeFile("chatLog.txt", chatScript)

def writeFile(path, contents):
    os.remove(path)
    with open(path, "wt") as f:
        f.write(contents)