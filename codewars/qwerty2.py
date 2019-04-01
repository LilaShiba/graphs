s1 = "qwertyuiopqwertyuiop" #10
s2 = "asdfghjklasdfghjkl" #9
s3 = "zxcvbnm,.zxcvbnm,." #9
s3_1 = "ZXCVBNM<>ZXCVBNM<>"

def encrypt(text, encryptKey):
    encryptKey = str(encryptKey).zfill(3)
    ans = ''
    for i in text:
        if i in s1:
            ans += s1[s1.index(i)+int(str(encryptKey)[0])]
        elif i.lower() in s1:
            ans += s1[s1.index(i.lower())+int(str(encryptKey)[0])].upper()
        elif i in s2:
            ans += s2[s2.index(i)+int(str(encryptKey)[1])]
        elif i.lower() in s2:
            ans += s2[s2.index(i.lower())+int(str(encryptKey)[1])].upper()
        elif i in s3:
            ans += s3[s3.index(i)+int(str(encryptKey)[2])]
        elif i.lower() in s3:
            ans += s3_1[s3.index(i.lower())+int(str(encryptKey)[2])].upper()
        else:
            ans += i
    return ans

def decrypt(text, encryptKey):
    encryptKey = str(encryptKey).zfill(3)
    ans = ''
    for i in text:
        if i in s1:
            ans += s1[s1.index(i)-int(str(encryptKey)[0])]
        elif i.lower() in s1:
            ans += s1[s1.index(i.lower())-int(str(encryptKey)[0])].upper()
        elif i in s2:
            ans += s2[s2.index(i)-int(str(encryptKey)[1])]
        elif i.lower() in s2:
            ans += s2[s2.index(i.lower())-int(str(encryptKey)[1])].upper()
        elif i in s3:
            ans += s3[s3.index(i)-int(str(encryptKey)[2])]
        elif i.lower() in s3:
            ans += s3_1[s3.index(i.lower())-int(str(encryptKey)[2])].upper()
        elif i in s3_1:
            ans += s3[s3_1.index(i)-int(str(encryptKey)[2])].upper()
        else:
            ans += i
    return ans
