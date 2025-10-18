from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from time import time 
import numpy as np
from PIL import Image
import cv2 as cv
import os
import io
import logging

class Browser:

    #properties
    website = ""
    windowWidth = 0
    windowHeight = 0
    windowName = ""
    userName = ""
    userPassword = ""
    driver = None
    world = ""

    # constructor
    def __init__(self, website, windowWidth, windowHeight, windowName, userName, userPassword, world):
        
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.website = website 
        self.windowName = windowName
        self.userName = userName
        self.userPassword = userPassword
        self.world = world
        #website = 'https://en12.forgeofempires.com/game/index?ref=gob_en_nn_foe_bra_discover_e'
    

        service = Service('chromedriver.exe')
        
        optionsList = Options()
        optionsList.add_argument(r"--user-data-dir=C:\Users\<YOUR_USER>\AppData\Local\Google\Chrome\User Data\Default")
        #provide the profile name with which we want to open browser
        optionsList.add_argument(r'--profile-directory=Default')
        
        #option.add_argument("--headless")#open in full screen
        optionsList.add_argument("--disable-infobars")
        #options.add_argument("start-maximized")
        #options.add_argument("--disable-extensions")
        optionsList.add_argument("--kiosk")#open in full screen
        # Pass the argument 1 to allow and 2 to block
        optionsList.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 2 
        })
        
        
        service.start()
        self.driver = webdriver.Chrome(options=optionsList)

    def openSite(self):
 
        #width = 1920
        #height = 1080
#        WebDriverException
       # self.driver.set_window_size(self.windowWidth, self.windowHeight)
        #self.driver.fullscreen_window()

        self.driver.get(self.website)
        #self.driver.fullscreen_window()
    
    def login(self):
        
        try:
            
            elementUserId = self.driver.find_element(By.ID,'login_userid')
            #elementUserId.send_keys('The Right King')
            elementUserId.send_keys(self.userName)
            elementPassword = self.driver.find_element(By.ID,'login_password')
            #elementPassword.send_keys('arvi1690@Game')
            elementPassword.send_keys(self.userPassword)
            elementLoginBtn = self.driver.find_element(By.ID,'login_Login')
            elementLoginBtn.click()
 
            #assume it's already logged in
            sleep(5)
            logging.info('Already logged')
            #<input type="button" name="play" value="Play" id="play_now_button" class="play_button">
            elemePlayBtn = self.driver.find_element(By.ID,'play_now_button')
            #elemePlayBtn = driver.find_element(By.NAME,'play')
            elemePlayBtn.click()
            #sleep(10)
              
            #worldSelectBtn = driver.find_element(By.ID,'world_selection_list')
                    
            #Select(worldSelectBtn).select_by_visible_text('Mount Killmore')
            #"Mount Killmore"
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//ul[@id='world_selection_list']//li/a[text()='"+ self.world +"']"))).click()  #Mount Killmore 

        except NoSuchElementException:  #spelling error making this code not work as expected
            pass
           
           
           
           
    def getScreenshot(self,imgNumber):       
        #sleep(10)
       #loop_time = time()
        #imgNumber = 0
        # Naming a window
        #cv.namedWindow(self.windowName, cv.WINDOW_NORMAL)
        # while(True):
        screenshot = self.driver.get_screenshot_as_png()
        screenshot = Image.open(io.BytesIO(screenshot))
        screenshot = np.asarray(
            screenshot,
            dtype=np.float32
        ).astype(np.uint8)
        # Convert image from BGR to RGB format
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2RGB)


        #nparr = np.frombuffer(screenshot, np.uint8)
        #img = cv.imdecode(nparr, cv.IMREAD_COLOR)
        #screenshot = np.asarray(img).astype("uint8")
        #screenshot = cv.cvtColor(screenshot,cv.COLOR_RGB2BGR)
        
        #imgNumber = imgNumber +1  
        #cv.resizeWindow(self.windowName, self.windowWidth, self.windowHeight)
        #cv.imshow(self.windowName,screenshot)
        #loop_time = time()
        #driver.get_screenshot_as_file("capture.png")
        #cv.imwrite('results\BrowserGame'+ str(imgNumber) +'.png', screenshot)  
        return screenshot    
    
    
    def fullScreen(self):
        self.driver.fullscreen_window()