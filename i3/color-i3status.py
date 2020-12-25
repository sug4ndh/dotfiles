#!/usr/bin/python
import fileinput
import os
from os.path import expanduser
home = expanduser("~")

def get_new_col():
    p=home+'/.cache/wal/colors.sh'
    print('Getting colors from'+p)
    with open(p, "r") as f:
        searchlines = f.readlines()
    f.close()
    searchphrase = ['color'+str(i)+'=' for i in range(16)]
    new_cols = {}
    for col in searchphrase:
        for line in searchlines:
            if col in line:new_cols[line.split('=')[0]]=line.split('=')[1].replace('\n','')
    return new_cols

def find_col_in_i3status():
    p=home+'/.config/i3/i3status.conf'
    print('finding colors in '+p)
    with open(p, "r") as f:
        searchlines = f.readlines()
    f.close()
    searchphrase = ['c'+str(i)+'=' for i in range(1,3)]
    old_cols = {}
    for col in searchphrase:
        for line in searchlines:
            if col in line:
                old_cols[line.split('=')[0]]=line.split('=')[1].replace('\n','')
    for col,hex in old_cols.items():
        print('Found '+col+' '+hex)
    return old_cols

def  update_col():
    old_cols = find_col_in_i3status()
    new_cols = get_new_col()
    #print(new_cols)
    #print(old_cols)
    p=home+'/.config/i3/i3status.conf'
    lines = []
    with open(p) as f:
        print('Changing {o} to {n} in i3status'.format(o=old_cols['# c1'], n=new_cols['color1']))
        newText=f.read().replace(old_cols['# c1'], new_cols['color1'])
    with open(p, "w") as f:
        f.write(newText)
    with open(p) as f:
        print('Changing {o} to {n} in i3status'.format(o=old_cols['# c2'], n=new_cols['color6']))
        newText=f.read().replace(old_cols['# c2'], new_cols['color6'])
    with open(p, "w") as f:
        f.write(newText)

    #with open(FileName, "w") as f:
    #    f.write(newText)
    #
    #    print('Changing {o} to {n} in i3status'.format(o=old_cols['# c2'], n=new_cols['color7']))
    #    s = s.replace(old_cols[1], new_cols[7])
    f.close()

if __name__=='__main__':
    update_col()
