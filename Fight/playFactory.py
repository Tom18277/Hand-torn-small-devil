from Hero.hero_attrs import MakeHero
# from Monster.monster_attrsa import

class PlayFactory(object):
    MonsterName = None
    HeroName = None
    def __init__(self,MN,HN):
        self.hero = HN
        self.monster = MN
        print(self.hero,self.monster)
    def Attackfunction(self):
        pass

