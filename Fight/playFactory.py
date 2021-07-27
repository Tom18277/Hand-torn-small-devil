from Monster.monster_attrs import MonsterAttrs
from Hero.hero_attrs import MakeHero

class PlayFactory(object):
    Monster = None
    Hero = None
    def __init__(self,MN,HN):
        self.Monster = MonsterAttrs(MN).attr_
        self.Hero = MakeHero().factory()
        # print(self.hero,self.monster)
        print(MN,self.Monster)
        print(HN,self.Hero)
    def Attackfunction(self):
        pass

