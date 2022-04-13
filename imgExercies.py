from selenium import webdriver
#from time import sleep
driver=webdriver.Chrome()
#driver.get("https://www.baidu.com")
#driver.find_element_by_xpath(".//*[@id='kw']").send_keys("python")
#driver.find_element_by_css_selector("#su").click()
#sleep(2)
#driver.get_screenshot_as_file(r"F:\scrrenshot\baidu.png")
#sleep(2)
driver.get("http://www.51zxw.net")
#driver.find_element_by_link_text("网页设计").click()        #要截圖的頁面
driver.get_screenshot_as_file("1.png") #截圖格式和存放地址
#sleep(4)
driver.close()
