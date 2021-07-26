import random


class MonsterAttrs(object):
    attr_: tuple = None
    def __init__(self,name):
        """
        Blood 血量
        harm  伤害
        Armor 护甲
        """
        self.attr_ = self.factory(name)
        self.Blood = self.attr_[0]
        self.harm = self.attr_[1]
        self.Armor = self.attr_[2]
        print(self.Blood,self.Armor)

    def factory(self, monster_name):
        monster_attrs = {
            '三等兵': (80, 10, 0),
            '二等兵': (100, 20, 0),
            '一等兵': (100, 25, 10),
            '上等兵': (120, 30, 15),
            '下士': (130, 40, 20),
            '伍长': (140, 40, 25),
            '中士': (150, 40, 30),
            '上士': (160, 40, 35),
            '军士长': (180, 50, 40),
            '准尉': (200, 50, 50),
            '准士官': (240, 50, 60),
            '少尉': (260, 60, 70),
            '大尉': (280, 70, 80),
            '大佐': (300, 80, 90)
        }
        return monster_attrs[monster_name]


BitchName = ['大佐', '大尉', '少尉', '准士官', '准尉', '军士长', '上士', '中士',
             '伍长', '下士', '上等兵', '一等兵', '二等兵', '三等兵', ]
monster_name = random.choice(BitchName)
