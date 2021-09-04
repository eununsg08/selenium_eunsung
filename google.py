from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'D:\code\selenium\chromedriver.exe')
driver.get("https://www.google.co.kr/")
elem = driver.find_element_by_name("q")
elem.send_keys("환경오염 일러스트")
elem.send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element_by_class_name("hide-focus-ring").click()
driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[2]/div[2]/div/div').click()
time.sleep(0.7)
driver.find_element_by_class_name("xFo9P r9PaP").click()

# SCROLL_PAUSE_TIME = 1
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)
#     new_height = driver.execute_script("return document.body.scrollHeight") 
#     if new_height == last_height:
#         try:
#             driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
#         except:
#             break
#     last_height = new_height

# imges = driver.find_elements_by_class_name("wXeWr.islib.nfEiy.mM5pbd")
# count = 0
# for imge in imges:
#     imge.click()
#     time.sleep(3)
#     imgUrl = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
#     urllib.request.urlretrieve(imgUrl,"환경오염." + str(count + 1) + ".jpg")
#     count +=1
#     if count == 1000:
#         break
# driver.close()