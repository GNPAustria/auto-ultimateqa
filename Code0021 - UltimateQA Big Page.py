# Code Number 0021
# Function: UltimateQA Big Page
# Browser Mode: Incognito
# Author: GPA

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# PREREQUISITE CODE (NECESSARY FOR INITIALIZATION) -- do not include in automation test steps

# PRQ 1: Create an instance of Edge Options
edge_options = Options()

# PRQ 2: Add the InPrivate argument
edge_options.add_argument("--inprivate")

# PRQ 3: Provide the path to your EdgeDriver executable -- note to always keep the driver updated.
edge_driver_path = "C:\\Users\\giana\\Downloads\\edgedriver_win64\\msedgedriver.exe"
service = Service(executable_path=edge_driver_path)

# PRQ 4: Create new instance of the Edge driver
driver = webdriver.Edge(service=service, options=edge_options)  # Use Edgedriver

# AUTOMATION SUITE (Test Steps start here)

# 1. Access the website: UltimateQA Automation.
driver.get("https://ultimateqa.com/automation")
time.sleep(2) # allot enough time to load page

# 2. Click the button with text, "Big page..."
wait = WebDriverWait(driver, 5)
bigpage_option = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Big page')]")))
bigpage_option.click()
time.sleep(5)

# 3. Click any of the 12 buttons that say, "Button".
driver.find_element(By.CLASS_NAME, "et_pb_button_6").click()
time.sleep(2)

# 4. Click an X (Twitter) icon.
dest_url = "https://twitter.com/Nikolay_A00"
button = driver.find_element(By.XPATH, f"//a[@href='{dest_url}']")
ActionChains(driver).move_to_element(button).perform()
button.click()
time.sleep(10)

# End result: Successful access of Big Page and Twitter.
