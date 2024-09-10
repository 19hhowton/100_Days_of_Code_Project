from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://google.com/')

driver.set_window_size(1024, 600)
driver.maximize_window()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.ChromeDriver(options)


