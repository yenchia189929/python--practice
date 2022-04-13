from bs4 import BeautifulSoup
import requests, os, cv2, re

# URL 
prefix = "https://www.w3schools.com/"
urls = ["python/default.asp", "bootstrap/bootstrap_ver.asp", "pro/index.php"]

# create a image folder
os.system("rm -rf images ;mkdir images")

# loop the urls
for url in urls:
	# find img tags
	r = requests.get(prefix + url)
	soup = BeautifulSoup(r.content, "lxml")
	imgs = soup.find_all("img")
	
	for img in imgs:
		# get img name
		name = img['src'].split('/')
		# curl the img
		s = "curl -o ./images/" + name[-1] + " " + prefix + img['src']
		os.system(s)

		# resize the pic
		# i only resize the png and jpeg file
		if re.findall(".png", name[-1]) or re.findall("jpeg", name[-1]) or re.findall(".jpg", name[-1]):
			origin_img = cv2.imread("./images/" + name[-1])
			resize_img = cv2.resize(origin_img, (100, 100))
			cv2.imwrite("./images/" + name[-1], resize_img)






