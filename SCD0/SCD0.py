import os
import random
import json
from state import state

#settings loading
os.system("cls")
print("请选择难度")
with open("settings.json", encoding="utf8") as s:
    settings = json.load(s)
for key in settings:
    print(key)
    setting = settings[key]
    print("    资金目标", str(setting["fund"]))
    print("    时间限制", str(setting["week"]), "weeks")
choice = input()
setting = settings[choice]
#events loading
with open("events.json", encoding="utf8") as e:
    events = json.load(e)


state = state()
worklist = [] # 0-5
input()

#game start
while(state.check()):
    os.system("cls")
    print(state.show())
    state.update(health=-2)
    input()
input("结束")