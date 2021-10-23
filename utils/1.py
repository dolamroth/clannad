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

for filename in os.listdir(os.path.join('.', 'ru')):
    with open(os.path.join('.', 'ru', filename), 'rt+', encoding="utf-8") as file_orig:
        with open(os.path.join('.', 'new', filename.replace('.txt', '.utf')), 'wt+', encoding="utf-8") as file_new:
            lines = file_orig.readlines()
            new_lines = []
            flag1 = False
            string_idx = 0
            for line in lines:
                if line.strip() == '':
                    flag1 = False
                    new_lines.append('')
                elif line.startswith('//') and not flag1:
                    flag1 = True
                elif line.startswith('//'):
                    pass
                elif not flag1:
                    pass
                else:
                    new_line = line
                    if len(new_line) >= 6 and new_line[0] == '<' and new_line[5] == '>':
                        new_line = '<' + ('0000' + str(string_idx))[-4:] + '>' + new_line[6:]
                    for char in change:
                        new_line = new_line.replace(char, change[char])
                    while new_line.find('\dango') > -1:
                        s = new_line.find('\dango')
                        e = max(new_line[s:].find('}'), 0)
                        if 'SEEN0415' in filename:
                            print(new_line[:s])
                        if new_line[:s]:
                            new_lines.append(new_line[:s] + '\n')
                            string_idx += 1
                        new_line = new_line[s+e+1:]
                        if new_line.startswith(' '):
                            new_line = '\\' + new_line
                        if new_line.strip():
                            new_line = '<' + ('0000' + str(string_idx))[-4:] + '> ' + new_line
                    if len(line) > 7:
                        new_lines.append(new_line)
                        string_idx += 1
            file_new.writelines(new_lines)
