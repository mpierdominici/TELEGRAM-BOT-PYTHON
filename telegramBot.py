# -*- coding: utf-8 -*-

import telebot  # biblioteca de la api del bot

from telebot import types

import time

TOKEN = '730560993:AAHWcJ22fhjkfeU_MjJ5_PcDs-b7Mz790I8'  # token del bot

AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/ayuda - Guia para utilizar el bot. \n/info - Informacion De interes \n/hola - Saludo del Bot \n/piensa3D - Informacion sobre Piensa3D \n\n'


# listener
def listener(messages):
    for singData in messages:
        cid = singData.chat.id  # identificador del chat, >0 usuarios , <0 grupos
        if cid > 0:
            log = str(singData.chat.first_name) + "[" + str(cid) + "]" + " = " + singData.text
        else:
            log = str(singData.from_user.first_name) + "[" + str(cid) + "]" + " = " + singData.text

        eventLog = open('log.txt', 'a')  # abrir en modo añadir
        eventLog.write(log + "\n")
        eventLog.close()


bot = telebot.TeleBot(TOKEN)  # instancia del bot
bot.set_update_listener(listener)  # seteamos el callback del listener

# COMANDOS


@bot.message_handler(commands=['help'])  # comando '/ayuda'

def command_help(m):  # funcion llamada con el comando ayuda

    cid = m.chat.id  # se guarda el id para poder responder

    bot.send_chat_action(cid, 'typing')  # Enviando ...

    time.sleep(1)  # esperamos 1 seg para responder
    print(m.text)
    bot.send_message(cid, AYUDA)  # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.


@bot.message_handler(commands=['status'])  # Indicamos que lo siguiente va a controlar el comando '/info'

def command_status(m):  # Definimos una función que resuleva lo que necesitemos.

    cid = m.chat.id  # Guardamos el ID de la conversación para poder responder.


    bot.send_message(cid, 'status')

@bot.message_handler(commands=['reboot'])  # Indicamos que lo siguiente va a controlar el comando '/info'

def command_status(m):  # Definimos una función que resuleva lo que necesitemos.

    cid = m.chat.id  # Guardamos el ID de la conversación para poder responder.


    bot.send_message(cid, 'reboot')



bot.polling(none_stop=True)
