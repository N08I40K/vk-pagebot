import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api import VkApi
import datetime
import time
import pytz
import random
import os
import json
import sys

config_lines = open("config.txt").readlines()
parameters_lines = [line[line.find("=") + 1:].replace("\n", "") for line in config_lines]
# обьявление базовых переменных, соединение с ВК
    
allowed_ids = [int(num) for num in parameters_lines[1].split(",")]
allowed_chats = [int(num) for num in parameters_lines[2].split(",")]
log_id = [int(num) for num in parameters_lines[3].split(",")]
index = int(parameters_lines[4])
delay = int(parameters_lines[5])
cmd_prefix = parameters_lines[6]
cmd_eval = parameters_lines[7]
safe_eval = parameters_lines[9]
vk_session = vk_api.VkApi(token=parameters_lines[0])
long_poll = VkLongPoll(vk_session)
vk = vk_session.get_api()
event = long_poll.listen()
def get_time():
    # возвращает время формата ДД.ММ.ГГ ЧЧ:ММ:СС (по МСК)
    # например, 01.01.01 13:37:00
    return datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('Europe/Moscow')), "%d.%m.%Y %H:%M:%S")


def console_log(text, symbols_amount=30):
    # выводит данные в консоль с указанием времени и интервалом после
    print("[" + get_time() + "] " + text)
    print("-" * symbols_amount)

def send_msg(peer_id=None, domain=None, chat_id=None, text=None,
             sticker_id=None, user_id=None):
    vk.messages.send(
        user_id=user_id,
        random_id=random.randint(-2147483648, 2147483647),
        peer_id=peer_id,
        domain=domain,
        chat_id=chat_id,
        message=text,
        sticker_id=sticker_id,
    )


def message_log(text):
    if log_id != [0]:
        for i in log_id:
            send_msg(user_id=i, text=text)
            time.sleep(delay)