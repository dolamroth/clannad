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

i = 0
codes = {}
string_idx = 0
for filename in os.listdir(os.path.join('.', 'ru')):
    with open(os.path.join('.', 'ru', filename), 'rt+', encoding="utf-8") as file_orig:
        lines = file_orig.readlines()
        string_idx = 0
        filebase = filename[:-4]
        codes[filebase] = {}
        flag1 = False
        for line in lines:
            if line.strip() == '':
                flag1 = False
            elif line.startswith('//') and not flag1:
                flag1 = True
            elif line.startswith('//'):
                pass
            elif not flag1:
                pass
            else:
                new_line = line
                while new_line.find('\dango') > -1:
                    s = new_line.find('\dango')
                    e = max(new_line[s:].find('}'), 0)
                    dango_word = new_line[s+7:s+e]
                    dango_translation = dango_word
                    for char in change:
                        dango_translation = dango_translation.replace(char, change[char])
                    codes[filebase][string_idx] = dango_translation
                    if new_line[s+e+1:].strip():
                        string_idx += 1
                    i += 1
                    new_line = new_line[s+e+1:]
                if len(line) > 7:
                    string_idx += 1


k = 0
for filename in os.listdir(os.path.join('.', 'org')):
    with open(os.path.join('.', 'org', filename), 'rt+', encoding="utf-8") as file_orig:
        with open(os.path.join('.', 'org_new', filename), 'wt+', encoding="utf-8") as file_new:
            lines = file_orig.readlines()
            new_lines = []
            flag = False
            filebase = filename[:-4]
            i = 0
            while i < len(lines):
                line = lines[i]
                for key in codes[filebase]:
                    if 'res<{}>'.format( ('0000' + str(key))[-4:] ) in line and i < len(lines) - 1 and 'farcall_with' in lines[i+1]:
                        new_lines.append(line)
                        k += 1
                        i += 1
                        line = lines[i]
                        try:
                            assert line.count("'") >= 2
                        except:
                            print(filebase, lines[i-1], line)
                            raise 
                        b = line.find("'")
                        e = line[b+1:].rfind("'")
                        patched_line = line[:b+1] + codes[filebase][key] + line[b+e+1:]
                new_lines.append(line)
                i += 1
            file_new.writelines(new_lines)
print(k)