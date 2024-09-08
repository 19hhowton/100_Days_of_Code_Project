from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

## Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()



##### Amazon Price Tracker ##### 
"""
link = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS?th=1"
driver.get(link)

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cent.text}") """



##### Notes #####
""" 
link = "https://www.python.org/"
driver.get(link)
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name) #get the tag name of the search_bar object
# print(search_bar.get_attribute("placeholder")) #get any attribute in search_bar object

# search_button = driver.find_element(By.ID, value="submit")
# print(search_button.tag_name) #get the tag name of the search_bar object
# print(search_button.size) #get any attribute in search_bar object

# docs_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a") #class has dot . 
# print(docs_link.text)
# print(docs_link.get_attribute("href"))

# beginners_guide_link = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[1]/div[1]/p[2]/a')
# print(beginners_guide_link.text)
# print(beginners_guide_link.get_attribute("href"))
"""



####### CHALLENGE 347: Python Conference Events #######
'''
link = "https://www.python.org/"
driver.get(link)
event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time') ## You don't have to have the whole path! 
# event_times_lists = [time.text for time in event_times]
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
# event_names_lists = [name.text for name in event_names]

event_dict = {}
for i in range(0, len(event_times)):
    event_dict[i] = {
        "Time": (event_times[i]).text,
        "Event": (event_names[i]).text 
    }
print(event_dict)
'''



####### CHALLENGE 348: WIKIPEDIA #######
# link = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(link)

## Click 
# stat = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# print(stat.get_attribute("href"))
# print(stat.text)
# stat.click()

## Link Text
# stat = driver.find_element(By.LINK_TEXT, value='Frye Fire')
# stat.click()

## Search Bar and Send Keyboard Input
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)



####### CHALLENGE 349: FILL FORM #######
"""
link = "https://secure-retreat-92358.herokuapp.com/"
driver.get(link)

top_bar = driver.find_element(By.CLASS_NAME, value="top")
middle_bar = driver.find_element(By.CLASS_NAME, value="middle")
bottom_bar = driver.find_element(By.CLASS_NAME, value="bottom")
# print(top_bar.get_attribute("name"))

top_bar.send_keys("Heather")
middle_bar.send_keys("Howton")
bottom_bar.send_keys("19hhowton@gmail.com")

submit_button = driver.find_element(By.CSS_SELECTOR, value="form button")
# submit_button = driver.find_element(By.CLASS_NAME, value="btn-block")
print(submit_button.text)
submit_button.click()
"""


# driver.close()
driver.quit()
