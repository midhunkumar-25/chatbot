from django.conf import settings
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from .cleaner import clean_corpus
import os
CORPUS_FILE = os.path.join(settings.BASE_DIR,"accounts/chat.txt")

chatbot = ChatBot("Chatpot")
trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)
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
trainer.train([
    "my gpa",
    "gpa",
])
trainer.train([
    "my attendance",
    "attendance",
])
def classify_intent(text):
    return chatbot.get_response(text)



