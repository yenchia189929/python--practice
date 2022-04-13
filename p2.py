from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import re

driver = webdriver.Chrome()
driver.get("https://tip.railway.gov.tw/tra-tip-web/tip?lang=EN_US")

# select the request value
# since this system is really cunning that we cant get the query result by the url's parameter, i think this is the only way to do it
# just use the selenium method!
startStation = driver.find_element(By.ID, "startStation")
startStation.send_keys("1040-Shulin")
endStation = driver.find_element(By.ID, "endStation")
endStation.send_keys("7000-Hualien")
rideDate = driver.find_element(By.ID, "rideDate")
rideDate.clear()
rideDate.send_keys("20220603")
startTime = Select(driver.find_element(By.ID, "startTime"))
startTime.select_by_visible_text("06:00")
endTime = Select(driver.find_element(By.ID, "endTime"))
endTime.select_by_visible_text("18:00")
driver.find_element(By.CSS_SELECTOR, ".btn-basic").click()

# get source time table
tb = pd.read_html(driver.page_source)[0]

# create the data frame table, col variable is the column name i found in the tb table, cnt = index count
col = ["Train type and code", "Orginating Station", "Terminal Station", "Departure time", "Arrival time", "Travel time", "Via", "Adult", "Discount"]
df = pd.DataFrame([], columns = col)
cnt = 0

# there're lots of noisy data dump from the table, we can observe that there is a increment with 5 between two data.
for i in range(0, len(tb), 5):
	cnt += 1
	# variable tmp is used to split the "Train type and code(Originating → Terminal Station)" to "Train type and code" & "stations", 
	# i split the data by " ( " by my observation
	tmp = tb["Train type and code(Originating → Terminal Station)"][i].split(" ( ")
	trainTypeAndCode = tmp[0]
	#split the start and end station by the regular expression, there is only alphabet in the word
	station = re.findall(r"[a-zA-Z]+", tmp[1])
	# create a new df row and concat it to the df data frame we create initially
	row_df = pd.DataFrame([[trainTypeAndCode, station[0], station[1], tb["Departure time"][i], tb["Arrival time"][i], tb["Travel time"][i], tb["Via"][i], tb["Adult"][i], tb["Discount"][i]]], columns = col, index = [str(cnt)])
	df = pd.concat([df, row_df])

df.to_csv("mid.csv")


driver.close()







