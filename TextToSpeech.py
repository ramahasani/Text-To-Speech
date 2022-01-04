import pyttsx3
engine = pyttsx3.init()


for voice in engine.getProperty('voices'):
    print(voice)

def change_voice(engine, name):
    for voice in engine.getProperty('voices'):
        if name in voice.name :
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}'  not found".format(name))

rate = engine.getProperty('rate')   # getting details of current speaking rate
print ('Kecepatan:', rate) 

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print ('volume:', volume)                          


change_voice(engine, "Microsoft Andika - Indonesian (Indonesia)")
engine.setProperty('volume',0.75)
engine.setProperty('rate', 150)
engine.say("Kepada Bapak Sumarno, Silahkan masuk ke ruang tunggu Nomor 123")
engine.runAndWait()

change_voice(engine, "Microsoft Rizwan - Malay (Malaysia)")
engine.setProperty('volume',0.75)
engine.setProperty('rate', 150)
engine.say("Kepada Bapak Sumarno, Silahkan masuk ke ruang tunggu Nomor 123")
engine.runAndWait()

change_voice(engine, "Microsoft Zira Desktop - English (United States)")
engine.setProperty('volume',0.75)
engine.setProperty('rate', 150)
engine.say("Kepada Bapak Sumarno, Silahkan masuk ke ruang tunggu Nomor 123")
engine.runAndWait()

change_voice(engine, "Microsoft David Desktop - English (United States)")
engine.setProperty('volume',0.75)
engine.setProperty('rate', 150)
engine.say("Kepada Bapak Sumarno, Silahkan masuk ke ruang tunggu Nomor 123")
engine.runAndWait()