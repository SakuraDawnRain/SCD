import os
import random

#data
health = 8     #0-10
ability = 1    #1-4
work = 200     #200-0
money = 1000   #0-
day = 100      #100-0
mood = 1       #0-3
tired = 2      #0-5

#probability 0-9
found_by_boss = 2
tired_over_sleep = 3
study_success = 4

#functions
def get_state():
    return "健康 = "+str(health)+" 能力 = "+str(ability)+" 剩余工作 = "+str(work)+" 资金 = "+str(money)+" 剩余时间 = "+str(day)

#game start
while( health>0 and day>0 and money>0 and work>0 ):
    os.system("cls")
    print("新的一天！")

    # show state
    state = get_state()
    print(state)

    # day time
    print("准时上班！")
    day_choice = input("今天怎么工作呢？0=摸鱼 其他=爆肝")
    if day_choice=="0":
        if random.randint(0, 9)>found_by_boss:
            mood = mood+1 if mood<3 else mood
            print("成功摸鱼！开心！")
        else:
            mood = mood-1 if mood>0 else mood
            money = money - 100
            print("被发现了！被扣钱了……失落……")
    else:
        work_amount = mood*ability
        work = work - work_amount
        if work_amount==0:
            print("心情低落，没有进度。")
    print(state)

    #night time
    print("该下班了！")
    night_choice = input("怎么安排时间呢？1=通宵爆肝 2=提升自己 其他=休养生息")
    if night_choice=="1":
        health = health-2
        work_amount = mood*ability
        work = work - work_amount
        print("你通宵了")
    elif night_choice=="2":
        if random.randint(0, 9)>study_success:
            ability = ability+1 if ability<4 else ability
            print("能力提升")
        else:
            print("失败")
    else:
        health = health+1 if health<9 else health

    input("开启下一天吧")
    day = day-1

#game end
os.system("cls")
print(state)
if health<1:
    print("你 猝 死 了")
elif money<1:
    print("你 破 产 了")
elif work<1:
    print("工 作 完 成")
elif day<1:
    print("你 被 开 了")

input("结束")