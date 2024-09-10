""""
I had it working up until the swipe left :( 
I dont know what's going wrong. I need to be more systematic in my approach...

"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import os
from dotenv import load_dotenv 

load_dotenv("50_Tinder_Swiping_Bot\.env")
# username = os.getenv("USER_NAME")
# password = os.getenv("PASSWORD")

## Keep Chrome browser open after program finishes
options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_argument("--start-maximized")
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")
driver = webdriver.Chrome()
driver.set_window_size(1024, 600)
driver.maximize_window()

## Navigate from Tinder to Facebook 
tinder_url = "https://tinder.com/en-GB"
driver.get(tinder_url)

time.sleep(1)
td_cookies = driver.find_element(By.XPATH, value='//*[@id="o1110570119"]/div/div[2]/div/div/div[1]/div[1]/button').click()
time.sleep(1)
td_login = driver.find_element(By.XPATH, value='//*[@id="o1110570119"]/div/div[1]/div/div/div/main/div/div[2]/div/div[3]/div/div/button[2]').click()
time.sleep(1)
td_facebook = driver.find_element(By.XPATH, value='//*[@id="o-617810957"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button').click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(1)
fb_cookies = driver.find_element(By.XPATH, value='//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]').click()

fb_username = driver.find_element(By.ID, value="email").send_keys("19hhowton@gmail.com")
fb_password = driver.find_element(By.ID, value="pass").send_keys("Login4me120!")
fb_login = driver.find_element(By.ID, value="loginbutton").click()

time.sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(3)
continue_button = driver.find_element(By.CLASS_NAME, value='x1i10hfl') 
continue_button.click()

time.sleep(3)
driver.switch_to.window(base_window)
print(driver.title)

# time.sleep(1)
# allow_button = driver.find_element(By.XPATH, value='//*[@id="q2044352340"]/div/div/div/div/div[3]/button[1]').click()

# time.sleep(1)
# notify_button = driver.find_element(By.XPATH, value='//*[@id="q2044352340"]/div/div/div/div/div[3]/button[1]').click()

# #### DENY ####
# time.sleep(30)
# print("DONE WAITING")

# nope_button = driver.find_element(By.CLASS_NAME, value='Bgi($g-ds-background-nope):a')
# nope_button.click()

"""
how to I use the wait feature in selenium? 

XPATH
wont work because id keeps changing
//*[@id="q-522233880"]/div/div[1]/div/div/div/main/div/div/div[1]/div/div[4]/div/div[2]/button'
//*[@id="o1110570119"]/div/div[1]/div/div/div/main/div/div/div[1]/div/div[3]/div/div[2]/button

CLASS
Bgi($g-ds-background-nope):a

Click on the page and then...
ActionChains(driver).key_down(Keys.ARROW_LEFT).key_down(Keys.ARROW_LEFT).perform()
print("NOPE")


"""

"""
THIS WORKED YESTERDAY

td_cookies = driver.find_element(By.XPATH, value='//*[@id="q-522233880"]/div/div[2]/div/div/div[1]/div[1]/button').click()
time.sleep(1)
td_login = driver.find_element(By.XPATH, value='//*[@id="q-522233880"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]').click()
time.sleep(1)
td_facebook = driver.find_element(By.XPATH, value='//*[@id="q2044352340"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button').click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(1)
fb_cookies = driver.find_element(By.XPATH, value='//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]').click()

fb_username = driver.find_element(By.ID, value="email").send_keys("19hhowton@gmail.com")
fb_password = driver.find_element(By.ID, value="pass").send_keys("Login4me120!")
fb_login = driver.find_element(By.ID, value="loginbutton").click()

time.sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(3)
continue_button = driver.find_element(By.CLASS_NAME, value='x1i10hfl')
continue_button.click()

time.sleep(3)
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(1)
allow_button = driver.find_element(By.XPATH, value='//*[@id="q2044352340"]/div/div/div/div/div[3]/button[1]').click()

time.sleep(1)
notify_button = driver.find_element(By.XPATH, value='//*[@id="q2044352340"]/div/div/div/div/div[3]/button[1]').click()
"""

time.sleep(300)

driver.quit()