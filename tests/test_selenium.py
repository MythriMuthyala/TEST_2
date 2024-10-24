from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH or provide its full path here

# Open a webpage
driver.get("https://www.example.com")

# Assert the page title
assert "Example Domain" in driver.title

# Interact with the page (if needed)
elem = driver.find_element_by_tag_name("h1")  # Find an element, e.g., the h1 tag
print(elem.text)

# Wait for a few seconds and close the browser
time.sleep(2)
driver.quit()
