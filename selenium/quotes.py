from bs4 import element
from selenium import webdriver

driver = webdriver.Chrome("/home/yashramani/Downloads/chromedriver_linux64 (94.0.4606.61)/chromedriver")

url = "http://quotes.toscrape.com/page/1/"

posts = driver.get(url)

# all = driver.find_elements_by_xpath('/html/body/div/div[2]/div[1]')


elements = driver.find_elements_by_class_name("quote")

# for e in elements:
#     q = e.find_element_by_class_name("text")
#     a = e.find_element_by_class_name("author")
#     t = e.find_element_by_class_name("tags")

#     print(q.text)
#     print(a.text)
#     print(t.text)
for v in elements:
    print(v.text, "\n")
# print(all.text)