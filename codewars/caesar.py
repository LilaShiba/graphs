# https://www.codewars.com/kata/break-the-caesar/train/python
def break_caesar(s, shift):
    s = s.lower()
    alpha = dict()
    numeric = dict()
    letters = list('$abcdefghijklmnopqrstuvwxyz')

    for x in range(len(letters)):
        alpha[letters[x]] = x
    print(alpha)

    for x in range(len(letters)):
        numeric[x] = letters[x]
    print(numeric)

    encode = []

    for x in s:
        if x in letters:
            new_letter = alpha[x] + shift
            if new_letter > 26:
                new_letter = new_letter - 26
            encode.append(numeric[new_letter])
    #    #print(encode)
    return encode





print(break_caesar("I Love Pizza",5))
