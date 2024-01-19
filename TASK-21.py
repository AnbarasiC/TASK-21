"""Using Python Selenium Automation and the URL https://www.saucedemo.com/
display the Cookie created before login and after login in the console.
After you login into the dashboard of the Zen portal kindly do the logout also.
Verify that the Cookies are being generated during the Login process."""

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Open the URL
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

# Display the Cookie created before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:")
for cookie in cookies_before_login:
    print(cookie)

# Login
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys('standard_user')
driver.find_element(By.XPATH,"//input[@id='password']").send_keys('secret_sauce')
driver.find_element(By.XPATH,"//input[@id='login-button']").click()

# Wait for login to complete
sleep(3)

# Display the Cookie after login
cookies_after_login = driver.get_cookies()
print("Cookies after login:")
for cookie in cookies_after_login:
    print(cookie)

# Wait for the element to be visible
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@id='react-burger-menu-btn']")))

# Perform click action on the element
element.click()

sleep(3)

# Logout from the dashboard
logout_btn = driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()

# Close the browser
driver.quit()