import re,pyperclip

#extract phone number
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?            # areaCode
(\s|\.|\-)                    # seperator
(\d{3})                       # 3 digit number
(\s|\.|\-)                    # seperator
(\d{4})                       # four digit
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''',re.VERBOSE)

#extract email number
emailRegex = re.compile(r'''(
([a-zA-Z0-9.%+-]+)    #userName
@                     # At the rate
([a-zA-Z0-9.-]+)      # domain name
(\.[a-zA-Z]{2,4})     #extention
 )''',re.VERBOSE)

#put email and phone in a list
text = pyperclip.paste()
matches =[]

print(phoneRegex.findall(text))
print()

for group in phoneRegex.findall(text):
    phoneNum = '-'.join([group[1],group[3],group[5]])
    if group[8]!='':
        phoneNum += 'X'+ group[8]
    matches.append(phoneNum)

print(emailRegex.findall(text))
print()

for group in emailRegex.findall(text):
    matches.append(group[0])

# paste it on the clipboard
if len(matches)>0:

    pyperclip.copy('\n'.join(matches))
    print('Copy to the clipboard: ')
    print('\n'.join(matches))