import pyautogui
import time
import os
from pynput.keyboard import Controller, Key, Listener, GlobalHotKeys
import pynput.keyboard as keyboard
import pyperclip
import configparser
import re
import sys
import random
import threading

exit_flag = False
cfg_ini_files = ['召唤物中型星团.ini', '混沌持续弓.ini']
cfg_ini_file = cfg_ini_files[0]
def on_press(key):
    global exit_flag
    if key == keyboard.Key.tab:
         exit_flag = True
         print('Exiting')

# 获取当前屏幕分辨率
def get_screenpoint():
    # screenWidth, screenHeight = pyautogui.size()  # 获取屏幕的尺寸
    # print(screenWidth, screenHeight)
    x, y = pyautogui.position()  # 获取当前鼠标的位置
    print('坐标已复制' + str(x) + ',' + str(y))
    pyperclip.copy(str(x) + ',' + str(y))

# 获取Item信息
def get_item_location():
    cp = configparser.ConfigParser()
    dirs = os.listdir('正在使用的config')
    cp.read('正在使用的config' + '\\' + cfg_ini_file, encoding="utf-8-sig")
    x, y = pyautogui.position()  # 获取当前鼠标的位置
    now_time = str(time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time())))
    cp.set("item", now_time, str(x) + ',' + str(y))
    cp.write(open('正在使用的config' + '\\' + cfg_ini_file, "w", encoding='utf-8-sig'))

def exit_sys():
    sys.exit()

