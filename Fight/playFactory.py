"""
            战斗界面
"""
# TODO 完成实例 "英雄" 和 "怪物" 两个对象，部署战斗的界面显示和打斗开展的计算 -- 21.7.27//20：19


from Monster.monster_attrs import MonsterAttrs
from Hero.hero_attrs import MakeHero


class PlayFactory(object):
    Monster = None
    Hero = None

    def __init__(self, MN, HN):
        self.Monster = MonsterAttrs(MN).attr_
        # self.Hero = HN['attrs']
        self.Hero = HN

    def Attackfunction(self):
        lisAtt = list(self.Monster)
        print('-----------战斗开始-----------')
        self.print_gui(self.Hero['Blood'], self.Hero['harm'], self.Hero['Armor'], self.Monster[0], self.Monster[1],
                       self.Monster[2])
        while True:
            command = int(input('command-[🔪:1 🛡:2] ::'))
            if command == 1:
                lisAtt[0] -= self.Hero['harm']
                print(self.Monster)
                print(lisAtt)
            #     TODO 攻击场景、攻击计算（防御、闪避概率；护甲的减伤）
            elif command == 2:
                pass

    def print_gui(self, h_bld, h_harm, h_A,m_bld, m_harm, m_A, ):
        print(
"""
[ Hero: ❤:{}  🔪:{}  🛡:{} ] 👈 ☠ 👉 [ 三等兵: ❤:{}  🔪:{}  🛡:{} ]
""".format(h_bld, h_harm, h_A, m_bld, m_harm, m_A))


a = {'Understand': 11, 'Blood': 104, 'harm': 23, 'Armor': 22, 'dodge': 11.0, 'agile': 12.0, 'Humanity': 12}
PlayFactory(MN='三等兵', HN=a).Attackfunction()
