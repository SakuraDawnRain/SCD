class state:
    def __init__(self) -> None:
        self.health = 8 #0-10
        self.ability = 0 #1-4
        self.money = 1000 
        self.time = 7

    def show(self):
        output = "健康 = "+str(self.health)+" 资金 = "+str(self.money)+" 时间 = "+str(self.time)
        return output

    def update(self, health=0, ability=0, money=0, day=0):
        self.health += health
        self.ability += ability
        self.money += money
        self.day += day

    def check(self):
        return self.health > 0
