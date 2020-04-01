#primeiro import uma lista de treinamento
from chatterbot.trainers import ListTrainer
#esta importação irá usar a biblioteca chatbot do python
from chatterbot import ChatBot

bot = ChatBot('MS BOT')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Quem é você?', 'Eu, sou o MS BOT prazer em conhece-lo(a)', 'o que você pode fazer?', 'Eu posso aprender com voce']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("humano: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('MS BOT: ', resposta)
    else:
        print('MS BOT: Ainda não sei responder esta pergunta')
