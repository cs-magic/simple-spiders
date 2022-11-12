from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driverfile_path = '/Users/mark/Downloads/downloaded-zips/chromedriver'

one_driver = webdriver.Chrome(executable_path=driverfile_path)
options=Options() # 忽略无用的日志 options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# WebDriver 实例对象的get方法 可以让浏览器打开指定网址

one_driver.get('http://www.bicpa.org.cn/dtzj/zxgg/index.html')

search_button = one_driver.find_elements(By.CLASS_NAME, 'a_gray')
for u in search_button:
    print(u.text)
 
sleep(5)
one_driver.close()  


   








