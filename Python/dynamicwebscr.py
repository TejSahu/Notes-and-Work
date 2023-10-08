from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# instantiate options
options = webdriver.ChromeOptions()

# pass arguments now this way
options.add_argument('--headless')
# instantiate driver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

# load website
url = 'https://angular.io/'

# get the entire website content
driver.get(url)

# select elements by class name
elements = driver.find_elements(By.CLASS_NAME, 'text-container')
for title in elements:
    # select H2s, within element, by tag name
    heading = title.find_element(By.TAG_NAME, 'h2').text
    # print H2s
    print(heading)
