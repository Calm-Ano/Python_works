
# -*-  coding:utf-8 -*-
import random

def dappun(name):
    li = ['ﾌﾞ','ﾘｭ','ﾘ','ｯ','ﾁ']
    retstr = str()
    retstr += '@{}「'.format(name)
    for i in range(0, 50):
        retstr += random.choice(li)
    retstr += '」'
    return retstr

if __name__ == "__main__":
    name = input("Input target name : ")
    print(dappun(name))
