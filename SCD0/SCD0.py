from GameSys.Kernel import Game
import UI
import os

discription = """
距离年终绩效考核还剩7天
你是首创地科技公司(SCD Ltd)的一名数据科学家
你需要通过调整数据处理和训练方法
完成机器学习模型的训练
总之 得想办法完成工作
并且 别在工作完成之前

猝死

按下任意键继续
"""

help = """
指令列表
pass   跳过本次行动
ext    查看插件说明
help   显示帮助
train  训练模型 需要消耗行动点
find( +资源地址)   查找问题解决方案 需要消耗行动点
"""

game = Game()
print(discription)
input()
os.system('cls')

guide = {
    0: "我是主人的AI助手姬 会为主人提供引导哦",
    1: "虽然时间只剩七天了 但我相信主人一定能把这个机器学习模型完成的",
    2: "插件是主人能够获得的物品 比如现在这个【健康手环】 在终端输入 ext 来获取插件的说明吧",
    3: ""
}

username = "user"

def parser(input):
    inputs = input.split()
    command = inputs[0]
    if len(inputs)>1:
        option = inputs[1]

    if command == "pass":
        pass
    elif command == "ext":
        for i in range(len(game.extensions)):
            print("【{}】: {}".format(game.extensions[i].name, game.extensions[i].intro))
    elif command == "help":
        print(help)
    elif command == "train":
        
        if game.move>0:
            game.move = game.move - 1
        elif game.overmove > 0:
            game.overmove = game.overmove - 1
        else:
            print("error")
            return
        
    elif command == "find" and len(inputs)>1:
        complete = False


        
        if option in game.resources.keys():
            print()
        else:
            print("地址解析失败 请检查拼写")

        if game.move>0:
            game.move = game.move - 1
        elif game.overmove > 0:
            game.overmove = game.overmove - 1
        else:
            print("error")
            return
    else:
        print("指令未找到")

day_check = [False, False, False, False, False, False, False, False]

while(game.check()):
    day = game.state.time
    if not day_check[day]:
        UI.display_info(game.state, game.progress, game.extensions, game.resources)

    if game.state.time == 7 and not day_check[day]:
        print("helper@SCD0", guide[0])
        print("helper@SCD0", guide[1])
        print("helper@SCD0", guide[2])

    day_check[day] = True

    order = input("{}@SCD0> ".format("username"))
    parser(order)

    if game.move == 0 and game.overmove != 0:
        print("helper@SCD0 今天的工作该结束啦 再工作下去会伤身体的")
        rest = input("是否继续工作(O/其他)")
        if rest != "O":
            game.overmove = 0
    if game.move == 0 and game.overmove == 0:
        game.state.time = day - 1
        os.system('cls')
        game.move = 2
        game.overmove = 1
    