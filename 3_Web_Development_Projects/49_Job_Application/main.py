import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv 

load_dotenv("49_Job_Application\.env")
username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")

## Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

link = r"https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver.get(link)

try:
  cancel_button = driver.find_element(By.CLASS_NAME, value="modal__dismiss").click()
except:
  pass
finally: 
  signin_button_1 = driver.find_element(By.LINK_TEXT, value="Sign in").click()
  email_txtbox = driver.find_element(By.ID, value="username").send_keys(f"{username}")
  password_txtbox = driver.find_element(By.ID, value="password").send_keys(f"{password}")
  signin_button_2 = driver.find_element(By.CLASS_NAME, value="from__button--floating").click()

  job_list = driver.find_elements(By.CLASS_NAME, value="jobs-search-results__list-item")
  for job in job_list:
    time.sleep(.2)
    job.click()
    
    time.sleep(.2)
    save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")

    time.sleep(.2)
    save_button.click()


# time.sleep(100)





driver.quit()


"""
<button class="modal__dismiss btn-tertiary h-[40px] w-[40px] p-0 rounded-full indent-0
                contextual-sign-in-modal__modal-dismiss absolute right-0 m-[20px] cursor-pointer" aria-label="Dismiss" data-tracking-control-name="public_jobs_contextual-sign-in-modal_modal_dismiss">
              <icon class="contextual-sign-in-modal__modal-dismiss-icon lazy-loaded" aria-hidden="true" aria-busy="false"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" class="artdeco-icon lazy-loaded" focusable="false" aria-busy="false">
  <path d="M20,5.32L13.32,12,20,18.68,18.66,20,12,13.33,5.34,20,4,18.68,10.68,12,4,5.32,5.32,4,12,10.69,18.68,4Z" fill="currentColor"></path>
</svg></icon>
            </button>
"""

