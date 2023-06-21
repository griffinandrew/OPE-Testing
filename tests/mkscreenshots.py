from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import platform
import sys
import time

if len(sys.argv) <= 1:
    print("Invalid number of arguments")
    exit(1)

token = sys.argv[1]
url = "http://127.0.0.1:8888/lab?token=" + token
chrome_options = Options()

if platform.system() == 'Windows' or platform.system() == 'Darwin':
    chrome_options.add_experimental_option('detach', True)
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()), options=chrome_options)
elif platform.system() == 'Linux':
    chrome_options.add_argument('--headless') # Inorder for Action to run, it needs to be headless
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chrome_options)
else:
    print("Unknown OS")
    exit(1)

driver.get(url)

time.sleep(10)

driver.save_screenshot('main_screenshot.png')
print("Saved main screenshot")

new_nb_button = driver.find_element(By.XPATH, '//div[@data-category="Notebook"]')
new_nb_button.click()
time.sleep(10)

driver.save_screenshot('new_nb_screenshot.png')
print("Saved new notebook screenshot")

rise_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:preview"]')
rise_button.click()
time.sleep(10)

driver.save_screenshot('rise_screenshot.png')
print("Saved rise screenshot")







