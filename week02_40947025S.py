#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def myfunction(inputSTR):
    '''
    這支程式的主要函式(「函式」就是「功能」的意思！)
    '''
    

    myName = inputSTR[0:3]
    myID = inputSTR[4:13]
    '''
    print("我的名字:{}".format(myName))
    print("我的學號:{}".format(myID))
    '''
    inputList = inputSTR.split(" ")

    print("我的名字:{}".format(inputList[0]))
    print("我的學號:{}".format(inputList[1]))


   

    messageSTR = """
    「程式設計與基礎資料型態與中文構詞學」
    整堂課的資訊量爆炸，在知識的海洋裡衝浪
    超過癮的啊啊啊啊！
    """
    #print(messageSTR)


#程式進入點！ week02.py 這支程式從這裡開始「執行」！
if __name__ == "__main__":
    nameSTR = "黃冠棠 40947025S"

    myfunction(nameSTR)
