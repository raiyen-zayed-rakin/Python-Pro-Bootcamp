from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.get("https://www.stackoverflow.com/")
driver.get("http://secure-retreat-92358.herokuapp.com/")
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# article_count.click()
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# search = driver.find_element(By.NAME, value="q")
# search.send_keys("Python", Keys.ENTER)

# Sending keyboard input to Selenium
# search.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

first_name.send_keys("Raiyen Zayed")
last_name.send_keys("Rakin")
email.send_keys("rakin69@gmail.com")

signup_btn = driver.find_element(By.CLASS_NAME, value="btn")
signup_btn.click()



#driver.quit()