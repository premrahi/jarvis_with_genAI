import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("Enter the Word you wnat ot speak it out by computer")
    s = input()
    speaker.speak(s)