"""
#s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s= "map"
newS = ""
for x in range(len(s)):
    if(ord(s[x]) > 96 and ord(s[x]) < 121):
        newS += chr(ord(s[x]) + 2)
    elif(ord(s[x]) > 120 and ord(s[x]) < 123):
        newS += chr(ord(s[x]) - 24)
    else:
        newS += s[x]
print(newS)
"""
#--------------------------------------------#
from urllib import *

page = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html");