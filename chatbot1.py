from chatterbot import ChatBot
   

# "ChatterBotCorpusTrainer"
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("bot")
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)
  
   


   
while True:
    try:
        bot_input = chatbot.get_response(input("you :"))
        print("bot "+str(bot_input))

    except(KeyboardInterrupt, EOFError, SystemExit):
        break