import os
import re
import fileinput
import translators as ts

re_p = re.compile(r'.*\[p\]')


for root,dirs,files in os.walk("."):
    for file in files:
        #获取文件所属目录
        if root == ".":
            print(os.path.join(root,file))
            filedir = os.path.join(root,file)
            with fileinput.input(files=filedir,inplace=True, backup='.bak', encoding="utf-8") as f:
                for line in f:
                    if re_p.match(line):
                        newtext = ts.google(line[:-4], from_language='ja', to_language='zh-CN', if_use_cn_host=True)
                        newtext = line.replace(line[:-4], newtext)
                        print(newtext,end='')
                    else:
                        print(line,end='')

