from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from datetime import datetime
import pyautogui

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

# log in to blooket
driver.get("https://id.blooket.com/login")
driver.maximize_window()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[4]/input")))
driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[4]/input").send_keys("email")
driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[5]/input").send_keys("password")
driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div[2]/form/input").click()
time.sleep(4)
print(datetime.now().time().strftime(
    "[%H:%M:%S]"), "Logged in to blooket")

# my sets then host
driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/a[7]").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[7]/div[3]/div/div[10]/div[3]"))).click()
time.sleep(4)

# in host tab, select game mode and host game
hostURl = driver.window_handles[1]
driver.switch_to.window(hostURl)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[3]/div[2]/div/div[9]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[3]/div[3]/div[2]/div[2]"))).click()

# set time and host now
time_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[3]/div[2]/div[4]/input")))
driver.execute_script("arguments[0].value = ''", time_input)
time_input.send_keys('6')
time.sleep(1)
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div[3]/div[2]/div[2]").click()
print(datetime.now().time().strftime(
    "[%H:%M:%S]"), "Cafe game hosted")

# copy game code
code = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.ID, "idNum"))).text

# in game tab, enter cafe game
gameURL = driver.window_handles[0]
driver.switch_to.window(gameURL)
driver.get("https://play.blooket.com/play")

# submit game code
WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/div[1]/input"))).send_keys(code)
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/div[2]").click()
time.sleep(4)

# choose name
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/div[1]/input").send_keys("KaiBot")
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/div[2]").click()
time.sleep(4)
print(datetime.now().time().strftime(
    "[%H:%M:%S]"), "Player has joined the game")

# in host tab, start game
driver.switch_to.window(hostURl)
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div[3]/div[1]/div[3]").click()
time.sleep(1)
print(datetime.now().time().strftime(
    "[%H:%M:%S]"), "Game started by host")

# in game tab, clear popups
driver.switch_to.window(gameURL)
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div[3]/form/div[2]/div/div[2]/div[3]").click()
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[3]/form/div[2]/div/div"))).click()
time.sleep(1)

# get absolute element location
panel_height = driver.execute_script(
    'return window.outerHeight - window.innerHeight;')
element_location = driver.find_element(
    By.ID, "restock").location
x = element_location["x"] + 150
y = element_location["y"] + panel_height + 44  # chrome controlled label height

# *** PRESS CTRL+ALT+M TO FORCE STOP SCRIPT ***
# *** WARNING: THIS CLOSES BLOOKET! ***
# start autoclick
pyautogui.PAUSE = 0.00001
print(datetime.now().time().strftime(
    "[%H:%M:%S]"), "Autoclicking now for 6 minutes...")
end_time = time.time() + 6 * 60
while True:
    pyautogui.click(x, y)
    if time.time() > end_time:
        break
print(datetime.now().time().strftime(
    "[%H:%M:%S]"), "Done. Thankyou for using KaiBot!")
