from GameSys.state import state
from GameSys.extension import extension

class Game:
    def __init__(self) -> None:
        self.state = state()
        self.progress = 20
        self.extensions = [
            extension("健康手环", "展示使用者的健康状况(心肺系统机能+神经系统状态)")]
        self.resources = {
            "docs.scd": "项目文档",
            "alchemist.ml": "机器学习问答社区"
        }
        self.move = 2
        self.overmove = 1

    def check(self):
        return self.state.check()

    def update(self, command):
        print(command)