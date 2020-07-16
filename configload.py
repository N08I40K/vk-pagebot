import sys
import os
import datetime

#HELP LOAD START
script_path = os.path.abspath(__file__).replace("configload.py", "")
configg_lines = open(script_path + "help_conf.txt").readlines()
def count_lines(filename, chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
            for chunk in iter(lambda: file.read(chunk_size), ''))
count_lines("help_conf.txt")
help_info = ""
strnum = 0
while True:
    help_info += configg_lines[int(strnum)]
    strnum += 1
    print(strnum)
    if strnum >= count_lines("help_conf.txt"):
        break
#HELP LOAD END

#TIME LOAD START
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
#TIME LOAD END
