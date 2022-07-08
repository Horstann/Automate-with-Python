from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

# Some important variables
website = 'https://www.thesun.co.uk/sport/football/'
path = "C:/Program Files/chromedriver"

# Create driver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
# Open driver
driver.get(website)

# Paste XPath
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

# Store data in a csv
headlines = {'titles': [], 'subtitles': [], 'links': []}
for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text
    subtitle = container.find_element(by="xpath", value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    
    headlines['titles'].append(title)
    headlines['subtitles'].append(subtitle)
    headlines['links'].append(link)

df = pd.DataFrame(headlines)
df.to_csv('02a_headlines.csv')

# Close driver
driver.quit()