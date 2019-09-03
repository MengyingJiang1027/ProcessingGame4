
from Button import Button
from Card import Card
from Game import Game

def setup():
    global bg, calcuBg, game, frameCounter, monster1, monster2
    global inputDic, numList, letterList, imgList, resultList
    global scr_w, scr_h
    global A, B, C
    global hint_btn
    
    bg = loadImage('./resources/map.png')
    calcuBg = loadImage('./resources/calculator.png')
  
   # 存放游戏结果图片
    resultList = []
    for i in range(5):
        resultList.append(loadImage('./resources/result/' + str(i) + '.png'))
   
    
    #  存放 0 - 9的数字图片
    numList = []
    for i in range(10):
        numList.append(loadImage('./resources/num/' + str(i) + '.png'))
    
    # 存放字母和加号的图片
    letterList = []
    for i in range(4):
        letterList.append(loadImage('./resources/letter/' + str(i) + '.png'))
    
    letterDic = {'letterA':letterList[1], 'letterB':letterList[2], 'letterC':letterList[3]}
    
    # 用户输入内容字典初始化
    A = ''
    B = ''
    C = ''
    inputDic = {'letterA': A, 'letterB':B, 'letterC':C}
    
    # 卡片实例对象存入列表并且display
    imgList = []     
    card0 = Card(760, 460, 30, 25, 'letterB', letterDic)
    card1 = Card(795, 460, 30, 25, 'letterC', letterDic)
    card2 = Card(760, 496, 30, 25, 'letterB', letterDic)
    card3 = Card(795, 496, 30, 25, 'letterC', letterDic)
    card4 = Card(725, 532, 30, 25, 'letterA', letterDic)
    card5 = Card(760, 532, 30, 25, 'letterC', letterDic)
    card6 = Card(795, 532, 30, 25, 'letterC', letterDic)
    
    for i in range(7):
        imgList.append(eval('card' + str(i)))
    
    
    
    
    # 加入提示信息
    Chinese = createFont("LiSu", 35)
    textFont(Chinese)
    
    attr_hint_btn = {"btn_x":720,"btn_y":655,"btn_w":60,"btn_h":60,
                 "msg_x":375,"msg_y":230,"msg_w":500,"msg_h":400}
    
    hint_btn = Button(attr=attr_hint_btn,
                      imgs=["/resources/q_mark.png", "/resources/hint_msg.png"])
    
    
    # 加入小怪
    monster1 = loadImage('./resources/monster1.png')
    monster2 = loadImage('./resources/monster2.png')

    
    scr_w = 960
    scr_h = 720
    frameCounter = 0
    game = Game()
    size(960,720)
    
    
def draw():
    global bg, calcuBg, game, frameCounter, monster1, monster2
    global inputDic, numList, letterList, imgList
    global scr_w, scr_h
    global A, B, C
    global hint_btn
    
    image(bg, 0, 0, scr_w, scr_h)
    image(calcuBg, 700, 400)
    image(letterList[0],721, 503, 30, 25)
    image(monster1, 200, 620, 61, 61)
    image(monster2, 758, 240, 61, 61)
    
    ### 学生输入代码区域 #######
    '''
    A = 1
    B = 5
    C = 0
    '''

    ### 学生输入代码区域 #########
    
    inputDic['letterA'] = A
    inputDic['letterB'] = B
    inputDic['letterC'] = C
    
    game.run(imgList, inputDic, numList)
    updateFrame(game,resultList, hint_btn)


def updateFrame(game,resultList, hint_btn):
    global frameCounter
    
    if game.isReady:
        frameCounter += 1
        if game.isWin:
            image(resultList[1],725, 420, 98, 37)
            if frameCounter > 100:
                noTint()
                image(resultList[3],scr_w//2-50,scr_h//2-150,200,200)
                fill(255)
                textSize(40)
                text(u"恭喜你闯关成功！",scr_w//2-100,scr_h//2+125)
                
        else:
            image(resultList[2],721, 420, 98, 37)
            if frameCounter > 100:
                fill(255)
                textSize(40)
                text(u"哎呀好像结果不正确呢，再想想",scr_w//2-230,scr_h//2+125)
                image(resultList[4],scr_w//2-50,scr_h//2-150,200,200)

    else:
        image(resultList[0],721, 420, 98, 37)
        hint_btn.show(mouseX,mouseY)   
    


    
    
    
    
    
    

    
    
    
    
    


    
    
