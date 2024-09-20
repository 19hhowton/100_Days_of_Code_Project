from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time
import os
from dotenv import load_dotenv 

load_dotenv("52_Instagram_Bot\.env")

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")

class InstaFollower():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.option)
        self.action = ActionChains(self.driver)

    def login(self):
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()

        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(2)
        # cookie_button = self.driver.find_element(By.XPATH,
        #                                          value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        # cookie_button.click()

        cookie_button = ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                                    ((By.CSS_SELECTOR, 
                                                    "._a9--._ap36._a9_0"))).click()
        
        time.sleep(1)
        username_textbox = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="loginForm"]/div/div[1]/div/label/input')
                                                        
        username_textbox.send_keys(f"{USERNAME}")
        
        password_textbox = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_textbox.send_keys(f"{PASSWORD}")

        login_button = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        time.sleep(3)
        save_login = ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                                    ((By.CSS_SELECTOR, 
                                                    ".x1i10hfl.xjqpnuy"))).click()
        
        notifications_button = ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                                    ((By.CSS_SELECTOR, 
                                                    "._ap36._a9_1"))).click()
        print("You're logged in!")
            

    def find_followers(self):
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(5)

        follower_button = self.driver.find_element(By.CSS_SELECTOR, f'ul li div a[href="/{SIMILAR_ACCOUNT}/followers/"]')
        follower_button.click()

        time.sleep(3)        
        xpath_follower_list = '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
        follower_list = self.driver.find_element(By.XPATH, xpath_follower_list)
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_list)
            time.sleep(5)


    def follow(self):
        time.sleep(2)
        follow_button = self.driver.find_elements(By.XPATH, '//div[contains(text(), "Follow")]')
        # Going through the list of follow buttons and following each one respectively
        for follow in follow_button:
            if follow.text == "Following":
                print(follow.text)
            elif follow.text == "Requested":
                print(follow.text)
            elif follow.text == "Follow":
                print(follow.text)
                time.sleep(1)
                self.action.scroll_to_element(follow).click(follow).perform()
                try:
                    time.sleep(1)
                    self.driver.find_element(By.XPATH, '//button[contains(text(), "OK")]').click()
                except NoSuchElementException:
                    pass