import selenium.webdriver as webdriver
import cv2

# screenshot
driver = webdriver.Chrome()
driver.get("https://edition.cnn.com/")
driver.get_screenshot_as_file("./screenshot.png")
driver.close()

# change image size
origin_img = cv2.imread("./screenshot.png")
resize_img = cv2.resize(origin_img, (300, 100))
cv2.imwrite("./resized.png", resize_img)



