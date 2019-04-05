r1 = 'qwertyuiopqwertyuiop'
r2 = 'asdfghjklasdfghjkl'
r3 = 'zxcvbnm,.zxcvbnm,.'
r3_1 = 'ZXCVBNM<>ZXCVBNM<>'

def encrpyt(string,shift):
    shift = str(shift).zfill(3)
    ans = ''
    for char in string:
        if char in r1:
            ans +=r1[r1.index(char)+int(str(shift)[0])]
        elif char.lower() in r1:
            ans += r1[r1.index(char.lower())+int(str(shift)[0])].upper()
        if char in r2:
            ans +=r2[r2.index(char)+int(str(shift)[1])]
        elif char.lower() in r2:
            ans += r2[r2.index(char.lower())+int(str(shift)[1])].upper()
    return ans

print(encrpyt('qWeRtYaSdFgHjK',191))
