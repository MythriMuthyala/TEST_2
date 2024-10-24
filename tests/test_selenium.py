from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Set up WebDriver (this example uses Chrome)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search box using its name attribute
search_box = driver.find_element("name", "q")

# Type a search query
search_box.send_keys("Selenium testing in Windows")

# Simulate pressing the Enter key
search_box.send_keys(Keys.RETURN)

# Close the browser
driver.quit()
