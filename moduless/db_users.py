import sys
sys.path.append('moduless/')
from forplugins import *
class init:
    def func(message=None, peer_id=None, user_id=None, chat_id=None):
        char_to_find = str(chat_id)
        if char_to_find[0] == "-":
            return False
        try:
            os.mkdir('becedi/'+str(chat_id))
        except:
            zaglushka = "."
        createfile = open(r'becedi/'+str(chat_id)+'/users_db.txt', "a")
        createfile.close()
        users_tmp = vk.messages.getConversationMembers(peer_id=peer_id)
        stackinfo = ""
        for i in users_tmp["profiles"]:
            if i.get('id', False) == user_id:
                first_name = i.get('first_name', False)
                last_name = i.get('last_name', False)
                screen_name = i.get('screen_name', False)
                usr_id = i.get('id', False)
                stackinfo += str(usr_id) + ":" + str(first_name) + ":" + str(last_name) + ":" + str(chat_id)
        word = stackinfo.split(":")[0]
        stackinfo3 = stackinfo.split(":")[1]
        stackinfo4 = stackinfo.split(":")[2]
        stackinfo5 = stackinfo.split(":")[3]
        inp = open('becedi/'+str(chat_id)+'/users_db.txt').readlines()
        global i1
        global i2
        global i3
        global i4
        global i5
        i1 = ""
        i2 = ""
        i3 = ""
        i4 = ""
        i5 = ""
        for i in iter(inp):
            if word in i:
                i1 = i.split(":")[0]
                i2 = i.split(":")[1]
                i3 = i.split(":")[2]
                i4 = i.split(":")[3]
                i5 = "1"
        if i5 == "1":
            i5 = "0"
            return True
        else:
            with open(r'becedi/'+str(chat_id)+'/users_db.txt', "a") as file_db:
                file_db.write(str(stackinfo)+"\n")
            if reg_warn == "1":
                send_msg(peer_id=peer_id, text="Пользователь [id" + str(word) + "|" + str(stackinfo3) + " " + str(stackinfo4) + "] зарегистирован в системе.")
            print("Пользователь id" + str(word) + " " + str(stackinfo3) + " " + str(stackinfo4) + " зарегистирован в системе.")