import os
from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as py
import schedule

w, h = py.size()
print(w, h)
s60 = 60
h8 = 8
url = 'https://embed.radio.co/player/7881434.html'
cmd = f'chromium {url} -kiosk'

def wait_for_page_load(driver, timeout=30):
    # Wait for the page to be loaded completely
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

def run():
    print('called')
    driver = webdriver.Chrome()
    driver.get(url)
    wait_for_page_load(driver)
    
    os.system(cmd)

def caller():
    os.system('sudo killall chromium')
    Thread(target=run, args=()).start()
    time.sleep(20)
    py.moveTo(int(0.5 * w), int(0.5 * h))
    py.click(int(0.5 * w), int(0.5 * h))
    time.sleep(13)
    py.moveTo(9, 9)
    py.click(9, 9)

schedule.every(h8).hours.do(caller)
caller()

while True:
    schedule.run_pending()
    time.sleep(1)
