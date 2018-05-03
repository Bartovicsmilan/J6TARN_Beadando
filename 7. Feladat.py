word='vsrbkeretkaraktereksv'

def PalindromOrNot(word):
    h=len(word)
    p=1
    for i in range(0,h):
        # print(i)
        if i-1==h//2:
            return True
        elif word[i]==word[h-p]:
            # print(word[i])
            # print(word[h - p])
            p+=1
        else:
            return False

# print(PalindromOrNot(word))


def AllFormations(word):
    h=len(word)
    ph=0
    longest=''
    for i in range(h+1):
        for j in range(i+1,h+1):
            if PalindromOrNot(word[i:j]) is True and ph<len(word[i:j]):
                ph=len(word[i:j])
                longest=word[i:j]
    print(longest)

AllFormations(word)
