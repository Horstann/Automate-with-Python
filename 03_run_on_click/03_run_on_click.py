from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

# Prepare to run on a regular basis
from datetime import datetime
import os
import sys

# Prepare to create an executable
app_path = os.path.dirname(sys.executable)

now = datetime.now() # get today's date & time
now = now.strftime("%m%d%Y") # convert to format MMDDYYYY

# Some important variables
website = 'https://www.thesun.co.uk/sport/football/'
path = "C://Program\ Files/chromedriver"

# Create driver & activate Headless mode - doesn't open browser, all done in background
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
# Open driver
driver.get(website)

# Paste XPath
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

# Store data
headlines = {'titles': [], 'subtitles': [], 'links': []}
for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text
    subtitle = container.find_element(by="xpath", value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    
    headlines['titles'].append(title)
    headlines['subtitles'].append(subtitle)
    headlines['links'].append(link)

# Store csv in app_path
df = pd.DataFrame(headlines)
file_name = f'03_headlines_{now}.csv'
final_path = os.path.join(app_path, file_name)
df.to_csv(final_path)

# Close driver
driver.quit()

# Now run the below in terminal, make sure you're in the folder
"""
pip install pyinstaller
pyinstaller --onefile <py filename>
"""
# the executable will be found in the "dist" folder