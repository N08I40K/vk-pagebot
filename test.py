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
vk_session = vk_api.VkApi(token="3cb7fb7873747265d7ad45c849725d15b6b4a1489810accf6efbcd9dc0641f190b4abaa16b360b3360ec1")
long_poll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        peer_id = event.peer_id
        members = vk.messages.getConversationMembers(peer_id = peer_id)
        i = members["items"]
        print(random.choice(list(i)))