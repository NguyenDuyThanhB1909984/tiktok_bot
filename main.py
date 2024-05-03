import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

# service = Service(executable_path=r'chromedriver.exe')

options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-data-dir=Profile")

bot = webdriver.Chrome(options=options)
# bot = webdriver.Chrome(service=service, options=options)

bot.get("https://studio.youtube.com")
time.sleep(3)
bot.save_screenshot("image/image.png")
bot.quit()





