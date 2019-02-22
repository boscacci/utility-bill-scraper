from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yagmail

from creds import *
"""
In a .py module called creds you will need to set these vars:
mygmailusername = 
mygmailpassword = 
optimum_username = 
optimum_password = 
national_grid_username = 
national_grid_password = 
coned_username = 
coned_password = 
coned_mfa_code = 
"""

driver = webdriver.Chrome()

# OPTIMUM:
driver.get("https://www.optimum.net/login")
login_field = driver.find_element_by_id("loginPageUsername")
pword_field = driver.find_element_by_id("loginPagePassword")
login_field.send_keys(optimum_username)
pword_field.send_keys(optimum_password)
pword_field.send_keys(Keys.RETURN)
pword_field.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

optimum_lastmonth = float(driver.find_element_by_xpath('//*[@id="site-wrapper"]/'
	'section[1]/section[3]/div/div/div[2]/div/section/div/div[2]/div[1]/div[1]'
	'/div[1]/span[1]/span[3]').text[1:])

# NATIONAL GRID:
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
login_field.send_keys(national_grid_username)
pword_field.send_keys(national_grid_password)
pword_field.send_keys(Keys.RETURN)
driver.implicitly_wait(8)
driver.switch_to_frame("_sweclient")
driver.switch_to_frame("_sweview")

nat_grid_lastmonth = float(driver.find_element_by_id('s_4_1_16_0').text[1:])

# CONED:
driver.get("https://www.coned.com/en/login")
login_field = driver.find_element_by_id("form-login-email")
pword_field = driver.find_element_by_id("form-login-password")
login_field.send_keys(coned_username)
pword_field.send_keys(coned_password)
pword_field.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
mfa_field = driver.find_element_by_id("form-login-mfa-code")
mfa_field.send_keys(coned_mfa_code)
mfa_field.send_keys(Keys.RETURN)
coned_lastmonth = float(driver.find_element_by_xpath('//*[@id="overview"]'
	'/div[1]/div[1]/div[1]/p/b').text[1:])

###
driver.quit()
###

# Format an email:
yag = yagmail.SMTP(mygmailusername, mygmailpassword)
to = 'santa@someone.com'
to2 = 'cinemarob1@gmail.com'
subject = 'Utility Bill Scraper — Report'
body = 'This is what utilities cost this past month:\n'
body += f'\nNational Grid: <b>${nat_grid_lastmonth}</b>.\n\n'
body += f'Optimum: <b>${optimum_lastmonth}</b>.\n\n'
body += f'Coned: <b>${coned_lastmonth}</b>.\n\n'
yag.send(to = [to, to2], subject = subject, contents = body)

