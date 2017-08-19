import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import config 

driver = webdriver.Chrome()
driver.get('https://studentcenter.cornell.edu')
time.sleep(1)

# Log in
actions = ActionChains(driver)
actions.send_keys(config.USR + Keys.TAB + config.PW + Keys.ENTER)
actions.perform()
time.sleep(3)

# Cycle through enrolling pages 
page_time = 2
driver.switch_to_frame('ptifrmtgtframe')
driver.find_element_by_xpath('//*[@id="DERIVED_SSS_SCR_SSS_LINK_ANCHOR3$span"]').click()
time.sleep(page_time)

def cycle():
    driver.find_element_by_xpath('//*[@id="DERIVED_REGFRM1_LINK_ADD_ENRL$82$"]').click()
    time.sleep(page_time)
    driver.find_element_by_xpath('//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]').click()
    time.sleep(page_time)
    driver.find_element_by_xpath('//*[@id="DERIVED_REGFRM1_SSR_LINK_STARTOVER"]').click()
    time.sleep(page_time)

while True:
    cycle()

driver.quit()
