from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Some important variables
form = 'https://docs.google.com/forms/d/e/1FAIpQLSek4lvyKCkjeKHJwRRSUdsNb4WCIohFNlog7YjeWVzmEr3DQQ/viewform'
path = "C:/Program Files/chromedriver"

# Create driver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
# Open driver
driver.get(form)

# Wait for browser to render HTML
import time
time.sleep(2) # wait for 2 seconds

# Retrieve HTML elements
lastName_text_box = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
firstName_text_box = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
radio_button = driver.find_element(by="xpath", value='//*[@id="i13"]/div[3]/div')
submit_button = driver.find_element(by="xpath", value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

# Type into elements
lastName_text_box.send_keys("Test")
firstName_text_box.send_keys("Test")
# Click element
radio_button.click()
submit_button.click()

# Validate if form submitted
confirmation_text =  driver.find_element(by="xpath", value='/html/body/div[1]/div[2]/div[1]/div/div[3]').text
if confirmation_text == "Thank you for attending":
    print("Submitted!")
else:
    raise Exception("Failed to submit form!")

# Close driver
driver.quit()