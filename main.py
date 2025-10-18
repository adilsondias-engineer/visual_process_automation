import cv2 as cv
import numpy as np
import os
from time import time
from browser import Browser
from vision import Vision
from time import sleep
import pyautogui
import logging
from bot import Bot

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='foe.log', encoding='utf-8', level=logging.INFO)

#logger = logging.getLogger('main')
#handler = logging.FileHandler('foe.log')
#logger.warning('This is a warning')

bot = Bot()

bot.go()