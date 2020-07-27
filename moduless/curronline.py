import sys
sys.path.append('moduless/')
from forplugins import *
class init:
    def func(message=None, peer_id=None, user_id=None, chat_id=None):
        if message == cmd_prefix + "онлайн":
            users_tmp = vk.messages.getConversationMembers(peer_id=peer_id)
            stackinfo = ""
            stackinfo += "Онлайн: \n"
            global number_id
            number_id = 1
            for i in users_tmp["profiles"]:
                if i.get('online', False) == True:
                    first_name = i.get('first_name', False)
                    last_name = i.get('last_name', False)
                    screen_name = i.get('screen_name', False)
                    usr_id = i.get('id', False)
                    stackinfo += str(number_id) + ". [id" + str(usr_id) + "|" + str(first_name) + " " + str(last_name)+ "]" + " \n"
                    number_id + 1
            send_msg(peer_id=peer_id, text=str(stackinfo))
            log_txt = "*id" + str(user_id) + " вызвал команду 'онлайн'"
            console_log(log_txt)
            message_log(log_txt)