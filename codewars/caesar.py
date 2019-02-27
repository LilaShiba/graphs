# https://www.codewars.com/kata/break-the-caesar/train/python

def encrypt(text,s):
  text = text.lower()
  letters = list('$abcdefghijklmnopqrstuvwxyz')
  alpha = dict()
  new_string = []

  # create hash for key = letter value = number
  for x in range(len(letters)):
    alpha[letters[x]] = x

  # traverse text
  for i in range(len(text)):
    if text[i] != ' ':
        char = text[i]
        ans = (alpha[char] + s % 26)
        if ans > 26:
            ans = ans - 26
        new_string.append(letters[ans])
    else:
        new_string.append(' ')

  # return string
  encrypted = ''.join(new_string)
  return encrypted


def decrypt(text,s):
  letters = list('$abcdefghijklmnopqrstuvwxyz')
  alpha = dict()
  new_string = []

  # create hash for key = letter value = number
  for x in range(len(letters)):
    alpha[letters[x]] = x

  # traverse text
  for i in range(len(text)):
    char = text[i]
    ans = (alpha[char] - s % 26)
    if ans <= 0:
      ans = ans + 26
    new_string.append(letters[ans])

  # return string
  encrypted = ''.join(new_string)
  return encrypted


print(decrypt('zy',25))
print(encrypt('Python Warrior',25))
# def break_caesar(s, shift):
#     s = s.lower()
#     alpha = dict()
#     numeric = dict()
#     letters = list('$abcdefghijklmnopqrstuvwxyz')
#
#     for x in range(len(letters)):
#         alpha[letters[x]] = x
#     #print(alpha)
#
#     for x in range(len(letters)):
#         numeric[x] = letters[x]
#     print(numeric)
#
#     encode = []
#
#     for x in s:
#         if x in letters:
#             new_letter = alpha[x] + shift
#             if new_letter > 26:
#                 new_letter = new_letter - 26
#             encode.append(numeric[new_letter])
#         if x == ' ':
#             encode.append(' ')
#     #    #print(encode)
#     return "".join(encode)







#print(break_caesar("ShiBas aRe the Best!!!",5))
