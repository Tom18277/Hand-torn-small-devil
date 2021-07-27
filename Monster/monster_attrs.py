"""
            怪物制造工厂
"""
# TODO 怪物的属性有待增加和更改，各级别怪物出现概率需要联系英雄的等级 -- 21.7.27/23：47

import random


class MonsterAttrs(object):
    attr_: tuple = None

    def __init__(self, name):
        """
        Blood 血量
        harm  伤害
        Armor 护甲
        xp 附带经验
        """
        self.attr_ = self.factory(name)
        # self.Blood = self.attr_[0]
        # self.harm = self.attr_[1]
        # self.Armor = self.attr_[2]

    def factory(self, monster_name):
        """
        制造工厂
        @param monster_name: 接受一个怪物名称
        @return: 初始化怪物属性
        """
        monster_attrs = {
            '三等兵': (80, 10, 0, round(random.triangular(7.3, 23, mode=10))),
            '二等兵': (100, 20, 0, round(random.triangular(7.8, 25, mode=10))),
            '一等兵': (100, 25, 10, round(random.triangular(13.8, 38, mode=19.8), 2)),
            '上等兵': (120, 30, 15, round(random.triangular(27, 48, mode=38), 2)),
            '下士': (130, 40, 20, round(random.triangular(27, 58, mode=32), 2)),
            '伍长': (140, 40, 25, round(random.triangular(27, 58, mode=34), 2)),
            '中士': (150, 40, 30, round(random.triangular(27, 68, mode=36), 2)),
            '上士': (160, 40, 35, round(random.triangular(27, 68, mode=38), 2)),
            '军士长': (180, 50, 40, round(random.triangular(27, 78, mode=36), 2)),
            '准尉': (200, 50, 50, round(random.triangular(27, 78, mode=38), 2)),
            '准士官': (240, 50, 60, round(random.triangular(27, 78, mode=40), 2)),
            '少尉': (260, 60, 70, round(random.triangular(27, 78, mode=42), 2)),
            '大尉': (280, 70, 80, round(random.triangular(27, 78, mode=44), 2)),
            '大佐': (300, 80, 90, round(random.triangular(27, 78, mode=46), 2))
        }
        return monster_attrs[monster_name]
