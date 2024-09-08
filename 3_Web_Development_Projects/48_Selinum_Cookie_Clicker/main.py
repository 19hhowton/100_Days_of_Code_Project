import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

## Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# my_element_id = 'something123'
# ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
# your_element = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
#                         .until(expected_conditions.presence_of_element_located((By.ID, my_element_id)))

""" PLANNING
create list of price_of_item
create dictionary of {id_of_item: price_of_item}
    ...can i click just using id of the item?
loop through items:
    if we have enough money to buy the item via item_list working from largest to smallest item:
        buy the item -- search dictionary for matching price & click on the button with id_of_item

EVENTUAl CONSIDERATIONS
* Algorithm to get most amount of value for cookies (add in a few seconds delay to really built up the cookie count)
* remove the last item later after you\ve created the dictionary ...for item in items[:-1]:... this fails...spacey_price = (item_name).split("-")[1]
* create a function for removing commas

### Can I use regex to get the item? 
# reobject = re.compile(pattern)
# result = reobject.match(string)
"""
driver = webdriver.Chrome()
link = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(link)

## USING PRICE LIST ##
def get_price_list():
    price_list = []
    item_names = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    for item in item_names[:-1]:
        item_price = int(item.text.split("-")[1].strip().replace(",",""))
        price_list.append(item_price)
    return price_list

def get_id_list():
    id_list = []
    items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    for item in items[:-1]:
        item_id = item.get_attribute('id')
        id_list.append(item_id)
    return id_list

## MONEY ## 
def get_money():
    cookie_count = driver.find_element(by=By.ID, value="money").text
    money = int(cookie_count.replace(",",""))
    return money

## ITER ##
""""""
### BREAKS AT GRANDMA :( WHYYY 
cookie = driver.find_element(By.ID, value="cookie")
price_list = get_price_list()
id_list = get_id_list()

timeout = time.time() + 30

for i in range(0,1000):
    cookie = driver.find_element(By.ID, value="cookie").click()
    
    if time.time() > timeout:
        for j in range(0, len(price_list)):
            money = get_money()
            price_list = get_price_list()

            price = price_list[j]  
            id = id_list[j]

            if price <= money:
                print(money, id, price) 

                # driver.refresh()
                button = driver.find_element(By.ID, value=f"{id}").click()  
                print(f"{id} bought for {price}")

"""
### ONLY FOR GRANDMA
cookie = driver.find_element(By.ID, value="cookie")
price_list = get_price_list()
id_list = get_id_list()

timeout = time.time() + 2

for i in range(0,1000):
    cookie.click()
    
    if time.time() > timeout:
        money = get_money()
        price_list = get_price_list()

        price = price_list[1]  
        id = id_list[1]

        if price <= money:
            print(price, id, money) 

            button = driver.find_element(By.ID, value=f"{id}")  
            button.click()
            print(f"{id} bought for {price}")
"""

"""
### ONLY CURSOR
for i in range(0,100):
    cookie.click()

    money = get_money()
    
    price_list = get_price_list()
    cursor_price = price_list[0]  
    cursor_id = id_list[0]

    if money == cursor_price:
        print(money, cursor_price) 

        # print(items_dict)
        # item_id = "buyCursor"
        # button = driver.find_element(By.ID, value=f"{item_id}")  
        button = driver.find_element(By.ID, value=f"{cursor_id}")  
        button.click()
        print(f"{cursor_id} bought for {cursor_price}")
""" 



""""""


"""
### DICTIONARY ERROR ###

def get_items_dict():
    items_dict = {}
    items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    for i in range(0,len(items)-1):
    # for item in items[:-1]:
        ## ITEM ID ##
        item_id = items[i].get_attribute('id')

        ## ITEM PRICE ## 
        # print(items[i])
        item_name = items[i].find_element(By.CSS_SELECTOR, value="b").text
        # print(item_name)
        spacey_price = (item_name).split("-")[1]
        item_price = int(spacey_price.replace(",",""))
        
        ## CREATE DICTIONARY ##
        items_dict[i] = {
            "item_id": item_id,
            "item_price": item_price
        }
    return items_dict

# items_dict = get_items_dict()
# cursor = items_dict[0]
# print(cursor['item_price'])

cookie = driver.find_element(By.ID, value="cookie")
items_dict = get_items_dict()

for i in range(0, 100):
    cookie.click()

    money = get_money()

    cursor = items_dict[0]  

    if money == cursor['item_price']:
        print(money, cursor['item_price']) 

        item_id = cursor["item_id"] 
        button = driver.find_element(By.ID, value=f"{item_id}")  
        button.click()
        print("Button clicked")
"""







"""
cookie = driver.find_element(By.ID, value="cookie")

for i in range(0,100):
    cookie.click()
    
    # cursor = driver.find_element(By.ID, value="buyCursor")  
    cursor = driver.find_element(By.LINK_TEXT, value='Cursor')
    cookie_count = driver.find_element(by=By.ID, value="money").text
    cursor_b = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b").text
    cursor_cost = cursor_b.split(" ")[2]

    if int(cookie_count) == int(cursor_cost):
        print(cookie_count, cursor_cost) 
        cursor.click()

"""



driver.quit()