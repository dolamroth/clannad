import os

const = """
А -- A
Б -- ｱ
В -- B
Г -- ｲ
Д -- ｳ
Е -- E
Ё -- ｴ
Ж -- ｵ
З -- ｶ
И -- ｷ
Й -- ｸ
К -- ｹ
Л -- ｺ
М -- M
Н -- H
О -- O
П -- ｻ
Р -- P
С -- C
Т -- T
У -- ｼ
Ф -- ｽ
Х -- ｾ
Ц -- ｿ
Ч -- ﾀ
Ш -- ﾁ
Щ -- ﾂ
Ъ -- ｪ
Ы -- ｫ
Ь -- ｬ
Э -- ﾆ
Ю -- ﾇ
Я -- ﾈ
а -- a
б -- ﾉ
в -- ﾊ
г -- ﾋ
д -- ﾌ
е -- e
ё -- ﾍ
ж -- ﾎ
з -- ﾏ
и -- ﾐ
й -- ﾑ
к -- ﾒ
л -- ﾓ
м -- ﾔ
н -- ﾕ
о -- o
п -- ﾖ
р -- p
с -- c
т -- ﾗ
у -- ﾘ
ф -- ﾙ
х -- ﾚ
ц -- ﾛ
ч -- ﾜ
ш -- ﾝ
щ -- ｩ
ъ -- ｪ
ы -- ｫ
ь -- ｬ
э -- ｭ
ю -- ｮ
я -- ｯ
""".strip().split('\n')

change = {}
for elem in const:
    change[elem[0]] = elem[-1]

import argparse
parser = argparse.ArgumentParser(description='My example explanation')
parser.add_argument('word', type=str)
args = parser.parse_args()
print(''.join([change.get(c, c) for c in args.word]))