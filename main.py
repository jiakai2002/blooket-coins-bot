from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import undetected_chromedriver as uc

import time
from datetime import datetime
import pyautogui

# *** EDIT LOGIN DETAILS ****
# don't worry, only you can see this
email = "insert_your_email"
password = "insert_your_password"

options = Options()
# bug to be fixed: detach option not regonized
# options.add_experimental_option("detach", True)
driver = uc.Chrome(options=options)


def spin_wheel():
    while True:
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div/div[3]/div/div[2]/div/div/div[6]")))
            driver.find_element(
                By.XPATH, "/html/body/div/div/div/div[3]/div/div[2]").click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/div[3]/div/div[3]/div"))).click()
            print(datetime.now().time().strftime(
                "[%H:%M:%S]"), "Spun daily wheel")
            break
        except TimeoutException:
            print(datetime.now().time().strftime(
                "[%H:%M:%S]"), "Daily wheel unavailable")
            break


# log in to blooket
driver.get("https://id.blooket.com/login")
driver.maximize_window()
wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[4]/input")))
driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[4]/input").send_keys(email)
driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[5]/input").send_keys(password)
driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div[2]/form/input").click()
time.sleep(4)
print(datetime.now().time().strftime(
    "[%H:%M:%S]"), "Logged in to blooket")

# my sets then host
driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/a[7]").click()
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[7]/div[3]/div/div[10]/div[3]"))).click()
time.sleep(4)

# in host tab, select game mode and host game
hostURl = driver.window_handles[1]
driver.switch_to.window(hostURl)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[3]/div[2]/div/div[9]"))).click()
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[3]/div[3]/div[2]/div[2]"))).click()

# set time and host now
time_input = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[3]/div[2]/div[4]/input")))
driver.execute_script("arguments[0].value = ''", time_input)
time_input.send_keys('1')
time.sleep(1)
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div[3]/div[2]/div[2]").click()
print(datetime.now().time().strftime(
    "[%H:%M:%S]"), "Cafe game hosted")

# copy game code
code = wait.until(EC.presence_of_element_located(
    (By.ID, "idNum"))).text

# in game tab, enter cafe game
gameURL = driver.window_handles[0]
driver.switch_to.window(gameURL)
driver.get("https://play.blooket.com/play")

# enter game code
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/div[1]/input"))).send_keys(code)
driver.find_element(
    By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/div[2]").click()
time.sleep(4)

# enter name
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
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/div/div[3]/form/div[2]/div/div[2]/div[3]"))).click()
wait.until(EC.element_to_be_clickable(
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
    "[%H:%M:%S]"), "Autoclicking now for 6 minutes")
end_time = time.time() + 60
while True:
    pyautogui.click(x, y)
    if time.time() > end_time:
        break

while True:
    try:
        time.sleep(8)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div[3]/div")))
        # spin wheel if available
        spin_wheel()
        # click thanks
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/div[3]/div/div[2]/div[2]/div"))).click()
        print(datetime.now().time().strftime(
            "[%H:%M:%S]"), "Rewards collected!")
        break
    except TimeoutException:
        # daily limit reached
        print(datetime.now().time().strftime(
            "[%H:%M:%S]"), "Daily limit reached, no coins rewarded")
        break

print(datetime.now().time().strftime(
    "[%H:%M:%S]"), "Done. Thankyou for using KaiBot!")

x = input("hi:")
