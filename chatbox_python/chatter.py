from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)
chatbot = ChatBot('testbot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish")

response = chatbot.get_response('hi!')
print(response)
