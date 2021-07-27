"""
            Game入口
"""
# TODO ? -- 21.7.27//20：13


import json
import random
import time

from Fight.playFactory import PlayFactory
from Hero.hero_attrs import MakeHero as mh


def login():
    print('-----------注册-----------')
    zh, pw, name = input('zh::'), input('pw::'), input('名字::')
    user_init = mh().factory()
    userDict = {'play': [zh, pw, name],
                'attrs': {
                    'Understand': user_init[0],
                    'Blood': user_init[1],
                    'harm': user_init[2],
                    'Armor': user_init[3],
                    'dodge': user_init[4],
                    'agile': user_init[5],
                    'Humanity': user_init[6]
                }}
    with open('User Info/user.json', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(userDict, indent=4))
    print('注册成功！')
    time.sleep(3)


if __name__ == '__main__':
    BitchName = ['大佐', '大尉', '少尉', '准士官', '准尉', '军士长', '上士', '中士',
                 '伍长', '下士', '上等兵', '一等兵', '二等兵', '三等兵', ]
    monster_name = random.choice(BitchName)
    flag = input('注册”Y/N“::').upper()
    if flag == 'Y':
        login()
        print('正在退出程序...请重新运行')
    elif flag == 'N':
        print('-----------登录-----------')
        zh, pw = input('zh::'), input('pw::')
        with open('User Info/user.json', 'r+', encoding='utf-8') as f:
            fil = json.loads(f.read())
            if fil['play'][0] != zh and fil['play'][1] != pw:
                print('密码错误！')
            elif fil['play'][0] == zh and fil['play'][1] == pw:
                print('登录成功！ 加载中...')
                time.sleep(3)
                PlayFactory(MN=monster_name, HN=fil)
                pass  # TODO 进入战斗页面
            else:
                print('请检查账号和密码~')


    # PlayFactory(MN=monster_name, HN='测试')