def use_transmutation(transmutation_point, item_point):
    # 定义各个需要用到的通货的位置点
    currency_number['transmutation'] -= 1
    pyautogui.moveTo(int(transmutation_point.split(",", 1)[0]), int(transmutation_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click(button='right')
    pyautogui.moveTo(int(item_point.split(",", 1)[0]), int(item_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click()
    time.sleep(random.uniform(0, 0.3))

def use_scouring(scouring_point, item_point):
    # 定义各个需要用到的通货的位置点
    currency_number['scouring'] -= 1
    pyautogui.moveTo(int(scouring_point.split(",", 1)[0]), int(scouring_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click(button='right')
    pyautogui.moveTo(int(item_point.split(",", 1)[0]), int(item_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click()
    time.sleep(random.uniform(0, 0.3))

def use_alc(alc_point, item_point):
    # 定义各个需要用到的通货的位置点
    currency_number['alc'] -= 1
    pyautogui.moveTo(int(alc_point.split(",", 1)[0]), int(alc_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click(button='right')
    pyautogui.moveTo(int(item_point.split(",", 1)[0]), int(item_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click()
    time.sleep(random.uniform(0, 0.3))

def use_aug(aug_point, item_point):
    # 定义各个需要用到的通货的位置点
    currency_number['aug'] -= 1
    pyautogui.moveTo(int(aug_point.split(",", 1)[0]), int(aug_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click(button='right')
    pyautogui.moveTo(int(item_point.split(",", 1)[0]), int(item_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click()
    time.sleep(random.uniform(0, 0.3))

def use_alt(alt_point, item_point):
    # 定义各个需要用到的通货的位置点
    currency_number['alt'] -= 1
    pyautogui.moveTo(int(alt_point.split(",", 1)[0]), int(alt_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click(button='right')
    pyautogui.moveTo(int(item_point.split(",", 1)[0]), int(item_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click()
    time.sleep(random.uniform(0, 0.3))

def use_reg(reg_point, item_point):
    # 定义各个需要用到的通货的位置点
    currency_number['reg'] -= 1
    pyautogui.moveTo(int(reg_point.split(",", 1)[0]), int(reg_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click(button='right')
    pyautogui.moveTo(int(item_point.split(",", 1)[0]), int(item_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click()
    time.sleep(random.uniform(0, 0.3))

def use_chaos(chaos_point, item_point):
    # 定义各个需要用到的通货的位置点
    currency_number['chaos'] -= 1
    pyautogui.moveTo(int(chaos_point.split(",", 1)[0]), int(chaos_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click(button='right')
    pyautogui.moveTo(int(item_point.split(",", 1)[0]), int(item_point.split(",", 1)[1]), duration=0.1)
    pyautogui.click()
    time.sleep(random.uniform(0, 0.3))

def make_gear():
    # 初始化INI
    cp = configparser.ConfigParser()
    dirs = os.listdir('正在使用的config')
    cp.read('正在使用的config' + '\\' + cfg_ini_file, encoding="utf-8-sig")
    # 定义需要的Mod，
    and_mod = eval(cp.get('Mod', 'and_mod'))
    count_mod = eval(cp.get('Mod', 'count_mod'))
    count_times = eval(cp.get('Mod', 'count_times'))
    not_mod = eval(cp.get('Mod', 'not_mod'))

    # 定义需要的Magic_mod
    magic_and_mod = eval(cp.get('magic_Mod', 'magic_and_mod'))
    magic_count_mod = eval(cp.get('magic_Mod', 'magic_count_mod'))
    magic_count_times = eval(cp.get('magic_Mod', 'magic_count_times'))
    magic_not_mod = eval(cp.get('magic_Mod', 'magic_not_mod'))

    # 定义POEDB前后缀总集
    pre_list = eval(cp.get('PreandSuf', 'pre_list'))
    suf_list = eval(cp.get('PreandSuf', 'suf_list'))

    # 检查设置的mod和magic_mod条件是否在定义的前后缀总集中，防止定义错误导致无限洗
    pre_and_suf_str_list = pre_list + suf_list
    # 合并所有字典的键
    combined_keys = list(and_mod.keys()) + list(count_mod.keys()) + list(not_mod.keys()) + list(magic_and_mod.keys())\
                    + list(magic_count_mod.keys()) + list(magic_not_mod.keys())
    unique_keys = list(set(combined_keys))
    check_ret = False
    for i in unique_keys:
        for j in pre_and_suf_str_list:
            if len(re.findall(i, j, re.S)) != 0 or len(re.findall(j, i, re.S)) != 0:
                check_ret = True
                break
        if check_ret == False:
            print('词缀' + i + ' 不在总表里，请修改')
            sys.exit()
        check_ret = False

    # 定义选择的做装模式
    make_model = eval(cp.get('make_model', 'model'))

    # 进行总分判断,和前后缀总分检查
    All_point = len(and_mod) + count_times
    if All_point > 3:
        print('总分大于3，无法制作')
        sys.exit()
    elif All_point == 3 and make_model in [1, 2]:
        print("你要求的词缀>=3，不可能在改造、改造增幅模式下成功")
        sys.exit()

    # 进行魔法总分判断
    magic_All_point = len(magic_and_mod) + magic_count_times
    if magic_All_point != 0:
        if magic_All_point > 2:
            print('魔法总分大于2，无法制作')
            sys.exit()
        elif len(magic_and_mod) >= 1 and magic_count_times >= 1 and list(set(magic_and_mod.values())) == list(set(magic_count_mod.values())):
            print('魔法物品定义了两个前缀或后缀，无法完成')
            sys.exit()
        elif len(magic_and_mod) >= 2 and magic_count_times >= 0 and len(list(set(magic_and_mod.values()))) == 1:
            print('magic_and_mod词缀2缀为同一个类型')
            sys.exit()
        elif len(magic_and_mod) >= 0 and magic_count_times >= 2 and len(list(set(magic_count_mod.values()))) == 1:
            print('magic_count_mod二缀为同一个类型')
            sys.exit()

    if make_model == 3:
        # 新增对词缀的判断
        if len(and_mod) >= 1 and count_times >= 2 and list(set(and_mod.values())) == list(set(count_mod.values())):
            print('要做的物品定义了超过三个前或后缀，无法完成')
            sys.exit()
        elif len(and_mod) >= 2 and count_times >= 1 and list(set(and_mod.values())) == list(set(count_mod.values())):
            print('要做的物品定义了超过三个前或后缀，无法完成')
            sys.exit()
        elif len(and_mod) >= 3 and count_times >= 0 and len(list(set(and_mod.values()))) == 1:
            print('andmod三缀为同一个类型')
            sys.exit()
        elif len(and_mod) >= 0 and count_times >= 3 and len(list(set(count_mod.values()))) == 1:
            print('count_mod三缀为同一个类型')
            sys.exit()
    elif make_model == 1 or make_model == 2:
        # 新增对词缀的判断
        if All_point > 2:
            print('总分大于2，无法制作')
            sys.exit()
        elif len(and_mod) >= 1 and count_times >= 1 and list(set(and_mod.values())) == list(set(count_mod.values())):
            print('物品定义了两个前缀或后缀，无法完成')
            sys.exit()
        elif len(and_mod) >= 2 and count_times >= 0 and len(list(set(and_mod.values()))) == 1:
            print('and_mod词缀2缀为同一个类型')
            sys.exit()
        elif len(and_mod) >= 0 and count_times >= 2 and len(list(set(count_mod.values()))) == 1:
            print('count_mod二缀为同一个类型')
            sys.exit()
    else:
        print('做装模式选择错误，请输入1或2或3')
        sys.exit()

    # 先分别移动到各个通货检查一遍，得到通货的具体数量,加入到通货字典里
    currency_list = cp.options("currency")
    global currency_number
    currency_number = {}
    for currency in currency_list:
        currency_point = cp.get('currency', currency)
        pyautogui.moveTo(int(currency_point.split(",", 1)[0]), int(currency_point.split(",", 1)[1]), duration=0.1)
        pyperclip.copy('')
        pyautogui.hotkey('ctrl', 'c')
        if pyperclip.paste() == '':
            print(currency + '为空请补充')
            sys.exit()
        try:
            number = re.search('堆叠数量: (.*?)/', pyperclip.paste()).group(1).strip()
        except:
            number = re.search('Stack Size: (.*?)/', pyperclip.paste()).group(1).strip()
        currency_number[currency] = int(number.replace(',', ''))

    # 通货基准值，用来统计最后用了多少
    currency_number_copy = currency_number.copy()

    # 定义各通货基准点
    transmutation_point = cp.get("currency", "transmutation")  # 蜕变
    scouring_point = cp.get("currency", "scouring")  # 重铸
    alc_point = cp.get("currency", "alc")  # 点金
    aug_point = cp.get("currency", "aug")  # 增幅
    alt_point = cp.get("currency", "alt")  # 改造
    reg_point = cp.get("currency", "reg")  # 富豪
    chaos_point = cp.get("currency", "chaos")  # 混沌

    # 初始化ini第二部分
    cp2 = configparser.RawConfigParser()
    cp2.read('ninja价格信息.ini', encoding="utf-8-sig")
    # 定义各通货对比C的价格
    transmutation_chaos = float(cp2.get("Price", "orb of transmutation"))  # 蜕变
    scouring_chaos = float(cp2.get("Price", "orb of scouring"))  # 重铸
    alc_chaos = float(cp2.get("Price", "orb of alchemy"))  # 点金
    aug_chaos = float(cp2.get("Price", "orb of augmentation"))  # 增幅
    alt_chaos = float(cp2.get("Price", "orb of alteration"))  # 改造
    reg_chaos = float(cp2.get("Price", "regal orb"))  # 富豪
    chaos_chaos = 1  # 混沌

    # 找到所有的item，进行for循环
    item_list = cp.options("item")
    for item in item_list:
        item_point = cp.get('item', item)
        # 这里应该做个死循环
        while True:
            try:
                if exit_flag:
                    print('程序已退出')
                    break

                # 先看通货剩余量，如果没有通货了直接跳出
                # print(currency_number)
                if 0 in currency_number.values():
                    print('通货不足：' + str(currency_number))
                    sys.exit()
                # 把鼠标放到物品上，对物品稀有度和词缀进行判断
                pyautogui.moveTo(int(item_point.split(",", 1)[0]), int(item_point.split(",", 1)[1]), duration=0.1)
                pyperclip.copy('')
                pyautogui.hotkey('ctrl', 'alt', 'c')
                item_status = pyperclip.paste()
                # 寻找词缀，并进行前后缀组织，找到词缀后对词缀整体段落进行判断，全部词缀是否都被识别出来了，如果没有，报错停止,mod是游戏里带数值的实际属性，pre，suf是列表里的正则表达式形式
                re_prefix_list = []
                re_suffix_list = []
                mod_prefix_list = []
                mod_suffix_list = []
                for pre in pre_list:
                    if re.search(pre, item_status):
                        mod = re.search(pre, item_status, re.S).group(0)
                        re_prefix_list.append(pre)
                        mod_prefix_list.append(mod)
                for suf in suf_list:
                    if re.search(suf, item_status):
                        mod = re.search(suf, item_status).group(0)
                        re_suffix_list.append(suf)
                        mod_suffix_list.append(mod)

                # 判断装备稀有度
                try:
                    Item_Rarity = re.search('稀 有 度: (.*)', item_status).group(1).strip()
                except:
                    Item_Rarity = re.search('Rarity: (.*)', item_status).group(1).strip()

                # 统计找出了多少个词缀，是否和物品上的真实词缀条数相同，防止ini中的正则匹配词条写错
                allfix_list = re_prefix_list + re_suffix_list
                if len(allfix_list) != 0:
                    real_mod_list = re.search('-----.*-----(.*?{}.*?)(-----|$)'.format(allfix_list[0]), item_status, re.S).group(1).strip().split('等阶', -1)
                    if len(allfix_list) != len(real_mod_list)-1:
                        print('找到的词缀' + str(allfix_list) + '\n' + '真实的词缀' + str(
                            real_mod_list) + '\n' + '上述两个列表的词缀不相等，词缀没找全，系统关闭')
                        sys.exit()
                elif len(allfix_list) == 0 and Item_Rarity not in ['Normal', '普通']:
                    print('非普通装备寻找到的词条为0，请检查ini，系统关闭')
                    sys.exit()

                # 判断得分，得分是关键词对前后缀拼接的字符串进行匹配，如果匹配到了则加分，countmod 的分数最多不能超过count_times
                get_point = 0
                count_timecheck = 0
                # 拼接物品上的词缀成为一个字符串
                pre_and_suf_str = " ".join(mod_prefix_list) + " ".join(mod_suffix_list)
                # 判断每一个and_mod的属性，如果在字符串里，则加分
                for i in and_mod.keys():
                    if re.search(i, pre_and_suf_str) is not None:
                        get_point += 1
                for i in count_mod.keys():
                    if re.search(i, pre_and_suf_str) is not None:
                        if count_timecheck < count_times:
                            count_timecheck += 1
                            get_point += 1
                # print('物品得分' + str(get_point))

                # 判断魔法得分，得分是关键词对前后缀拼接的字符串进行匹配，如果匹配到了则加分，magic_countmod 的分数最多不能超过magic_count_times
                magic_get_point = 0
                magic_count_timecheck = 0
                # 判断每一个and_mod的属性，如果在字符串里，则加分
                for i in magic_and_mod.keys():
                    if re.search(i, pre_and_suf_str) is not None:
                        magic_get_point += 1
                for i in magic_count_mod.keys():
                    if re.search(i, pre_and_suf_str) is not None:
                        if magic_count_timecheck < magic_count_times:
                            magic_count_timecheck += 1
                            magic_get_point += 1
                # print('物品得分' + str(magic_get_point))

                # 开始具体的装备判断
                # 如果稀有度是白色，则上蜕变石
                if Item_Rarity == '普通' or Item_Rarity == 'Normal':
                    # print('物品等级是普通')
                    use_transmutation(transmutation_point, item_point)
                # 如果稀有度是蓝色
                if Item_Rarity == '魔法' or Item_Rarity == 'Magic':
                    # print('物品等级是魔法')

                    # 判断not词缀是否在里面,如果在词缀里则使用改造
                    for i in not_mod:
                        if re.search(i, pre_and_suf_str) is not None:
                            # 使用改造石
                            use_alt(alt_point, item_point)

                    # 如果前缀为0，后缀为1
                    if len(re_prefix_list) == 0 and len(re_suffix_list) == 1:
                        # 得分为0 且 总分<=2 且 and和count所有词缀至少有一个是前缀
                        if get_point == 0 and All_point <= 2 and ('pre' in and_mod.values() or 'pre' in count_mod.values()):
                            # 如果是改造模式（1），使用改造石
                            if make_model == 1:
                                use_alt(alt_point, item_point)
                            # 如果是模式2（改造增幅），使用增幅
                            elif make_model == 2:
                                use_aug(aug_point, item_point)
                            # 如果是模式3（改造增幅富豪），使用增幅
                            elif make_model == 3:
                                use_aug(aug_point, item_point)
                        elif get_point == 1:
                            if All_point > get_point:
                                # 如果是改造模式（1），使用改造石
                                if make_model == 1:
                                    use_alt(alt_point, item_point)
                                # 如果是模式2（改造增幅），使用增幅
                                elif make_model == 2:
                                    use_aug(aug_point, item_point)
                                # 如果是模式3（改造增幅富豪），使用增幅
                                elif make_model == 3:
                                    # 如果有魔法总分
                                    if magic_All_point != 0:
                                        # 如果魔法总分>魔法得分
                                        if magic_All_point > magic_get_point:
                                            # print(magic_get_point)
                                            # 魔法得分为0
                                            if magic_get_point == 0:
                                                # 如果魔法总分=1且魔法and count所有词缀至少有一个是前缀——上增幅
                                                if magic_All_point == 1 and (
                                                        'pre' in magic_and_mod.values() or 'pre' in magic_count_mod.values()):
                                                    use_aug(aug_point, item_point)
                                                # 如果魔法总分=2，假设增幅成2个词缀，也无法满足魔法得分等于2，因为此时的魔法得分为0，故直接使用改造——使用改造
                                                elif magic_All_point == 2:
                                                    use_alt(alt_point, item_point)
                                                # 可能出现magic_All_point =1 但是需要的magic不在前缀里，使用改造
                                                else:
                                                    use_alt(alt_point, item_point)
                                            # 如果魔法总分=1
                                            elif magic_get_point == 1:
                                                # 如果魔法总分=2，且魔法and count所有词缀至少有一个是前缀——上增幅
                                                if magic_All_point == 2 and (
                                                        'pre' in magic_and_mod.values() or 'pre' in magic_count_mod.values()):
                                                    use_aug(aug_point, item_point)
                                                else:
                                                    use_alt(alt_point, item_point)
                                            # 如果魔法总分没在1,2里，报错
                                            elif magic_All_point not in [1, 2]:
                                                print(str(magic_All_point) + '格式错误')
                                                sys.exit()

                                        # 如果魔法总分<=魔法得分
                                        elif magic_All_point <= magic_get_point:
                                            use_aug(aug_point, item_point)
                                    # 如果没有魔法总分
                                    elif magic_All_point == 0:
                                        use_aug(aug_point, item_point)
                            elif All_point <= get_point:
                                # 跳出循环
                                break
                        else:
                            # 使用改造
                            use_alt(alt_point, item_point)
                    # 如果前缀为1，后缀为0
                    if len(re_prefix_list) == 1 and len(re_suffix_list) == 0:
                        if get_point == 0 and All_point <= 2 and ('suf' in and_mod.values() or 'suf' in count_mod.values()):
                            # 如果是改造模式（1），使用改造石
                            if make_model == 1:
                                use_alt(alt_point, item_point)
                            # 如果是模式2（改造增幅），使用增幅
                            elif make_model == 2:
                                use_aug(aug_point, item_point)
                            # 如果是模式3（改造增幅富豪），使用增幅
                            elif make_model == 3:
                                use_aug(aug_point, item_point)
                        elif get_point == 1:
                            if All_point > get_point:
                                # 如果是改造模式（1），使用改造石
                                if make_model == 1:
                                    use_alt(alt_point, item_point)
                                # 如果是模式2（改造增幅），使用增幅
                                elif make_model == 2:
                                    use_aug(aug_point, item_point)
                                # 如果是模式3（改造增幅富豪），使用增幅
                                elif make_model == 3:
                                    # 如果有魔法总分
                                    if magic_All_point != 0:
                                        # 如果魔法总分>魔法得分
                                        if magic_All_point > magic_get_point:
                                            # 魔法得分为0
                                            # print(magic_get_point)
                                            if magic_get_point == 0:
                                                # 如果魔法总分=1且魔法and count所有词缀至少有一个是后缀——上增幅
                                                if magic_All_point == 1 and (
                                                        'suf' in magic_and_mod.values() or 'suf' in magic_count_mod.values()):
                                                    use_aug(aug_point, item_point)
                                                # 如果魔法总分=2，假设增幅成2个词缀，也无法满足魔法得分等于2，因为此时的魔法得分为0，故直接使用改造——使用改造
                                                if magic_All_point == 2:
                                                    use_alt(alt_point, item_point)
                                                # 可能出现magic_All_point =1 但是需要的magic不在后缀里，使用改造
                                                else:
                                                    use_alt(alt_point, item_point)
                                            # 如果魔法总分=1
                                            elif magic_get_point == 1:
                                                # 如果魔法总分=2，且魔法and count所有词缀至少有一个是后缀——上增幅
                                                if magic_All_point == 2 and (
                                                        'suf' in magic_and_mod.values() or 'suf' in magic_count_mod.values()):
                                                    use_aug(aug_point, item_point)
                                                # 否则改造
                                                else:
                                                    use_alt(alt_point, item_point)
                                            # 如果魔法总分没在1,2里，报错
                                            elif magic_All_point not in [1, 2]:
                                                print(str(magic_All_point) + '格式错误')
                                                sys.exit()
                                        # 如果魔法总分<=魔法得分
                                        elif magic_All_point <= magic_get_point:
                                            use_aug(aug_point, item_point)
                                    # 如果没有魔法总分
                                    elif magic_All_point == 0:
                                        use_aug(aug_point, item_point)
                            elif All_point <= get_point:
                                # 跳出循环
                                break
                        else:
                            # 使用改造
                            use_alt(alt_point, item_point)
                    # 如果前缀为1，后缀为1
                    if len(re_prefix_list) == 1 and len(re_suffix_list) == 1:
                        if get_point == 0:
                            # 使用改造
                            use_alt(alt_point, item_point)
                        elif get_point == 1:
                            if All_point > get_point and All_point - get_point <= 1:
                                # 如果是改造模式（1），使用改造石
                                if make_model == 1:
                                    use_alt(alt_point, item_point)
                                # 如果是模式2（改造增幅），使用改造石
                                elif make_model == 2:
                                    use_alt(alt_point, item_point)
                                # 如果是模式3（改造增幅富豪），使用富豪
                                elif make_model == 3:
                                    if magic_All_point != 0:
                                        # 如果魔法总分<=魔法得分
                                        if magic_All_point <= magic_get_point:
                                            for i in magic_not_mod:
                                                # 循环魔法物品not词缀，如果有，使用改造并打破循环，如果没有上富豪
                                                if re.search(i, pre_and_suf_str) is not None:
                                                    use_alt(alt_point, item_point)
                                                    break
                                            use_reg(reg_point, item_point)
                                        else:
                                            use_alt(alt_point, item_point)
                                    else:
                                        use_reg(reg_point, item_point)

                            elif All_point <= get_point:
                                break
                            else:
                                # 使用改造
                                use_alt(alt_point, item_point)
                        elif get_point == 2:
                            if All_point > get_point:
                                # 如果是改造模式（1），使用改造石
                                if make_model == 1:
                                    use_alt(alt_point, item_point)
                                # 如果是模式2（改造增幅），使用改造石
                                elif make_model == 2:
                                    use_alt(alt_point, item_point)
                                # 如果是模式3（改造增幅富豪），使用富豪
                                elif make_model == 3:
                                    if magic_All_point != 0:
                                        # 如果魔法总分<=魔法得分
                                        if magic_All_point <= magic_get_point:
                                            for i in magic_not_mod:
                                                # 循环魔法物品not词缀，如果有，使用改造并打破循环，如果没有上富豪
                                                if re.search(i, pre_and_suf_str) is not None:
                                                    use_alt(alt_point, item_point)
                                                    break
                                            use_reg(reg_point, item_point)
                                        else:
                                            use_alt(alt_point, item_point)
                                    else:
                                        use_reg(reg_point, item_point)

                            elif All_point <= get_point:
                                break

                # 如果稀有度是金色
                if Item_Rarity == '稀有' or Item_Rarity == 'Rare':
                    # print('物品等级是稀有')
                    # 判断not词缀是否在里面,如果在词缀里则使用改造
                    for i in not_mod:
                        if re.search(i, pre_and_suf_str) is not None:
                            # 使用重铸
                            use_scouring(scouring_point, item_point)

                    if All_point > get_point:
                        use_scouring(scouring_point, item_point)
                    elif All_point <= get_point:
                        break

            except Exception as e:
                print('错误' + str(e))
                for i in currency_number_copy.keys():
                    # 用过的数量 = 原来的数量 - 剩余的数量
                    currency_number_copy[i] -= currency_number[i]
                used_chaos = float(currency_number_copy['chaos']) * chaos_chaos + float(
                    currency_number_copy['scouring']) * scouring_chaos + float(
                    currency_number_copy['transmutation']) * transmutation_chaos + float(
                    currency_number_copy['alc']) * alc_chaos + float(currency_number_copy['aug']) * aug_chaos + float(
                    currency_number_copy['alt']) * alt_chaos + float(currency_number_copy['reg']) * reg_chaos
                print('此装备使用了' + str(currency_number_copy) + '约使用了' + str(used_chaos) + '混沌石')
                sys.exit()

        # 报告通货使用情况
        for i in currency_number_copy.keys():
            # 用过的数量 = 原来的数量 - 剩余的数量
            currency_number_copy[i] -= currency_number[i]
        used_chaos = float(currency_number_copy['chaos']) * chaos_chaos + float(
            currency_number_copy['scouring']) * scouring_chaos + float(
            currency_number_copy['transmutation']) * transmutation_chaos + float(
            currency_number_copy['alc']) * alc_chaos + float(currency_number_copy['aug']) * aug_chaos + float(
            currency_number_copy['alt']) * alt_chaos + float(currency_number_copy['reg']) * reg_chaos
        print('此装备使用了' + str(currency_number_copy) + '约使用了' + str(used_chaos) + '混沌石')

        # print('剩余' + str(currency_number))
        # 通货基准值重定义
        currency_number_copy = currency_number.copy()


if __name__ == '__main__':
    # 直接绑定快捷键
    with keyboard.Listener(on_press=on_press) as listener:
        thread = threading.current_thread()
        with GlobalHotKeys({'<alt>+1': get_screenpoint,
                            '<alt>+2': get_item_location,
                            '<alt>+3': make_gear,
                            '<alt>+q': exit_sys
                            }
                           ) as h:
            listener.join()
            h.join()
