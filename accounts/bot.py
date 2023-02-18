from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 🤗"
])
trainer.train([
    "college Fees",
    "college fee",
])
trainer.train([
    "Fees",
    "college fee",
])
trainer.train([
    "placements",
    "placements",
])
trainer.train([
    "hostel",
    "hostelfee",
])
def classify_intent(text):
    return chatbot.get_response(text)



