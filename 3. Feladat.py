strings=['Hello','World','in','a','frame']

def leghosszabbstring(srtings):
    l=0
    for i in strings:
        if len(i)>l:
            l=len(i)
    return l

# print(leghosszabbstring(strings))

def ListToFrame(strings):
    h=leghosszabbstring(strings)
    print('*'*(h + 4))
    for i in strings:
        i += ' ' * (h - len(i))
        print('* {0} *'.format(i))
    print('*' * (h + 4))


ListToFrame(strings)