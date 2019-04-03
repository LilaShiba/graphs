def string_incrementer(letters):
    ints = list("1234567890")
    count = len(letters)-1
    for x in letters:
        if letters[count] in ints:
            count -= 1
        else:
            num = letters[count+1:]
            if num[0] != '0' or num[0] != '9':
                num = int(num) + 1
                letters = letters[:count+1]
                num = str(num)
                ans = letters+num
                return ans
            elif num[0] == '9':
                




print(string_incrementer('o37b59'))
