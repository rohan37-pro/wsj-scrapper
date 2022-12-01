from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import json
import sys
import pyexcel
from time import sleep

def credentials():
	with open('credentials.txt','r') as file:
		data = file.read()
		data = json.loads(data)
		username = data['user_name'].strip()
		password  = data["password"].strip()
	return username , password


def login():
	options = webdriver.ChromeOptions()
	options.add_argument('--user-data-dir=./user')
	driver = webdriver.Chrome("./chromedriver",options=options)
	driver.get("https://accounts.wsj.com/login")
	sleep(3)

	username, password  = credentials()
	print(username, password)

	element = driver.find_element('xpath', "(//div[@class='fancy-text-input'])[1]//input")
	element.send_keys(username)
	action = ActionChains(driver)
	action.send_keys(Keys.ENTER).perform()
	sleep(3)
	action.send_keys(password).send_keys(Keys.ENTER).perform()
	sleep(5)

	element = driver.find_element('xpath', "//button[@class='solid-button reg-rtl-btn']")
	element.click()

	sleep(2)
	driver.quit()




def main():
	try:
		if sys.argv[1] == 'login':
			login()
	except:
		pass

	options = webdriver.ChromeOptions()
	options.add_argument('--user-data-dir=./user')

	driver = webdriver.Chrome("./chromedriver",options=options)

	driver.get("https://www.wsj.com/news/types/crypto?mod=breadcrumb")
	sleep(2)

	article_list = []
	for i in range(1,4):
	
		stories = driver.find_element('xpath',f"(//div[@id='latest-stories']//article[{i}]//a)[2]")
		author = driver.find_element('xpath',f"(//div[@id='latest-stories']//article[{i}]//p)[2]")
		date = driver.find_element('xpath',f"(//div[@id='latest-stories']//article[{i}]//p)[3]")
		image = driver.find_element('xpath',f"(//div[@id='latest-stories']//article[{i}]//img)")
		head_line = driver.find_element('xpath',f"(//div[@id='latest-stories']//article[{i}]//span)[1]")

		author = author.text
		date = date.text
		head_line = head_line.text
		image = image.get_attribute('src')
		article = stories.get_attribute("href")
		article_list.append(article)

		print(f"author {author}")
		print(f"date {date}")
		print(f"image {image}")
		print(f"article {article}")
		print(f"head_line {head_line}")
		print()	


	add_para = ''
	for article in article_list:
		driver.get(article)
		sleep(2)

		paragraphs = driver.find_elements('xpath', "//section//p[@data-type='paragraph']")

		for p in paragraphs:
			add_para += p.text + '\n'

		print(add_para)
		print()
		print()
		print()
		print()
		print()
		print()
	

if __name__ == "__main__":
	main()

	

