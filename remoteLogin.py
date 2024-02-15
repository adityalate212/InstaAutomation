from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Wait for the login form to appear
wait = WebDriverWait(driver, 20)
login_form = wait.until(EC.presence_of_element_located((By.XPATH, "//form[@method='post']")))

# Enter your Instagram username and password
username_field = login_form.find_element(By.NAME, "username")
username_field.send_keys("your username")
password_field = login_form.find_element(By.NAME, "password")
password_field.send_keys("your password")

# Click the login button
login_button = login_form.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for the page to load after login
wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/%s/']" % "your_username")), 20)
time.sleep(5)

# Go to your profile page
driver.get("https://www.instagram.com/_adityalate212_/")

# Quit the driver
driver.quit()
