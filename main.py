import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 created by one and only ME")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to speak (type 'q' to quit): ")
        if x.lower() == "q":
            engine.say('bye bye friend')
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
