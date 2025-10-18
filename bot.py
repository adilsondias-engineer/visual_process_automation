import cv2 as cv
import numpy as np
import os
from time import time
from browser import Browser
from vision import Vision
from time import sleep
import pyautogui
import logging

class Bot:

    def __init__(self):
        pass

    def get_screen_position(self,pos,w,h,target):
    
        x = 0#12
        y = 0#148 
        # account for the window border and titlebar and cut them off
        if(target=='oks'):
            x = pos[0]#12
            y = pos[1]#148 
        elif(target=='closeWindowBtn'):
            x = pos[0]#12
            y = pos[1] #148 
        elif(target=='collectBtn'):
            x = pos[0]#12
            y = pos[1] + 40#148 
        elif(target=='trainButtons'):
            x = pos[0] + 12
            y = pos[1] + int(h/2)#148 
        elif(target=='tavernFullBtn'):
            x = pos[0]#12
            y = pos[1] + h * 2#148 
        elif(target == '5minutesJob'): 
            #: or target == 'collectall'    
            x = (pos[0] + int(w/2)) - 20 #12
            y = pos[1]#148 
        elif(target == 'collectall'): 
            #: or target == 'collectall'    
            x = (pos[0] + int(w/2)) - 30 #12
            y = pos[1] + int(h/2) #148 
        else: #(target=='coins'):
            x =  pos[0] #- 5 # int(w/2) # center - 5
            y =  pos[1] + h # * 2 # int(h/2) + h  #center + h

        logging.info('needle %s  pos X: %s, pos Y: %s ', target, pos[0], pos[1])
        #logging.info('pos X, pos Y: ',pos[0], pos[1])
    # w1 = pos[0] - (border_pixels * 2)
    # h1 =  pos[1] - titlebar_pixels - border_pixels
    # cropped_x = border_pixels
    # cropped_y = titlebar_pixels
    # set the cropped coordinates offset so we can translate screenshot
    # images into actual screen positions
    #offset_x = w1 + cropped_x
    # offset_y = h1 + cropped_y
        return  (x, y)
        #return  (pos[0] , pos[1] )

    def run(self, points,target,w,h):
            for c in points:
                screen_x, screen_y = self.get_screen_position(c,w,h,target)
                logging.info('needle %s  size: %s', target, pyautogui.size())
                logging.info('needle %s screen_x: %s, screen_y: %s',target, screen_x, screen_y)
                #logging.info('clicking %s', pyautogui.click(screen_x, screen_y, duration=0.5))
                
                logging.info('needle %s mouse position before move: %s',target, pyautogui.position())
                #logging.info('\b' * len(positionStr), end='')
                ''' if( screen_x > windowW ):
                    logging.info('needle %s dragging right: %s',target, screen_x)
                    pyautogui.drag( screen_x - windowW , 0 , 2, button='left')
                    break
                if(screen_x < 0 ):
                    logging.info('needle %s dragging left: %s',target, screen_x)
                    pyautogui.drag( windowW - screen_x , 0 , 2, button='left')
                    break
                if( screen_y > windowH ):
                    logging.info('needle %s dragging up: %s',target, screen_y)
                    pyautogui.drag( 0, windowH - screen_y , 2, button='left')
                    break
                if( screen_y < 0 ):
                    logging.info('needle %s dragging up: %s',target, screen_y)
                    pyautogui.drag( 0, screen_y - windowH, 2, button='left')
                    break
                '''
                pyautogui.moveTo(x=screen_x, y=screen_y,  duration=3.0)
                # short pause to let the mouse movement complete
                sleep(2)
                logging.info('needle %s mouse position after move: %s',target, pyautogui.position())
                logging.info('needle %s clicking %s',  target, pyautogui.click()) # clicks=1, interval=0.2, x=screen_x, y=screen_y,  button='left'
                sleep(2)
                if(target =='sleeps' or target == 'trainButtons' or target == 'trainedbtn' or target == '5minutesJob' or target == 'collectall'):
                    break

    def runOnce(self, points,target,w=0,h=0):
        screen_x, screen_y = points
        if(target == 'tavernFullBtn'):
            screen_x, screen_y = self.get_screen_position(points,w,h,target)
        
        logging.info('needle %s size: %s',target, pyautogui.size())
        logging.info('needle %s screen_x: %s, screen_y: %s', target, screen_x, screen_y)
        pyautogui.moveTo(x=screen_x, y=screen_y ,  duration=3.0)
    
        logging.info('needle %s clicking %s', target, pyautogui.click(x=screen_x, y=screen_y))
        sleep(2)
        #x, y = pyautogui.position()
        #positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        #logging.info(positionStr)
        #pyautogui.moveTo(x=screen_x, y=screen_y, duration=5.0)
        # short pause to let the mouse movement complete
        #sleep(5)
        #logging.info('clicking %s',  pyautogui.click(duration=0.5))
        #sleep(2)

    def go(self):

        # initialize the WindowCapture class
        #wincap = WindowCapture('Albion Online Client')
        # initialize the Vision class
        vision_coin = Vision('images/coin6.png')
        #coinsImg = 'images/coin6.png'
        vision_collectall = Vision('images/collectAll.png')
        vision_5minutesJob = Vision('images/5minutesJob.png')

        vision_tools = Vision('images/tools2.png')
        #toolsImg = 'images/tools1.png'
        vision_sleep = Vision('images/sleep3.png')
        #sleepingImg =  'images/sleep2.png'
        #vision_produceButton = Vision('images/produce2Btn.png')#,method=cv.TM_CCORR_NORMED)
        produceButtonImg = 'images/produceBtn.png'
        #vision_OkButton = Vision('images/ok.png')#,method=cv.TM_CCORR_NORMED)
        OkButtonImg = 'images/ok.png'
        vision_trainButton = Vision('images/train.png')#,method=cv.TM_CCORR_NORMED)
        trainButtonImg = 'images/train.png'
        vision_trainedButton = Vision('images/trained3.png')#,method=cv.TM_CCORR_NORMED)
        trainedButtonImg = 'images/trained3.png'
        #vision_questCompletedBtn = Vision('images/questCompleted.png')
        questCompletedBtnImg = 'images/questCompleted.png'
        vision_collectBtn = Vision('images/collectBtn1.png')
        collectBtnImg = 'images/collectBtn.png'
        vision_completedGoodsBtn = Vision('images/completedGoods1.png','images/completedGoodsStar.png')
        #completedGoodsBtnImg = 'images/completedGoods.png'
        vision_closeWindowBtn = Vision('images/closeWindow1.png')
        #closeWindowBtnImg = 'images/closeWindow2.png'
        vision_tavernFullBtn = Vision('images/tavernfull.png')
        tavernFullBtnImg = 'images/tavernfull.png'
        #vision_tavernRoomBtn = Vision('images/tavernroom.png')
        tavernRoomBtnImg = 'images/tavernroom.png'
        #vision_collectTaverncoinsBtn = Vision('images/collectTaverncoins.png')
        collectTaverncoinsBtnImg = 'images/collectTaverncoins.png'
        #vision_collectEvent3 = Vision('images/event3.png')
        collectEvent3Img = 'images/event3.png'

        windowW = 1920
        windowH = 1080

        browser = Browser('https://en14.forgeofempires.com/game/index', windowW, windowH, 'Game', '<YOUR_USERN_NAME', '<YOUR_PASSWORDS>', '<WORLD_NAME')  
        #                                                                                  windowName, userName, userPassword, world
        browser.openSite()

        sleep(10)

        browser.login()
        sleep(10)
        loop_time = time()

        imgNumber = 0

        clickedTavernfull = False
        clickedTavernRoom = False
        clickedSleeps = False
        clickedQuestCompleted = False

        browser.fullScreen()


        sleep(2)

        oks = []
        oks = pyautogui.locateCenterOnScreen(OkButtonImg, confidence=0.8)
        logging.info('OK: %s', oks)
        if(oks):
            self.runOnce(oks,'oks')
            oks = [] 

        sleep(5)

        #drag the mouse left -140 pixels right and down 100 pixels over 2 seconds while holding down the right mouse button
        #pyautogui.drag(-180, -140, 2, button='left')
        #pyautogui.drag(100, 0, 2, button='left')

        screenScrolled = False
        paused = False


        coins = [] 
        tools = []
        sleeps = []
        trainButtons = []
        trainedButton = []
        productionBtn = []
        questCompletedBtn = []
        collectBtn = []
        completedGoodsBtn  = []
        closeWindowBtn   = []
        collectTaverncoinsBtn   = []
        tavernFullBtn   = []
        tavernRoomBtn  = []
        collectEvent3 = []

        while(True):


            if(not screenScrolled):
                #make sure the screen is zoomed out after initial screens/dialogs
                pyautogui.scroll(4)  # scroll up X "clicks"
                screenScrolled = True

            logging.info('Paused: %s', paused)

            keys = cv.waitKey(2) & 0xFF
            if cv.waitKey(2) == ord('h'):
                cv.destroyAllWindows()
                break
                
            elif keys == ord('p') and not paused:
                print('p is pressed')
                paused = True
                continue
            elif keys == ord('o'):
                print('o is pressed')
                paused = False

            logging.info(' ------------- start loop -------------')
            # get an updated image of the game
            # screenshot = browser.getScreenshot(imgNumber)
            logging.info(' ------------- new screenshot -------------')
            


            oks = pyautogui.locateCenterOnScreen(OkButtonImg, confidence=0.8)
            logging.info('OK: %s', oks)
            if(oks):
                self.runOnce(oks,'oks')
                oks = [] 
                #continue  
        
            if(not clickedQuestCompleted):
                questCompletedBtn = pyautogui.locateCenterOnScreen(questCompletedBtnImg, confidence=0.8)
                logging.info('questCompletedBtn: %s', questCompletedBtn)
                if(questCompletedBtn):
                    self.runOnce(questCompletedBtn,'questCompleted')
                    questCompletedBtn = []
                    clickedQuestCompleted = True

            if(clickedQuestCompleted):
                sleep(2) #wait popup
                #collectBtn = pyautogui.locateCenterOnScreen(collectBtnImg, confidence=0.7)
                screenshot = browser.getScreenshot(imgNumber)
                collectBtn = vision_collectBtn.findMultiple(screenshot, 0.7, 'rectangles',imgNumber,'collectBtn')
                imgNumber = imgNumber +1
                logging.info('collectBtn: %s', collectBtn)

            # logging.info('autocollectBtn: %s', collectBtn)
                if(collectBtn):
                    self.run(collectBtn,'collectBtn',vision_collectBtn.needle_w, vision_collectBtn.needle_h)
                    collectBtn = []
                    clickedQuestCompleted = False
                    #continue


            screenshot = browser.getScreenshot(imgNumber)
            collectallButton = vision_collectall.findMultiple(screenshot, 0.6, 'rectangles',imgNumber,'collectall')
            
            logging.info('collectallButton: %s', collectallButton)
            #logging.info('trainedAuto: %s', trainedButtonAuto)
            if(collectallButton):
                self.run(collectallButton,'collectall',vision_collectall.needle_w,vision_collectall.needle_h)
                collectallButton = []
                #continue
                screenshot = browser.getScreenshot(imgNumber)
                fiveMinutesJobButton = vision_5minutesJob.findMultiple(screenshot, 0.6, 'rectangles',imgNumber,'5minutesJob')
                logging.info('fiveMinutesJobButton: %s', fiveMinutesJobButton)
                #logging.info('trainedAuto: %s', trainedButtonAuto)
                if(fiveMinutesJobButton):
                    self.run(fiveMinutesJobButton,'5minutesJob',vision_5minutesJob.needle_w,vision_5minutesJob.needle_h)
                    fiveMinutesJobButton = []


            '''
            tavernFullBtn = pyautogui.locateCenterOnScreen(tavernFullBtnImg, confidence=0.8)
            logging.info('tavernFullBtn: %s', tavernFullBtn)
            if(tavernFullBtn and not clickedTavernfull):
                runOnce(tavernFullBtn,'tavernFullBtn',vision_tavernFullBtn.needle_w, vision_tavernFullBtn.needle_h)
                tavernFullBtn = []
                clickedTavernfull = True
                #continue

                if(clickedTavernfull):
                    tavernRoomBtn = pyautogui.locateCenterOnScreen(tavernRoomBtnImg, confidence=0.8)
                    logging.info('tavernRoomBtn: %s', tavernRoomBtn)

                    if(tavernRoomBtn):
                        runOnce(tavernRoomBtn,'tavernRoomBtn')
                        tavernRoomBtn = []
                        clickedTavernRoom = True
                        #continue
                    if(clickedTavernRoom):
                        collectTaverncoinsBtn = pyautogui.locateCenterOnScreen(collectTaverncoinsBtnImg, confidence=0.8)
                        logging.info('collectTaverncoinsBtn: %s', collectTaverncoinsBtn)
                        if(collectTaverncoinsBtn):
                            runOnce(collectTaverncoinsBtn,'collectTaverncoinsBtn')
                            collectTaverncoinsBtn = []
            
                clickedTavernfull = False
                clickedTavernRoom = False
            
            if(not clickedSleeps and not clickedQuestCompleted):
                screenshot = browser.getScreenshot(imgNumber)
                coins = vision_coin.findMultiple(screenshot, 0.7, 'rectangles',imgNumber,'coins')
                imgNumber = imgNumber +1
                logging.info('coins: %s', len(coins))

                if(coins):
                    run(coins,'coins',vision_coin.needle_w,vision_coin.needle_h)
                    coins = []
                    #continue

            if(not clickedSleeps and not clickedQuestCompleted):
                screenshot = browser.getScreenshot(imgNumber)
                tools = vision_tools.findMultiple(screenshot, 0.6, 'rectangles',imgNumber,'tools')
                imgNumber = imgNumber +1
                logging.info('tools: %s', tools)

                if(tools):
                    run(tools,'tools',vision_tools.needle_w,vision_tools.needle_h)
                    tools = []
                    #continue '''
            
            logging.info('clickedSleeps 1: %s', str(clickedSleeps))
            if(not clickedSleeps and not clickedQuestCompleted):
                screenshot = browser.getScreenshot(imgNumber)
                sleeps = vision_sleep.findMultiple(screenshot, 0.5, 'rectangles',imgNumber,'sleeps')
                imgNumber = imgNumber +1
                logging.info('sleeps: %s', sleeps)
                if(sleeps):
                    clickedSleeps = True
                    self.run(sleeps,'sleeps',vision_sleep.needle_w,vision_sleep.needle_h)
                    sleeps=[]
                    #continue
            '''
            if(not clickedSleeps and not clickedQuestCompleted):
                screenshot = browser.getScreenshot(imgNumber)
                completedGoodsBtn = vision_completedGoodsBtn.findMultiple(screenshot, 0.6, 'rectangles',imgNumber,'completedGoodsBtn')
                imgNumber = imgNumber +1
                logging.info('completedGoodsBtn: %s', completedGoodsBtn)

                if(completedGoodsBtn ):
                    run(completedGoodsBtn,'completedGoodsBtn',vision_completedGoodsBtn.needle_w, vision_completedGoodsBtn.needle_h)
                    completedGoodsBtn = []
                    #continue

            #coinsAuto =list(pyautogui.locateAllOnScreen(coinsImg, confidence=0.7))
            #tools =list(pyautogui.locateAllOnScreen(toolsImg, confidence=0.6))
            #sleeps =list(pyautogui.locateAllOnScreen(sleepingImg, confidence=0.6))

            if(clickedSleeps):
                #trainButtons = pyautogui.locateCenterOnScreen(trainButtonImg, confidence=0.7)
                trainButtons = vision_trainButton.findMultiple(screenshot, 0.7, 'rectangles',imgNumber,'trainButtons')
                logging.info('train: %s', trainButtons)

                if(trainButtons):
                    while(trainButtons):
                        run(trainButtons,'trainButtons',vision_trainButton.needle_w,vision_trainButton.needle_h)
                        trainButtons = vision_trainButton.findMultiple(screenshot, 0.7, 'rectangles',imgNumber,'trainButtons')
                        #trainButtons = pyautogui.locateCenterOnScreen(trainButtonImg, confidence=0.8)

                productionBtn = pyautogui.locateCenterOnScreen(produceButtonImg, confidence=0.7)
                logging.info('productions: %s', productionBtn)

                if(productionBtn):
                    while(productionBtn):
                        runOnce(productionBtn,'productionbtn')
                        productionBtn = pyautogui.locateCenterOnScreen(produceButtonImg, confidence=0.8)
                    
                clickedSleeps = False
                #continue
            trainedButton = vision_trainedButton.findMultiple(screenshot, 0.6, 'rectangles',imgNumber,'trainedbtn')
            #trainedButtonAuto = list(pyautogui.locateAllOnScreen(trainedButtonImg, confidence=0.6))
            logging.info('trained: %s', trainedButton)
            #logging.info('trainedAuto: %s', trainedButtonAuto)
            if(trainedButton):
                run(trainedButton,'trainedbtn',vision_trainedButton.needle_w,vision_trainedButton.needle_h)
                trainedButton = []
                #continue

            #completedGoodsBtn =list(pyautogui.locateAllOnScreen(completedGoodsBtnImg, confidence=0.6))
            
            collectEvent3 = pyautogui.locateCenterOnScreen(collectEvent3Img, confidence=0.8)
            logging.info('collectEvent3: %s', collectEvent3)
            if(collectEvent3):
                runOnce(collectEvent3,'collectEvent3')
                collectEvent3 = []
            '''

            logging.info('clickedSleeps 2: %s', str(clickedSleeps))

            if(clickedSleeps):

                productionBtn = pyautogui.locateCenterOnScreen(produceButtonImg, confidence=0.7)
                logging.info('productions: %s', productionBtn)

                if(productionBtn):
                    while(productionBtn):
                        self.runOnce(productionBtn,'productionbtn')
                        productionBtn = pyautogui.locateCenterOnScreen(produceButtonImg, confidence=0.7)


                #trainButtons = vision_trainButton.findMultiple(screenshot, 0.6, 'rectangles',imgNumber,'trainButtons')
                trainButtons = pyautogui.locateCenterOnScreen(trainButtonImg, confidence=0.6)
                logging.info('train: %s', trainButtons)
                #logging.info('trainAuto: %s', trainButtonsAuto)

                if(trainButtons):
                    while(trainButtons):
                        self.runOnce(trainButtons,'trainButtons')
                        trainButtons = pyautogui.locateCenterOnScreen(trainButtonImg, confidence=0.6)
                        #self.run(trainButtons,'trainButtons',vision_trainButton.needle_w,vision_trainButton.needle_h)
                        #trainButtons = vision_trainButton.findMultiple(screenshot, 0.6, 'rectangles',imgNumber,'trainButtons')
                        #trainButtons = pyautogui.locateCenterOnScreen(trainButtonImg, confidence=0.8)

                #clickedSleeps = False


            closeWindowBtn = vision_closeWindowBtn.findMultiple(screenshot, 0.7, 'rectangles',imgNumber,'closeWindowBtn')
            #closeWindowBtn = pyautogui.locateCenterOnScreen(closeWindowBtnImg, confidence=0.8)
            logging.info('closeWindowBtn: %s', closeWindowBtn)
            if(closeWindowBtn):
                self.run(closeWindowBtn,'closeWindowBtn',vision_closeWindowBtn.needle_w,vision_closeWindowBtn.needle_h)
                closeWindowBtn = []
                #continue


            #points = []    
            clickedSleeps = False
            clickedTavernfull = False
            clickedTavernRoom = False
            clickedQuestCompleted = False
            # debug the loop rate
            #logging.info('FPS {}'.format(1 / (time() - loop_time)))
            loop_time = time()
            # press 'q' with the output window focused to exit.
            # waits 1 ms every loop to process key presses
            logging.info(' ------------- end loop -------------')

            logging.info('Done.')



