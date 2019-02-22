from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from creds import *
import time, os

try:
    coned_username = os.environ['coned_username']
    coned_password = os.environ['coned_password']
    national_grid_username = os.environ['national_grid_username']
    national_grid_password = os.environ['national_grid_password']
    optimum_username = os.environ['optimum_username']
    optimum_password = os.environ['optimum_password']
except KeyError:
    pass


driver = webdriver.Chrome()
while True:

    # OPTIMUM
    driver.get("https://www.optimum.net/login")
    login_field = driver.find_element_by_id("loginPageUsername")
    pword_field = driver.find_element_by_id("loginPagePassword")
    login_field.send_keys(optimum_username)
    pword_field.send_keys(optimum_password)
    pword_field.send_keys(Keys.RETURN)
    driver.implicitly_wait(2)
    optimum_balance = float(driver.find_element_by_xpath("//*[@id='site-wrapper']/section[1]"
                                 "/section[3]/div/div/div[2]/div/section/div"
                                 "/div[2]/div[1]/div[1]/div[2]/span[1]"
                                 "/span[2]").text[1:])
    # NATIONAL GRID
    driver.get("https://online.nationalgridus.com/login/"
               "LoginActivate?applicurl=aHR0cHM6Ly9vbmxpbm"
               "UubmF0aW9uYWxncmlkdXMuY29tL2VzZXJ2aWNlX2VudQ==&auth_method=0")
    login_field = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[4]/"
                                               "table[5]/tbody/tr[2]/td[1]/form/"
                                               "table/tbody/tr[2]/td[1]/table/"
                                               "tbody/tr[2]/td[2]/input")
    pword_field = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[4]/"
                                               "table[5]/tbody/tr[2]/td[1]/form/"
                                               "table/tbody/tr[2]/td[1]/table/"
                                               "tbody/tr[3]/td[2]/input")
    login_field.send_keys(optimum_username)
    pword_field.send_keys(optimum_password)
    pword_field.send_keys(Keys.RETURN)
    driver.implicitly_wait(3)
    driver.switch_to_frame("_sweclient")
    driver.switch_to_frame("_sweview")
    nat_grid_balance = float(driver.find_element(By.ID, 's_4_1_15_0').text[1:])

    time.sleep(2629800)