"""
请定义一个城市的类，想一想，一个城市应该有什么属性，应该有什么方法。
属性：人口数量、高楼数量、城市面积
方法：扩建道路、拆迁旧楼、疏通下水道
请尝试在上面列举的属性与方法之外，定义其它的属性与方法。

"""


class city:
    def __init__(self):
        self.people: int = 100000
        self.buildings: int = 9000
        self.area: float = 90000000.0
        self.money: float = 10000000000.0

    def make_road(self):
        self.area += 100.0
        self.money -= 20000.0

    def rem(self):
        self.area -= 100.0
        self.money -= 20000

    def rem_block(self):  # 疏通
        self.money -= 1000.0
