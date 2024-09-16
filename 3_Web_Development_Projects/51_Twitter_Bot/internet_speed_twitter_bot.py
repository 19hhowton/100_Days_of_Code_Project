from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv 

load_dotenv("51_Twitter_Bot\.env")

USERNAME = os.getenv("TW_USERNAME")
PASSWORD = os.getenv("TW_PASSWORD")
PROMISED_DOWN = os.getenv("PROMISED_UP")
PROMISED_UP = os.getenv("PROMISED_DOWN")

class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self):
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        speedtest_url = "https://www.speedtest.net/"
        self.driver.get(speedtest_url)
        
        time.sleep(2)
        cookie_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler").click()
        go_button = self.driver.find_element(By.CLASS_NAME, value="js-start-test").click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text
        
        print(f"Internet speed is: {self.down}, {self.up}")
        

    def tweet_at_provider(self):
        time.sleep(2)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        twitter_url = "https://x.com/i/flow/login"
        self.driver.get(twitter_url)

        time.sleep(5)
        username_textbox = self.driver.find_element(By.XPATH, 
                                                 value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        username_textbox.send_keys(f"{USERNAME}")
        next_button = self.driver.find_element(By.XPATH, 
                                                 value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_button.click()

        time.sleep(3)
        password_textbox = self.driver.find_element(By.XPATH, 
                                                    value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_textbox.send_keys(f"{PASSWORD}")
        
        login_button = self.driver.find_element(By.XPATH, 
                                                    value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login_button.click()

        time.sleep(3)
        cookies_button = self.driver.find_element(By.XPATH, 
                                                   value='//*[@id="layers"]/div/div/div/div/div/div[2]/button[1]')
        cookies_button.click()

        draft_textbox = self.driver.find_element(By.XPATH,
                                                    value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div') 
        
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        
        draft_textbox.send_keys(tweet)

        post_button = self.driver.find_element(By.XPATH, 
                                               value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        
        post_button.click()
        
        time.sleep(10)

        self.driver.quit()
        