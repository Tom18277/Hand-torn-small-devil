import random
import time


class MakeHero(object):
    def __init__(self):
        """
        悟性
        血量
        伤害
        护甲
        闪避
        敏捷
        人脉
        """
        self.Understand = 10
        self.Blood = 100
        self.harm = 20
        self.Armor = 20
        self.dodge = 10.0
        self.agile = 10.0
        self.Humanity = 10

    def factory(self):
        """
        制造工厂
        @return:
        """
        count = 15
        print(f'系统将会自动分配点数至您的英雄结构树上，共{count}点')
        print("""
悟性:%d
血量:%d
伤害:%d
护甲:%d
闪避:%.2f
敏捷:%.2f
人脉:%d""" % (self.Understand, self.Blood, self.harm, self.Armor, self.dodge, self.agile, self.Humanity))
        time.sleep(2)
        while count:
            heroKey = random.choices(['Understand', 'Blood', 'harm', 'Armor', 'dodge', 'agile', 'Humanity'], k=3)
            a, b, c = heroKey[0], heroKey[1], heroKey[2]
            exec(f'self.{a} += 1')
            exec(f'self.{b} += 1')
            exec(f'self.{c} += 1')
            count -= 3
        print("""
悟性:%d
血量:%d
伤害:%d
护甲:%d
闪避:%.2f
敏捷:%.2f
人脉:%d""" % (self.Understand, self.Blood, self.harm, self.Armor, self.dodge, self.agile, self.Humanity))
        return (self.Understand, self.Blood, self.harm, self.Armor, self.dodge, self.agile, self.Humanity)

    def goUp(self):
        """
        角色升级
        @return:
        """
        self.Understand += random.randint(3,7)
        self.Blood += 15
        self.harm += random.randint(5,10)
        self.Armor += 5
        self.dodge += round(random.uniform(0.4,2.8),2)
        self.agile += round(random.uniform(1.1,2.3),2)
        self.Humanity += random.randint(5,10)
