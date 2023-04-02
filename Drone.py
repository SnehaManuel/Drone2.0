from Body.Listen import MicInput
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Body.Speak import Speak
from Features.Clap import Tester
from Main import MainTaskExecution

print(">> Starting The Drone: Wait For Some Seconds.")


def MainExecution():
    Speak("Hello Miss, I'm Drone, I'm ready to assist you.")
    
    while True:
        Data = MicInput()
        Data = str(Data)
        ValueReturn = MainTaskExecution(Data)
        if ValueReturn == True:
            pass
        elif len(Data)<3:
            pass

        elif "What is" in Data or " where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionAnswer(Data)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)
        
def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print(">>Clap Detected! >>")
        MainExecution()
    else:
        pass

    ClapDetect()

ClapDetect()
