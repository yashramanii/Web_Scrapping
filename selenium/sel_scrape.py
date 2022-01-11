from selenium import webdriver

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

driver = webdriver.Chrome("/home/yashramani/Downloads/chromedriver_linux64 (94.0.4606.61)/chromedriver")

driver.get(url)

jobs = driver.find_elements_by_class_name("joblist-comp-name")

for job in jobs:
    print(job.text)

experience = driver.find_elements_by_class_name("top-jd-dtl clearfix")

for e in experience:
    print(e.text)










#     comp_name = job.find_element_by_xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "joblist-comp-name", " " ))]').text
#     print(comp_name)

    # skills = job.find_element_by_class_name("srp-skills").text
    # title = jobs.find_element_by_class("joblist-comp-name").text

    

# comp_name = jobs.find_element_by_class_name("joblist-comp-name")
