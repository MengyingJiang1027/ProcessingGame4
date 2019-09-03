from processing import *

class Card(object):
    def __init__(self, x, y, size_h, size_w, attribute, letterDic):
        self.img = letterDic[attribute]
        self.x = x
        self.y = y
        self.size_h = size_h
        self.size_w = size_w
        self.attribute = attribute

    def display(self):
        image(self.img, self.x, self.y, self.size_w, self.size_h)


    def changePic(self, inputDic, numList):
        image(numList[inputDic[self.attribute]], self.x, self.y, self.size_w, self.size_h)


    def run(self, inputDic, numList):
        if inputDic[self.attribute] < 10:
            self.changePic(inputDic, numList)
        else:
            self.display()
