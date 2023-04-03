import PySimpleGUI as sg
import pyttsx3

layout = [
    [sg.Text('Enter text to speak:')],
    [sg.InputText()],
    [sg.Text('Select voice type:')],
    [sg.DropDown(values=['Male', 'Female'], key='voice')],
    [sg.Button('Speak')]
]

window = sg.Window('Text to Speech App', layout)

def speak(text, voice_type):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voice_type == 'Male':
        engine.setProperty('voice', voices[0].id)
    elif voice_type == 'Female':
        engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Speak':
        text = values[0]
        voice_type = values['voice']
        speak(text, voice_type)



