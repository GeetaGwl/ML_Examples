from nltk.chat.util import Chat,reflections
from pairss import p1 as pairs
#pairs=[[r"my name is (.*)",["hello %1. how are you"]],]

def first():
    print("hi what can i do for you")
    chatbot=Chat(pairs,reflections)
    chatbot.converse()

if __name__ == '__main__':
    first()
        