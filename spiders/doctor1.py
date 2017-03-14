import requests
from selenium import webdriver
import time
import PyV8
from io import StringIO


web_url = 'https://www.91160.com/doctors/index/docid-1286.html'
url = 'http://www.newhealth.com.cn/doctor/34c015acc16b434a93564f3973da3734.html?deptID=8754e4f9246b4f54ac6605988e08daa4&hospitalID=3cd2a5b55e5f4d35b6048c8fba573804'
w = webdriver.Chrome()
w.get(web_url)
# w.get(url)
time.sleep(2)
# print(w.title)
# dl = w.find_element_by_css_selector('ul.doctablist li.current').click()
n = w.find_element_by_css_selector('.fs24.fl').text
i = w.find_element_by_css_selector('.righr_side_content.pt10.cl6>p').text
# i = w.find_element_by_css_selector('.doc-tx>a').text
print(n)
print(i)
print(1111)
