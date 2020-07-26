import sys
sys.path.append('moduless/')
from forplugins import *
class init:
    def func(message=None, peer_id=None, user_id=None, chat_id=None):
        if message == cmd_prefix + "время":
            days = {
                0: 'понедельник',
                1: 'вторник',
                2: 'среда',
                3: 'четверг',
                4: 'пятница',
                5: 'суббота',
                6: 'воскресенье'
            }
            timemsg = "Текущие дата и время по МСК: "
            delta = datetime.timedelta(hours=3)
            utc = datetime.timezone.utc
            fmt = '%d-%m-%Y %H:%M:%S'
            time = (datetime.datetime.now(utc) + delta)
            timestr = time.strftime(fmt)
            send_msg(peer_id=peer_id, text=str(timemsg) + " \n" + str(timestr) + "\nСегодня " + str(days[time.weekday()]))
            log_txt = "*id" + str(user_id) + " вызвал команду 'время'"
            console_log(log_txt)
            message_log(log_txt)