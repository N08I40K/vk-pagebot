import sys
sys.path.append('moduless/')
from forplugins import *
class init:
    def func(message=None, peer_id=None, user_id=None, chat_id=None):
        if message == cmd_prefix + "вопрос":
            random_response=random.randint(-2, 2)
            if random_response == -2:
                response_a = "Нет."
            if random_response == -1:
                response_a = "Скорее нет."
            if random_response == 0:
                response_a = "50 на 50."
            if random_response == 1:
                response_a = "Скорее да."
            if random_response == 2:
                response_a = "Да."
            send_msg(peer_id=peer_id, text=str(response_a))
            log_txt = "*id" + str(user_id) + " вызвал команду 'вопрос'"
            console_log(log_txt)
            message_log(log_txt)