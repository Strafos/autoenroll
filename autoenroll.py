import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import config 

driver = webdriver.Chrome()
driver.get('https://studentcenter.cornell.edu')
time.sleep(1)

filename = 'logs+' + time.strftime('%I-%M') + '.txt'
f = open(filename, 'w')

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

def log():
    class_name = driver.find_elements_by_xpath('//*[contains(@id, "win0divR_CLASS_NAME")]')
    message = driver.find_elements_by_xpath('//*[contains(@id, "win0divDERIVED_REGFRM1_SS_MESSAGE")]')
    for i in range(len(class_name)):
        f.write(class_name[i].text + ' ' + message[i].text + '\n')

def cycle():
    driver.find_element_by_xpath('//*[@id="DERIVED_REGFRM1_LINK_ADD_ENRL$82$"]').click() # Proceed to Step 2 of 3
    time.sleep(page_time)
    driver.find_element_by_xpath('//*[@id="DERIVED_REGFRM1_SSR_PB_SUBMIT"]').click() # Finish Enrolling
    time.sleep(page_time)
    log()
    driver.find_element_by_xpath('//*[@id="DERIVED_REGFRM1_SSR_LINK_STARTOVER"]').click() # Add another class 
    time.sleep(page_time)

while True:
    cycle()

driver.quit()