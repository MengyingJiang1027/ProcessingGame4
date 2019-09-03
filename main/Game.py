from processing import *

class Game(object):
    def __init__(self):
        self.isReady = False
        self.isWin = False
                
    def check(self,inputDic):
        for key in inputDic:
            if inputDic[key] != '':
                self.isReady = True
            elif inputDic[key] == '' or type(key) is not int or (key > 5 or key < 0):
                inputDic[key] = 11
                self.isWin = False
            
        if inputDic['letterA'] == 1 and inputDic['letterB'] == 5 and inputDic['letterC'] == 0 :
            self.isWin = True
    
                            
    def showResult(self, imgList, inputDic, numList):
        if not self.isReady:
            for img in imgList:
                    img.display()
        
        else:
            for img in imgList:
                    img.run(inputDic, numList)
            if self.isWin:
                print('yes')
            else:
                print('no')
        
    
    def run(self, imgList, inputDic, numList):
        self.check(inputDic)
        self.showResult(imgList, inputDic, numList)
