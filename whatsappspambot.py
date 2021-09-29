import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


os.environ['PATH'] += r"Address"

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

#Scan the QR CODE between the 20 seconds

driver.implicitly_wait(20)

bot_path='//*[@title="YourContactNameHere"]'
message_xpath='//div[@data-tab="9"]'
bot=driver.find_element_by_xpath(bot_path)
bot.click()

#Spamming
for i in range(1000):
    message=driver.find_element_by_xpath(message_xpath)
    message.send_keys('Your Message Here')
    message.send_keys(Keys.ENTER)
    time.sleep(3)