from datetime import datetime

import speech_recognition

r = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    r.adjust_for_ambient_noise(mic,duration=1)
    print("start speaking...")
    audio = r.listen(mic)

print("Done recording voice...")
text = r.recognize_google(audio)
print(text)

note_date = datetime.strftime(datetime.today(),"%d/%m/%Y, %H:%M:%S")

md_text = f"| {note_date} | {text} |\n"

with open('Notes.md','a') as md:
    md.write(md_text)

print("Notes has been saved!")
