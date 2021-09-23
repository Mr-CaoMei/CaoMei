import pypinyin


def pinyin(word):  # 实现拼音转换
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
        # print(s)
    return s


def beg_word_min(word):  # 实现小写拼音首字母转换
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i[0][0])
    # print(s)
    return s


def beg_word_max(word):  # 实现大写拼音首字母转换
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(str.swapcase(i[0][0]))
    # print(s)
    return s
