from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install(), chrome_type=ChromeType.GOOGLE), options=chrome_options)
    #add this from rise_test bc complaining about version of chrome in this test now
    #driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chrome_options) #kes og command, updated due to chrome vers mismatch
else:
    print("Unknown OS")
    exit(1)

driver.get(url)

time.sleep(10)

driver.save_screenshot('main_screenshot.png')
print("Saved main screenshot")

wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds

new_nb_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-category="Notebook"]')))
#new_nb_button = driver.find_element(By.XPATH, '//div[@data-category="Notebook"]')

new_nb_button.click()
time.sleep(10)

driver.save_screenshot('new_nb_screenshot.png')
print("Saved new notebook screenshot")

rise_button = driver.find_element(By.XPATH, '//button[@data-command="RISE:preview"]')
rise_button.click()
time.sleep(10)

driver.save_screenshot('rise_screenshot.png')
print("Saved rise screenshot")


