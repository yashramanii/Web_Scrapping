# _4rR01T = phone

# _30jeq3 _1_WHN1 = price

from selenium import webdriver
# import requests
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/home/yashramani/Downloads/chromedriver_linux64 (94.0.4606.61)/chromedriver")

url = "https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_1"

driver.get(url)

# all_details = driver.find_elements_by_class_name("_1AtVbE col-12-12")


# for a in all_details:
phones = driver.find_elements_by_class_name("_1AtVbE")

# print(len(phones))

# img = driver.find_element_by_class_name("_4rR01T")

# print(img.get_attribute('innerHTML'))

for phone in phones:

    # print(phone.get_attribute('innerHTML'))

    phone_name = phone.find_element_by_xpath(By.xpath("//div[contains(@class,'_4rR01T')]"))

    price = phone.find_element_by_xpath(By.xpath("//div[contains(@class,'_25b18c')]"))

    print(phone_name.get_attribute('innerHTML'), price.get_attribute('innerHTML'))
    

# .findElement(By.xpath("//div[contains(@class,'Small')]"));