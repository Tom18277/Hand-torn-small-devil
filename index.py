import random
from Fight.playFactory import PlayFactory

if __name__ == '__main__':
    # zh = int(input('zh::'))
    # pw = int(input('pw::'))
    BitchName = ['大佐', '大尉', '少尉', '准士官', '准尉', '军士长', '上士', '中士',
                 '伍长', '下士', '上等兵', '一等兵', '二等兵', '三等兵', ]
    monster_name = random.choice(BitchName)
    PlayFactory(MN=monster_name,HN='测试')

