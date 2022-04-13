#file without space #未成功
f = open('220406.txt','w')
txt = f.write('https://www.google.com/https://www.youtube.com/https://edition.cnn.com/')
f.close()

f1 = open('220406.txt','r')
arr1 = f1.readlines()
print('1: ',arr1)
txt1 = ''.join(arr1)
print('2: ',txt1)

import re
x = re.findall(r'(?:https://).*',txt1)
print('3: ',x)

y = re.search(r'(https://).*',txt1)
print('4: ',y.group())

z = re.search(r'https?://[\w-]+(\.[\w-]+)+/?',txt1) #T的regex
print('5: ',z)

txt6 = re.compile(r'https?://[\w-]+(\.[\w-]+)+/?')
print('6: ',txt6.search(txt1).group())

i = re.findall(r'https://',txt1)
print('7: ',i)

j = re.findall(r'(https://).*+[^https://]',txt1)
print('8: ',j)
