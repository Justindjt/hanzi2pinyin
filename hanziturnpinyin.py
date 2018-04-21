def pinyindict(filepath):
    pinyin_list = []
    with open(filepath, 'r') as file_test:
        for file_str in file_test.readlines():
            pinyin_file_list = []
            pinyin_file_list = file_str.strip('\n').split(' ')
            pinyin_list.append(pinyin_file_list)
    return pinyin_list


PinyinDict = dict(pinyindict('E:\Program\word\chinese_unicode_to__pinyin.txt'))


def getpy(hanzi):
    pinyin_list = []
    for char in hanzi[:]:
        char_ord = hex(ord(char))
        if char_ord in PinyinDict:
            pinyin_str = PinyinDict[char_ord]
            pinyin_list.append(pinyin_str)
    return pinyin_list


# def main():
#     pinyin_str = input('请输入需要查询拼音的汉字： ')
#     pinyin_list = pinyin_str.split()
#     pinyin = getpy(pinyin_str)
#     print(pinyin)
#
#
# if __name__ == '__main__':
#     main()
