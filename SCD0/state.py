class state:
    def __init__(self) -> None:
        self.health = 8 #0-10
        self.ability = 0 #1-4
        self.money = 1000 #0-
        self.day = 1 #1-7
        self.week = 0 #0-
        self.mood = 1 #0-3
        self.tired = 2 #0-5

    def show(self):
        output = "健康 = "+str(self.health)+" 能力 = "+str(self.ability)+" 资金 = "+str(self.money)+" 剩余时间 = "+str(self.day)
        return output

    def update(self, health=0, ability=0, money=0, day=0, mood=0):
        self.health += health
        self.ability += ability
        self.money += money
        self.day += day
        self.mood += mood

    def check(self):
        return self.health > 0
