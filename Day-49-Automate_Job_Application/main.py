from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sleep(2)
signin_btn = driver.find_element(By.CSS_SELECTOR, value=".sign-in-modal__outlet-btn")
signin_btn.click()

MY_EMAIL = "rakin.100daysofcode@gmail.com"
MY_PASSWORD = "100daysofcoderakin"
MY_NUMBER = "0123456789"
sleep(1)
email_box = driver.find_element(By.CSS_SELECTOR, value="#base-sign-in-modal_session_key")
password_box = driver.find_element(By.CSS_SELECTOR, value="#base-sign-in-modal_session_password")
signin_btn = driver.find_element(By.CSS_SELECTOR, value=".sign-in-form__submit-btn--full-width")

email_box.send_keys(MY_EMAIL)
password_box.send_keys(MY_PASSWORD)
signin_btn.click()

easy_apply_btn = driver.find_element(By.CLASS_NAME, value="jobs-apply-button")
easy_apply_btn.send_keys(Keys.ENTER)

number_box = driver.find_element(By.CLASS_NAME, value="artdeco-text-input--input")
number_box.send_keys(MY_NUMBER)

next_btn = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
next_btn.click()

next_btn = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
next_btn.click()

if driver.find_elements(By.ID, value="text") == "Yes":
    yes_options = driver.find_elements(By.CLASS_NAME, value="t-14")
    for yes_btn in yes_options:
        yes_btn.click()

next_review_btn = driver.find_element(By.XPATH, value="next_btn2 = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')")
next_review_btn.click()